# ~/usr/bin/python2.7

# from mciot import ServerConnection
from mcpi import minecraft
from pyfirmata import Arduino, util, INPUT
from time import sleep
import server

mc = minecraft.Minecraft.create(server.address)

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


# A function to check if the button has been pressed, or the switch pulled and if it has
# to send a command to the Minecraft server
def check_for_switch():
	global light_status
	if button_pin.read():
		print("Light switch pulled")
		if not light_status:
			# The switch is on, but the light isn't
			light_pin.write(1)
			mc.postToChat("Switch Pulled!")
#      mc_server.run_command("removecode nep8g8z6 0 396 168")
			jump(50)
			#mc_server.run_command("time set 900")
			#mc_server.run_command("loadcode nep8g8z6 0 396 168")
			sleep(0.5)
			light_status = True
	else:
		if light_status:
			# The switch is off, but the light is on
			light_pin.write(0)
			#mc_server.run_command("time set 14000")
			#mc_server.run_command("say removing")
			light_status = False


# Now just check regularly to see if they're online or not
while True:
	playerPos = mc.player.getPos()
	playerPos = minecraft.Vec3(int(playerPos.x), int(playerPos.y), int(playerPos.z))
	check_for_switch()
	sleep(0.1)

