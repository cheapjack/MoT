# MoT (Minecraft Of Things)

![CloudMaker](https://github.com/cheapjack/cheapjack.github.io/blob/master/tumblr_files/Cloudmaker.png)

###Background

[The Minecraft Of Things](http://minecraftofthings.tumblr.com) sprang from research with [FACT](http://fact.co.uk/), [Dr Mark Wright](https://twitter.com/dr_mark_wright), [Adrian McEwen](http://www.mcqn.com/) and Paul Harter of [PrintCraft](http://www.printcraft.org/) funded by IT as a Utility (ITaaU) Network for the [CloudMaker](http://www.fact.co.uk/projects/cloudmaker-making-minecraft-real.aspx) project

###Resources

This uses Martin O'Hanlon's [mcpi](https://github.com/martinohanlon/mcpi) the Minecraft: Pi Edition API Python Library and his and Zhuowei's [Canary Raspberry Juice](https://github.com/martinohanlon/CanaryRaspberryJuice) plugin for use with FACT's CloudMaker Minecraft Server


You can view the [Minecraft CloudMaker Server with this link](http://mc.fact.co.uk:8123/)

###Requirements

You need to clone this repo into your home directory and edit the server.py file depending on whether you are connecting to CloudMaker on a pi or not.

You also need to edit your minecraft user profile to play `version 1.7.9` to make sure all our plugins work nicely. Updates are on the way.

###Quickstart

You will need to install Python and then you can follow the tutorials at [Raspberry Pi here](https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/worksheet/) but just change the way you setup the server to

    import mcpi.minecraft as minecraft
    import server

    mc = minecraft.Minecraft.create(server.address)


###Shrimps

It also uses the *brilliant* **Shrimped Arduino kits** from [Shrimping.it](http://shrimping.it/blog/) at its core and also features prototype methods for visualising data on onboard LED flashers, in Processing and in Minecraft 


**Note** These files are in progress, particularly the .pdf instructions that need checking and revising please see [issues](https://github.com/cheapjack/ShrimpCraft/issues)
