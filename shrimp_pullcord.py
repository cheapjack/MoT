from mciot import ServerConnection
from pyfirmata import Arduino, util, INPUT
from time import sleep

#MINECRAFT_SERVER = "localhost"
MINECRAFT_SERVER = "mc.fact.co.uk"
MINECRAFT_RCON_PASSWORD = "lR1Nx52MDwdjSy2dVL16AQyJS87XTLkc"

light_status = False

# Set up the connection to the Arduino/Shrimp
shrimp = Arduino("/dev/tty.SLAB_USBtoUART")

# And the connection to the server
mc_server = ServerConnection(MINECRAFT_SERVER, MINECRAFT_RCON_PASSWORD, 25568)

# If we get here things should be ready to go
print("Everything is connected up.")

# Start an iterator so we can read in the button press easily
it = util.Iterator(shrimp)
it.start()
print("Iterator starting up.")

# Set up the button pin to read things in (rather than write things out)
button_pin = shrimp.digital[8]
button_pin.mode = INPUT
button_pin.enable_reporting()

light_pin = shrimp.digital[13]

# A function to check if the button has been pressed, and if it has
# to send the command to the Minecraft server
def check_for_button():
  global light_status
  if button_pin.read():
    print("Light switch pulled")
    if not light_status:
      # The switch is on, but the light isn't
      light_pin.write(1)
      mc_server.run_command("time set 900")
      mc_server.run_commnad("playsound mob.cat.hitt cloudmaker01")
#      mc_server.run_command("loadcode nep8g8z6 0 396 168")
#      mc_server.run_command("say loading")
      sleep(0.5)
      light_status = True
  else:
    if light_status:
      # The switch is off, but the light is on
      light_pin.write(0)
      mc_server.run_command("time set 14000")
#      mc_server.run_command("say removing")
#      mc_server.run_command("removecode nep8g8z6 0 396 168")
      light_status = False

# Now just check regularly to see if they're online or not
while True:
  check_for_button()
  sleep(0.1)

