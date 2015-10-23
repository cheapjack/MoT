#!/usr/bin/python
# Import modules for mcpi etc

# File to listen for a sword hit action at a specific block and find the ISS current location

#from mciot import ServerConnection

import urllib2
import json
from time import sleep
from mcpi import minecraft
import server

mc = minecraft.Minecraft.create(server.address)
mc.postToChat("Server started watching block events")

def peopleInSpace():
        req = urllib2.Request("http://api.open-notify.org/astros.json")
        response = urllib2.urlopen(req)
        obj = json.loads(response.read())
        NUMBER = obj['number']
        #NAME = obj['people']['name']
        NAME = obj['people']
        #SPACECRAFT = [obj['people']['craft']]
	def getPeople(list):
		results = []
		index = 0
                for items in list:
			for n in items:
                        	if index < len(list):
					results.append(list[index]['name'])
					index = index + 1
				else:			
					return results
	print "NUMBER OF PEOPLE IN SPACE: " , int(NUMBER)
	mc.postToChat("My God, It's Full of Stars..." + int(NUMBER))
	sleep(0.5)
	mc.postToChat("NUMBER OF PEOPLE IN SPACE: " + int(NUMBER))
	sleep(0.5)
	print getPeople(NAME)
	mc.postToChat("PEOPLE: " + str(getPeople(NAME)))
        sleep(2)

def FindISS():
	req = urllib2.Request("http://api.open-notify.org/iss-now.json")
	response = urllib2.urlopen(req)
	obj = json.loads(response.read())
	TIMESTAMP = obj['timestamp']
	ISSLAT = obj['iss_position']['latitude']
	ISSLONG = obj['iss_position']['longitude']
	print "TIMESTAMP: " , TIMESTAMP 
	sleep(0.5)
	print "ISS POSITION: LATITUDE = " , ISSLAT
	print "ISS POSITION: LONGITUDE = " , ISSLONG
	sleep(0.5)
	mc.postToChat("LATITUDE: " + str(ISSLAT // 1))
	mc.postToChat("LONGITUDE: " + str(ISSLONG // 1))
	#return ISSLAT, ISSLONG
	sleep(5)

def GoISS():
	req = urllib2.Request("http://api.open-notify.org/iss-now.json")
	response = urllib2.urlopen(req)
	obj = json.loads(response.read())
	TIMESTAMP = obj['timestamp']
	ISSLAT = obj['iss_position']['latitude']
	ISSLONG = obj['iss_position']['longitude']
	print "TIMESTAMP: " , TIMESTAMP 
	sleep(0.5)
	print "ISS POSITION: LATITUDE = " , ISSLAT
	print "ISS POSITION: LONGITUDE = " , ISSLONG
	mc.postToChat("LATITUDE: " + str(ISSLAT // 1))
	mc.postToChat("LONGITUDE: " + str(ISSLONG // 1))
	mc.player.setPos(blockEvent.entityId, ISSLAT, 100, ISSLONG)
	sleep(0.5)
	#return ISSLAT, ISSLONG
	#sleep(5)

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


def listen_for_block_hits():
	global blockEvents
	global blockEvent
	blockEvents = mc.events.pollBlockHits()
	if blockEvents:
		print "polling for a hit" , blockEvents
		for blockEvent in blockEvents:
			print blockEvent
			#print blockEvent.pos.x
			#print blockEvent.pos.y
			#print blockEvent.pos.z
			#print blockEvent.face
			print blockEvent.type
			#print blockEvent.entityId
			mc.postToChat(str(blockEvent))
			#mc.postToChat("Event at: " + "x: " + str(blockEvent.pos.x) + ", y: "  + str(blockEvent.pos.y) + ", z: " +  str(blockEvent.pos.z))
			if blockEvent.pos.x == 344 and blockEvent.pos.y == 39 and blockEvent.pos.z == -391:
				# find the ISS
				mc.postToChat("Finding ISS...")
				FindISS()
			elif blockEvent.pos.x == 344 and blockEvent.pos.y == 39 and blockEvent.pos.z == -392:
				# Go to the ISS and Make it
				mc.postToChat("Teleporting to ISS...")
				GoISS()
				makeISS()
			elif blockEvent.pos.x == 344 and blockEvent.pos.y == 39 and blockEvent.pos.z == -390:
				# Find Who is in space and print it
				mc.postToChat("Finding People in space...")
				#mc.postToChat("Sorry service down at the moment...try ")
				#mc.postToChat("type http://api.open-notify.org/astros.json in your browser")
				#peopleInSpace()
			else:
				mc.postToChat("Empty")

while True:
	listen_for_block_hits()
	sleep(0.5)

