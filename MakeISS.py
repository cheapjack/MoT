#!/usr/bin/python
# Import modules for mcpi etc

# File to listen for a sword hit action at a specific block and find the ISS current location

#from mciot import ServerConnection

from time import sleep
from mcpi import minecraft
import server

mc = minecraft.Minecraft.create(server.address)

def makeISS():
	playerPosNow = mc.player.getPos()
	mc.postToChat(str(playerPosNow))
	# Solar panel 1
	mc.setBlocks(playerPosNow.x, playerPosNow.y + 1, playerPosNow.z, playerPosNow.x + 26, playerPosNow.y + 1, playerPosNow.z + 2, 89)
	# Main cabin block
	mc.setBlocks(playerPosNow.x + 9, playerPosNow.y, playerPosNow.z + 4, playerPosNow.x + 15, playerPosNow.y + 3, playerPosNow.z + 6, 42)
	mc.setBlocks(playerPosNow.x + 9, playerPosNow.y + 1, playerPosNow.z + 5, playerPosNow.x + 15, playerPosNow.y + 2, playerPosNow.z + 5, 0)
	# observation ports
	mc.setBlocks(playerPosNow.x + 8, playerPosNow.y + 1, playerPosNow.z + 5, playerPosNow.x + 8, playerPosNow.y + 2, playerPosNow.z + 5, 20)
	mc.setBlocks(playerPosNow.x + 16, playerPosNow.y + 1, playerPosNow.z + 5, playerPosNow.x + 8, playerPosNow.y + 2, playerPosNow.z + 5, 20)
	# Solar panel 2
	mc.setBlocks(playerPosNow.x, playerPosNow.y + 1, playerPosNow.z +8, playerPosNow.x + 26, playerPosNow.y + 1, playerPosNow.z + 10, 89)
	return (playerPosNow)
	sleep(1)

makeISS()
print makeISS()
sleep(0.5)

