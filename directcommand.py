#!/usr/bin/python3

import smbus
import time
import sys
import datetime

busAddress = 0x23
bc= 0b11111110

dali = smbus.SMBus(1)

def __waitForAnswer(busAddress):
    statusRegister = dali.read_byte_data(busAddress, 0x00)
    commandRegister = dali.read_byte_data(busAddress, 0x01)

    while statusRegister==0x40:
        print("{:s} BUSY {:08b}".format(str(datetime.datetime.now()), statusRegister))
        statusRegister = dali.read_byte_data(busAddress, 0x00)
        time.sleep(0.01)

    while statusRegister==0x04:
        print("{:s} REPLY TIMEFRAME {:08b}".format(str(datetime.datetime.now()), statusRegister))
        statusRegister = dali.read_byte_data(busAddress, 0x00)

    while statusRegister<0x08 and statusRegister>0x0b:
        print("{:s} status {:08b} | {:08b}".format(str(datetime.datetime.now()), statusRegister, commandRegister))
        statusRegister = dali.read_byte_data(busAddress, 0x00)
        commandRegister = dali.read_byte_data(busAddress, 0x01)


def __sendToBus(b1, b2, busAddress):
    print("send {:08b} {:08b}".format(b1,b2))

    message =[b1, b2]
    dali.write_i2c_block_data(busAddress, 0x01, message)
    __waitForAnswer(busAddress)

    #statusRegister = dali.read_byte_data(busAddress, 0x00)
    commandRegister = dali.read_byte_data(busAddress, 0x01)
    print("{:s} command {:08b} ".format(str(datetime.datetime.now()), commandRegister))


def sendBrightness(deviceAddress, brightness, busAddress):
    b1 = deviceAddress<<1 | 0
    b2 = brightness
    __sendToBus(b1, b2, busAddress)


def sendCmd(deviceAddress, cmd, busAddress):
    b1 = deviceAddress<<1 | 1
    b2 = cmd
    __sendToBus(b1, b2, busAddress)



sendCmd(0xff,32,busAddress)

#sendCmd(0x7f, 150, busAddress)

# for device in range(0, 64):
#     sendCmd(device, 150, busAddress)
#     sendBrightness(device, 0, busAddress)

# for b in range(0,255,1):
    # sendBrightness(0x7f, b, busAddress)

# for b in range(255,0,-1):
#     sendBrightness(0x7f, b, busAddress)

deviceAddress = int(sys.argv[1],16)
brightness = int(sys.argv[2],16)
sendBrightness(deviceAddress, brightness, busAddress)



#sendCmd(bc, 187, busAddress)
