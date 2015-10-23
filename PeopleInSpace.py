#!/usr/bin/python# Import modules for mcpi etc

# File to listen for a sword hit action at a specific block and find the ISS current location

#from mciot import ServerConnection

import urllib2
import json
from time import sleep
#from mcpi import minecraft
#import server

#mc = minecraft.Mineicraft.create(server.address)
#mc.postToChat("Server started watching block events")


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
	sleep(0.5)
	print getPeople(NAME)
	sleep(0.5)
        #print "SPACECRAFT = " , SPACECRAFT
        sleep(0.5)
 #       mc.postToChat("NUMBER OF PEOPLE IN SPACE: " + int(NUMBER))
 #       mc.postToChat("NAMES: " + str(getPeople(NAME))
        sleep(5)

peopleInSpace()

