# Fast hack to get the Wand data on Python
# Tested with the bluepy library on the KANO OS
# Python v3.5 compatible

# Copyright Ioannis Valasakis <code@wizofe.uk>
# Licensed under the GNU GPLv3.0

from bluepy import btle
from time import sleep
import sys

LED_CHAR_W = '0x001e'
LED_CHAR_UUID = '64A70009-F691-4B93-A6F4-0968F5B648F8'
IO_SERVICE_UUID = '64A70012-F691-4B93-A6F4-0968F5B648F8'
SENSOR_SERVICE_UUID = '64A70011-F691-4B93-A6F4-0968F5B648F8'


class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print("A notification was received: {}".format(data))


def pairWand():
    print("Looking for a magic wand...")
    # TODO Change to discover the closest device of type Wand-75
    try:
        global blueWand

        scanner = btle.Scanner()
        le_devices = scanner.scan(timeout=5)

        for dev in le_devices:
            # print("D: dvc {} ({}), RSSI={} dB".format(dev.addr, \
            # dev.addrType, dev.rssi))
            for (adtype, desc, value) in dev.getScanData():
                # print("D:  {}, {} = {}".format(adtype, desc, value))
                if ("Kano-Wand" in value):
                    print("I found a wand! A: {}".format(dev.addr))
                    MAC_ADDRESS = dev.addr

        if (MAC_ADDRESS is None):
            print("E: MAC_ADDRESS is not set (no Wand was found :/)...")
            exit(0)

        blueWand = btle.Peripheral(MAC_ADDRESS, btle.ADDR_TYPE_RANDOM)
        blueWand.setDelegate(MyDelegate())
        print('Hey. We paired.')
    except Exception as e:
        print('E: I am afraid I cannot connect: {}', e)
        sys.exit(0)


def rcv_data():
    svc = blueWand.getServiceByUUID(SENSOR_SERVICE_UUID)
    ch = svc.getCharacteristics()[2]
    blueWand.writeCharacteristic(ch.valHandle+1, "\x01\x00".encode('utf-8'))


def lightShow():
    print('Let me show you some magic LEDs')

    ioSensor = btle.UUID(IO_SERVICE_UUID)
    ioService = blueWand.getServiceByUUID(ioSensor)
    print('DEBUG io: {}'.format(ioService))
    led = btle.UUID(LED_CHAR_UUID)
    ledConfig = ioService.getCharacteristics(led)[0]

    # Blink the LED's
    print('DEBUG: led: {}'.format(ledConfig))
    ledConfig.write(bytes('07', 'UTF-8'))
    sleep(5)
    ledConfig.write(bytes('00', 'UTF-8'))
    sleep(0.5)

pairWand()
rcv_data()

while True:
    if blueWand.waitForNotifications(1.0):
        continue
    print("Waiting...")
