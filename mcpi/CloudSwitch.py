#!/usr/bin/python

#from mciot import ServerConnection
from mcpi import minecraft
from mcpi import minecraftstuff
import buildHouse2
from pyfirmata import Arduino, util, INPUT
from time import sleep
import server

mc = minecraft.Minecraft.create(server.address)
mcdrawing = minecraftstuff.MinecraftDrawing(mc)


# Use the command /getpos to find out where you are then use those
# x, y, z coordinates to build things
# translate mc coords for mcpi ones
# add this to x
mcx = 177
# - this from y
mcy = 64
# - this from z
mcz = 135

# Set up a light_status variable
light_status = False

# Set up the connection to the Arduino/Shrimp
# navigate to /dev and ls to see what usb port your arduino is on
shrimp = Arduino("/dev/tty.SLAB_USBtoUART")

# If we get here things should be ready to go
print("Everything is connected up.")
mc.postToChat("Hello World! Connected to CloudMaker!")

# Switch Crafting! #
# Start an iterator so we can read in the switch press easily
it = util.Iterator(shrimp)
it.start()
print("Iterator starting up.")

# Set up the switch pin to read things in (rather than write things out)
button_pin = shrimp.digital[8]
button_pin.mode = INPUT
button_pin.enable_reporting()
# make a pin to light up the LED on D13
light_pin = shrimp.digital[13]

#Changing your players position
def jump(blocks):
        mc.postToChat("Jump your player " + str(blocks) + "UP!")
        sleep(1)
        mc.player.setPos(playerPos.x, playerPos.y + blocks, playerPos.z)
        # - wait for you to fall!
        sleep(5)

def beacon(x, y, z):
        #playerPos = mc.player.getPos()
        mc.postToChat("Made A beacon near " + str(x) + " " + str(y) + " " + str(z))
        sleep(1)
        mc.setBlocks((x + mcx)+1, (y - mcy)-1, (z - mcz)+1, (x + mcx)+3, (y - mcy), (z - mcz)+3, 57)
        mc.setBlock((x + mcx)+2, (y - mcy)+1, (z-mcz)+2, 138)
        sleep(1)


def beacon_near_player():
        playerPos = mc.player.getPos()
        playerPos = minecraft.Vec3(int(playerPos.x), int(playerPos.y), int(playerPos.z))
        mc.postToChat("Made A beacon near " + str(playerPos))
        sleep(1)
        mc.setBlocks(playerPos.x+1, playerPos.y-1, playerPos.z+1, playerPos.x+3, playerPos.y, playerPos.z+3, 57)
        mc.setBlock(playerPos.x+2, playerPos.y+1, playerPos.z+2, 138)
        sleep(1)

def beacon_near_player_off():
        playerPos = mc.player.getPos()
        playerPos = minecraft.Vec3(int(playerPos.x), int(playerPos.y), int(playerPos.z))
        mc.postToChat("Removing beacon " + str(playerPos))
        sleep(1)
        mc.setBlocks(playerPos.x+1, playerPos.y-1, playerPos.z+1, playerPos.x+3, playerPos.y, playerPos.z+3, 0)
        mc.setBlock(playerPos.x+2, playerPos.y+1, playerPos.z+2, 0)
        sleep(1)

def makeCircle(x, y, z, radius, blocktype):
        mcdrawing.drawCircle(x + mcx, y - mcy, z - mcz, radius, blocktype)


def makeBlock(blocktype):
        playerPos = mc.player.getPos()
        playerPos = minecraft.Vec3(int(playerPos.x), int(playerPos.y), int(playerPos.z))
        mc.setBlocks(playerPos.x + 2, playerPos.y + 2, playerPos.z + 2, blocktype)

def makeTreasure(x, y, z, blocktype):
        mc.setBlocks(x + mcx, (y - mcy)-2, z - mcz, (x + mcx)+ 4, (y - mcy)- 4, (z - mcz) + 4, blocktype)

# takes a minecraft coord and translates it for mcpi
def makeSphere(x, y, z, radius, blocktype):
        #playerPos = mc.player.getPos()
        #playerPos = minecraft.Vec3(int(playerPos.x), int(playerPos.y), int(playerPos.z))
        #mcdrawing.drawSphere(playerPos.x - (radius*2), playerPos.y - (radius*2), playerPos.z - (radius*2), radius, blocktype)
        mcdrawing.drawSphere(x + mcx, y - mcy, z - mcz, radius, blocktype)

# A function to check if the button has been pressed, or the switch pulled and if it has
# to send a command to the Minecraft server with the mcpi API
def check_for_switch():
        global light_status
        if button_pin.read():
                print("Light switch pulled")
                if not light_status:
                        # The switch is on, but the light isn't
                        light_pin.write(1)
                        # Say something to the server
                        mc.postToChat("Switch Pulled!")
                        beacon_near_player()
                        # uncomment the different functions below
                        # and change the values in brackets, x,y and z to coordinates you want

                        #Makes a beacon at a specific location
                        #beacon(x,y,z)

                        #Jumps a random player in the air!
                        #jump(blocks)

                        #Makes Buried Treasure
                        #makeTreasure(x, y, z, 57)

                        #make a Circle
                        #makeCircle(x, y, z, radius, blocktype)

                        #Make a block
                        #makeBlock(blocktype)


                        #Make a sphere
                        #makeSphere(x, y, z, radius, blocktype)

                        #Make a house
                        #house()

                        sleep(0.5)
                        light_status = True

        else:
                if light_status:
                        # The switch is off, but the light is on
                        # Do something
                        # beacon_near_player_off()
                        # beacon_near_player()
                        light_pin.write(0)
                        #mc_server.run_command("time set 14000")
                        #mc_server.run_command("say removing")
                        light_status = False


# Now just check regularly to see if they're online or not
while True:
        #makes everything under your feet gold
        '''
        pos = mc.player.getTilePos()
        blockBelow = mc.getBlock(pos.x,pos.y-1,pos.z)
        if blockBelow != 0 and blockBelow != 9:
                mc.setBlock(pos.x, pos.y-1, pos.z, 41)
        sleep(0.1)
        '''
        #check if the switch has been pulled or switched
        check_for_switch()
        sleep(0.1)


