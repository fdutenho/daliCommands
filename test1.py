#!/usr/bin/python3

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import daliMaster
import defines
import time

master = daliMaster.daliMaster()

if master.begin() == defines.ERROR :
    quit()
#master.clean()

daliAddress = master.getBroadcastAddress(defines.LW14_MODE_DACP)
print("-----")

print("bc off @", daliAddress)
print("waitForReady() ", master.waitForReady())
print("directCmd(daliAddress, 0)", master.directCmd(daliAddress, 0))
#print("waitForTelegram_1() ", master.waitForTelegram_1())
#print("waitForTelegram_2() ", master.waitForTelegram_2())
time.sleep(2)
print("-----")

print("bc on @", daliAddress)
if (master.waitForReady() == defines.ERROR) or (master.directCmd(daliAddress, 254) == defines.ERROR) :
    print("Error..")
time.sleep(2)
print("-----")


#for l in range(0, 64):
#    if (master.waitForReady() == defines.ERROR) or (master.directCmd(l, 0) == defines.ERROR) :
#        print("Error..")
#        time.sleep(0.02)
