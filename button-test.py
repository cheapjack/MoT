#!/usr/bin/python

import serial

ser = serial.Serial('/dev/tty.SLAB_USBtoUART7', 9600, timeout=1)
x = ser.read()          # read one byte
s = ser.read(10)        # read up to ten bytes (timeout)
line = ser.readline()   # read a '\n' terminated line
print ("Read One Byte, message: " + x + "Read up to 10 bytes, msg:  " + s + line)
ser.close()
