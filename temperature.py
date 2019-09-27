#!/usr/bin/python

import sys

cpuTempFile=open("/sys/class/thermal/thermal_zone0/temp","r")
cpuTemp=float(cpuTempFile.read())/1000
cpuTempFile.close()

if __name__ == "__main__":
    print(cpuTemp)

