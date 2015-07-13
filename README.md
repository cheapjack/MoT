# MoT (Minecraft Of Things)

![CloudMaker](https://github.com/cheapjack/cheapjack.github.io/blob/master/tumblr_files/Cloudmaker.png)

###Background

[The Minecraft Of Things](http://minecraftofthings.tumblr.com) sprang from research with [FACT](http://fact.co.uk/), [Dr Mark Wright](https://twitter.com/dr_mark_wright), [Adrian McEwen](http://www.mcqn.com/) and Paul Harter of [PrintCraft](http://www.printcraft.org/) funded by [IT as a Utility (ITaaU) Network](http://www.itutility.ac.uk) for the [CloudMaker](http://www.fact.co.uk/projects/cloudmaker-making-minecraft-real.aspx) project

###Resources

This uses Martin O'Hanlon's [mcpi API](https://github.com/martinohanlon/mcpi) the Minecraft: Pi Edition API Python Library and his and Zhuowei's [Canary Raspberry Juice](https://github.com/martinohanlon/CanaryRaspberryJuice) plugin for use with FACT's CloudMaker Minecraft Server


You can view the [Minecraft CloudMaker Server with this link](http://mc.fact.co.uk:8123/)

###Requirements

You need to clone this repo into your home directory and edit the `server.py` file depending on whether you are connecting to CloudMaker on a pi or not.

Change the flag `is_pi = True` if you are using a Pi to interact with the server
Change the flag `is_pi = False` if you are using PC/MAC/Linux to interact with the server

You also need to edit your minecraft user profile to play `version 1.7.9` to make sure all our plugins work nicely. Updates on the way.

###Quickstart

You will need to install Python and then you can follow the tutorials at [Raspberry Pi here](https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/worksheet/) You setup the server like this:

    from mcpi import minecraft
    import server

    mc = minecraft.Minecraft.create(server.address)

Other unfinished more detailed setup guides and resources are on the [Minecraft of Things](http://minecraftofthings.tumblr.com/resources) but updating, simplifying and migrating to the Wiki in due course

###Shrimps

We've used mcpi with the *brilliant* **Shrimped Arduino kits** from [Shrimping.it](http://shrimping.it/blog/) at its core and used prototype methods for visualising raw temperature and turbdiity data on onboard LED flashers, in Processing and in Minecraft. We used this method for the [ShrimpCraft](https://github.com/cheapjack/ShrimpCraft) workshops with Octopus Collective and Amanda Steggell.

###Server Features

 * Printbot
 * ScriptCraft
 * WorldEdit
 * Essentials

###Minecraft of Things Wiki

To Do


**Note** These files are in progress, particularly the .pdf instructions that need checking and revising please see [issues](https://github.com/cheapjack/ShrimpCraft/issues)
