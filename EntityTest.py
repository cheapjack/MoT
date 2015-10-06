#!/usr/bin/python

# Moteino Receiver for RF-Crafting and button-craft
# RF Event listener
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
mc.postToChat("Hello CloudMaker this is Serial ")

#main loop
while True:
	blockEvents = mc.events.pollBlockHits()
	if blockEvents:
		#print "polling for a hit" + blockEvents
		for blockEvent in blockEvents:
			print blockEvent
			print blockEvent.pos.x
			print blockEvent.pos.y
			print blockEvent.pos.z
			print blockEvent.face
			print blockEvent.type
			print blockEvent.entityId
			mc.postToChat(str(blockEvent))
			'''mc.postToChat("Event Monitor reads: " + str(blockEvent.pos.x))
			mc.postToChat("Event Monitor reads: " + str(blockEvent.pos.y))
			mc.postToChat("Event Monitor reads: " + str(blockEvent.pos.z))
			mc.postToChat("Event Monitor reads: " + str(blockEvent.face))
			mc.postToChat("Event Monitor reads: " + str(blockEvent.type))
			mc.postToChat("Event Monitor reads: " + str(blockEvent.entityId))
			'''
			if blockEvent.pos.x == 45 and blockEvent.pos.z == 18:
				mc.postToChat("You hit the sign! sending a 3 over RF-Craft")
				#ser.write("3," + node)


