
import mcpi.minecraft as minecraft
import server

mc = minecraft.Minecraft.create(server.address)

mc.postToChat("Hello world! Connecting to CloudMaker!")
