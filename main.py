#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import time

with ser = serial.Serial('/dev/tty.usbserial-XXXXXX',9600,timeout=None):
    line = ser.readline()
    print(line)
    time.sleep(1)
