##Using `node-red` to issue `mcpi` commands


Follows the basic `node-red` -> `mosquitto` -> `mcpi` flow described by 
Boris Adryan in his [blogpost](http://logic.sysbiol.cam.ac.uk/?p=1499)

Also inspired by this awesome [node-red minecraft hack](https://utbrudd.bouvet.no/2014/03/10/an-internet-of-things-demo-using-raspberry-pi-arduino-minecraft-and-mqtt/)

Assumes some working knowledge of `python`, the command line, `mcpi` and `node-red`

<img src="https://utbrudd.bouvet.no/wp-content/uploads/2014/03/Skjermbilde-2014-03-08-kl.-20.34.01-1024x657.png" width="400">

###How-to

 * Install Minecraft and the Python API on the Raspberry Pi as described on [Craig’s blog.](https://arghbox.wordpress.com/2013/06/16/minecraft-pi-api-setting-up/)
 * Install Node-RED as described on the [Hardware Hacks blog](http://c-mobberley.com/wordpress/2013/10/03/raspberry-pi-hosting-node-red-take-the-crap-out-of-developing-automation-the-internet-of-things-iot/).
 * Install mosquitto and mosquitto clients (i.e. mosquitto_pub) via `sudo apt-get install mosquitto mosquitto-clients`
 * Install Eclipse Paho MQTT libraries for Python via `sudo pip install paho-mqtt` 
 * Test if Minecraft, Node-RED, mosquitto et al. work.

 * Assuming you have Node-RED running as a service (here’s a [hint on how to have this at startup](http://c-mobberley.com/wordpress/2014/01/12/raspberry-pi-node-red-startstoprestart-script/)), you also want to start up the mosquitto broker by issuing `mosquitto -p 1883` (or a port of your choosing).

 * Then with mosquitto running, run the python script `python node-red-mqtt-mc.py` and fire off the input node in the `node-red` flow below and `mcpi` will move you forward 5 blocks in the CloudMaker world

```
[{"id":"4fd1c3ef.37dd1c","type":"mqtt-broker","broker":"localhost","port":"1883","clientid":""},{"id":"5355392e.7b463","type":"mqtt out","name":"Mosquitto","topic":"","qos":"","retain":"","broker":"4fd1c3ef.37dd1c","x":391,"y":260,"z":"e7f395ce.584028","wires":[]},{"id":"359574e1.bf1fdc","type":"debug","name":"","active":true,"console":"false","complete":"true","x":385,"y":162,"z":"e7f395ce.584028","wires":[]}]
```

