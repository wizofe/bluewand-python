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


def pairWand():
    print("Let's pair...")
    # TODO Change to discover the closest device of type Wand-75
    try:
        # TODO Remove hardcoded address
        blueWand = btle.Peripheral('DF:92:F0:4A:F4:D5', btle.ADDR_TYPE_RANDOM)
        print('Hey. We paired.')
        sleep(1)
    except Exception as e:
        print('E: I am afraid I cannot connect: {}', e)
        sys.exit(0)


def lightShow():
    print('Let me show you some magic LEDs')

    ioSensor = btle.UUID(IO_SERVICE_UUID)
    ioService = blueWand.getServiceByUUID(ioSensor)

    led = btle.UUID(LED_CHAR_UUID)
    ledConfig = ioService.getCharacteristics(led)[0]

    ledConfig.write(bytes('\x07'))
    sleep(5)
    ledConfig.write(bytes('\x00'))
    sleep(0.5)

    print('Show is over now. Goodbye.')


pairWand()
lightShow()
