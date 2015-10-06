#!/usr/bin/python

# Moteino Receiver for RF-Crafting and button-craft

from mcpi import minecraft
import server
import serial
from time import sleep

mc = minecraft.Minecraft.create(server.address)
# use the default mac serial port, '/dev/tty.SLAB_USBtoUART' this will change platform to platform
ser = serial.Serial('/dev/tty.SLAB_USBtoUART', 9600)
serialstring = ser.readline()
action = serialstring[0]
node = serialstring[2]
# The Button sends the serial message (action , node)
# node: "1", "Button Pressed"
#	"2", "Error"
#	"3", "OK"
 
mc.postToChat("Hello CloudMaker this is Serial " + str(ser.readline()))

if action == "1":
	#prints the port name for debugging
	#print ser.name
	#write an "OK" over serial back to the button id (node) 
	ser.write("3," + node)
	print "Sending : 3," + node
	#wait a moment
	sleep(0.5)
	# print the Message received
	print "Message from Button " + node + " " + ser.readline()
	print "Action Message Received is: " + action + " From Button no." + node
else:
	mc.postToChat("Action Message Received is: " + action + " From Button no." + node)
	print ser.readline()

ser.close
