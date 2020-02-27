#!/usr/bin/python3

import smbus
import time
import datetime


busAddress = 0x23
dali = smbus.SMBus(1)

while 1:
    statusRegister = dali.read_byte_data(busAddress, 0x00)
    commandRegister = dali.read_byte_data(busAddress, 0x01)

    if(statusRegister>0):
        print("{:s} status {:08b} command {:08b} ".format(str(datetime.datetime.now()), statusRegister, commandRegister))

    if statusRegister>=0x08 and statusRegister<=0x0b:
        print("{:s} response received {:08b} command {:08b}".format(str(datetime.datetime.now()), statusRegister, commandRegister))

    if statusRegister==0x40:
        print("{:s} BUSY {:08b}".format(str(datetime.datetime.now()), statusRegister))

    if statusRegister==0x04:
        print("{:s} REPLY TIMEFRAME {:08b} ".format(str(datetime.datetime.now()),statusRegister))

    # answer = dali.read_i2c_block_data(busAddress, 0x02)
    # if(any(elem > 0 for elem in answer) > 0):
    #     print("{:s} config {:s} ".format(str(datetime.datetime.now()),str(answer)))

    # signatureRegister = dali.read_i2c_block_data(busAddress, 0xF0)
    # if(any(elem > 0 for elem in answer) > 0):
    #     print("{:s} signature {:s} ".format(str(datetime.datetime.now()),str(signatureRegister)))

    # answer = dali.read_i2c_block_data(busAddress, 0xFE)
    # if(any(elem > 0 for elem in answer) > 0):
    #     print("{:s} address {:s} ".format(str(datetime.datetime.now()),str(answer)))
