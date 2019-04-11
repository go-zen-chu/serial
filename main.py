#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import time

with serial.Serial('/dev/tty.usbserial-XXXXXX',9600,timeout=None) as ser:
    while True:
        sbytes = serial.inWaiting()
        ser.read(sbytes)
