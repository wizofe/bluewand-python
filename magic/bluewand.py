# Fast hack to get the Wand data on Python
# Tested with the bluepy library on the KANO OS
# Python v2.x

from bluepy import btle
from time import sleep
import time
import binascii
import sys

LED_CHAR_W = '0x001e'
LED_CHAR_UUID = '64A70009-F691-4B93-A6F4-0968F5B648F8'
IO_SERVICE_UUID = '64A70012-F691-4B93-A6F4-0968F5B648F8'
DATA_SERVICE_UUID ='64A70011-F691-4B93-A6F4-0968F5B648F8'

class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print("A notification was received: {}".format(data))    


def pairWand():
    print("Let's pair...")
    # TODO Change to discover the closest device of type Wand-75
    try:
        # TODO Remove hardcoded address
        global blueWand
        blueWand = btle.Peripheral('DF:92:F0:4A:F4:D5', btle.ADDR_TYPE_RANDOM)
        blueWand.setDelegate(MyDelegate())
        print('Hey. We paired.')
        sleep(1)
    except Exception as e:
        print('E: I am afraid I cannot connect: {}', e)
        sys.exit(0)

def enable_notify(self, chara_uuid):
    setup_data = b"\x01\x00"
    notify = self.ble_conn.getCharacteristics(uuid=chara_uuid)[0]
    notify_handle = notify.getHandle() + 1
    self.ble_conn.writeCharacteristic(notify_handle, setup_data, withResponse=True)


def rcv_data():
    svc = blueWand.getServiceByUUID(DATA_SERVICE_UUID)
    ch = svc.getCharacteristics()[2]
    blueWand.writeCharacteristic(ch.valHandle+1, "\x01\x00".encode('utf-8'))

def lightShow():
    print('Let me show you some magic LEDs')

    ioSensor = btle.UUID(IO_SERVICE_UUID)
    ioService = blueWand.getServiceByUUID(ioSensor)
    print('DEBUG io: {}'.format(ioService))
    led = btle.UUID(LED_CHAR_UUID)
    ledConfig = ioService.getCharacteristics(led)[0]

    print('DEBUG: led: {}'.format(ledConfig))
    ledConfig.write(bytes('07', 'UTF-8'))
    sleep(5)
    ledConfig.write(bytes('00', 'UTF-8'))
    sleep(0.5)

    print('Show is over now. Goodbye.')


pairWand()
rcv_data()

while True:
    if blueWand.waitForNotifications(1.0):
        continue
    print("Waiting...")

