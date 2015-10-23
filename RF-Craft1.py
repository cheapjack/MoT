#!/usr/bin/python

# Moteino Receiver for RF-Crafting and button-craft

from mcpi import minecraft
from mcpi import  minecraftstuff
import server
import serial
from time import sleep

mc = minecraft.Minecraft.create(server.address)

mcdrawing = minecraftstuff.MinecraftDrawing(mc)


# use the default mac serial port, '/dev/tty.SLAB_USBtoUART' this will change platform to platform
ser = serial.Serial('/dev/tty.SLAB_USBtoUART', 9600)
mc.postToChat("Hello CloudMaker this is Serial " + str(ser.readline()))
button1_received = "1,1\r\n"
button2_received = "1,2\r\n"
# The Button sends the serial message (action , node)
# action: "1", "Button Pressed"
#	"2", "Error"
#	"3", "OK"

# translate mc coords for mcpi ones
# add this to x
mcx = 177
# - this from y
mcy = 64
# - this from z
mcz = 135

def makeCircle(x, y, z, blocktype):
	mcdrawing.drawCircle(x, y, z, blocktype)


def makeBlock(blocktype):
	playerPos = mc.player.getPos()
	playerPos = minecraft.Vec3(int(playerPos.x), int(playerPos.y), int(playerPos.z))
	mc.setBlock(playerPos.x + 2, playerPos.y + 2, playerPos.z + 2, blocktype)

def makeTreasure(x, y, z, blocktype):
	mc.setBlock(x + mcx, y - mcy, z - mcz, blocktype)

# takes a minecraft coord and translates it for mcpi
def makeSphere(x, y, z, radius, blocktype):
	#playerPos = mc.player.getPos()
	#playerPos = minecraft.Vec3(int(playerPos.x), int(playerPos.y), int(playerPos.z))	
	#mcdrawing.drawSphere(playerPos.x - (radius*2), playerPos.y - (radius*2), playerPos.z - (radius*2), radius, blocktype)
	mcdrawing.drawSphere(x + mcx, y - mcy, z - mcz, radius, blocktype)


while True:
	serialcommand = str(ser.readline())
	if serialcommand == button1_received:
		print "We've Got Mail from Button 1!"
		mc.postToChat("We've Got Mail from Button 1! It says: " + serialcommand)
		mc.postToChat("Building...")
		#makeBlock(20)
		#makeTreasure(-197, 152, 81, 89)
		makeTreasure(2765, -50, 4078, 20)
		makeCircle(-199, 109, 108, 6, 89)
	else:
		print "Nothing"
		mc.postToChat("Nothing")
	sleep(0.5)
