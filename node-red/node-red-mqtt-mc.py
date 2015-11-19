#!/usr/bin/python

from mcpi import minecraft
import server
import paho.mqtt.client as paho

def fwd(pos, step):
	mc.player.setTilePos(pos.x+step, mc.getHeight(pos.x+step, pos.z), pos.z)
#pointless avoidance of switch statement using array

options = {"/fwd":fwd}

def on_message(mosq, obj, msg):
	print(msg.topic + " " + str(msg.qos) + str(msg.payload))
	pos = mc.player.getTilePos()
	options [msg.topic](pos, int(msg.payload))

mc = minecraft.Minecraft.create(server.address)
mc.postToChat("Hello world! Connecting to CloudMaker with MQTT & node-red!")

mqttc = paho.Client()
mqttc.on_message = on_message
mqttc.connect("127.0.0.1", 1883, 60)

mqttc.subscribe([("/fwd", 0)])
mqttc.loop_forever()



