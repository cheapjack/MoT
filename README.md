# MoT (Minecraft Of Things)

![CloudMaker](https://github.com/cheapjack/cheapjack.github.io/blob/master/tumblr_files/Cloudmaker.png)

###Background

[The Minecraft Of Things](http://minecraftofthings.tumblr.com) sprang from research with [FACT](http://fact.co.uk/), [Dr Mark Wright](https://twitter.com/dr_mark_wright), [Adrian McEwen](http://www.mcqn.com/) and Paul Harter of [PrintCraft](http://www.printcraft.org/) funded by [IT as a Utility (ITaaU) Network](http://www.itutility.ac.uk) for the [CloudMaker](http://www.fact.co.uk/projects/cloudmaker-making-minecraft-real.aspx) project

###Resources

This uses Martin O'Hanlon's [mcpi API](https://github.com/martinohanlon/mcpi) the Minecraft: Pi Edition API Python Library and his and Zhuowei's [Canary Raspberry Juice](https://github.com/martinohanlon/CanaryRaspberryJuice) plugin for use with FACT's CloudMaker Minecraft Server


You can view the [Minecraft CloudMaker Server with this link](http://mc.fact.co.uk:8124/)

###Requirements

First you will need to install `Python v2.7` from [here](https://www.python.org/about/gettingstarted/) and then you can follow the tutorials at [Raspberry Pi here](https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/worksheet/)

I'd recommend looking at the [Hitchhiker's Guide To Python](http://docs.python-guide.org/en/latest/) for extensive tips on installing `Python 2.7` (much of what we use is not ready for `Python 3`) and although you can run from the command line I'd recommend using the Idle IDE. I'd also consider using Virtual Environments  [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

You then need to clone this repo into your home directory and edit the `server.py` file depending on whether you are connecting to CloudMaker on a pi or not.

Change the flag `is_pi = True` if you are using a Pi to interact with the server
Change the flag `is_pi = False` if you are using PC/MAC/Linux to interact with the server

You also need to edit your minecraft user profile to play `version 1.7.9` to make sure all our plugins work nicely. Updates on the way.

###Quickstart

####Hello World!

You generally talk to the server with the API like this:

    from mcpi import minecraft
    import server

    mc = minecraft.Minecraft.create(server.address)

If you open Idle and run the HelloWorld.py module you can see what happens on the CloudMaker server. Alternatively run from the command line in the mcpi directory in the enclosing directory you cloned `MoT` into (**ie** `~/MoT/mcpi`) using 

    $ python HelloWorld.py

Other unfinished more detailed setup guides and resources are on the [Minecraft of Things](http://minecraftofthings.tumblr.com/resources) but updating, simplifying and migrating to the Wiki in due course

You can also play with all of the code in Martin O'Hanlon and David Whale's excellent book **Adventures in Minecraft** which you can get from [the Wiley publishers' website](http://eu.wiley.com/WileyCDA/Section/id-823690.html)

To make it work with our setup remember to just add the server module

    import server
    
And add `(server.address)` to the mc object to make sure you send your API calls to the CloudMaker server    

Of course you also need to be playing minecraft `v1.7.9` to see what's happening!

###Shrimps

We've used mcpi with the *brilliant* **Shrimped Arduino kits** from [Shrimping.it](http://shrimping.it/blog/) at its core and used prototype methods for visualising raw temperature and turbdiity data on onboard LED flashers, in Processing and in Minecraft. We used this method for the [ShrimpCraft](https://github.com/cheapjack/ShrimpCraft) workshops with Octopus Collective and Amanda Steggell.

###Server Features

 * Printbot
 * ScriptCraft
 * WorldEdit
 * Essentials

###Minecraft of Things Wiki

[Read the Wiki here](https://github.com/cheapjack/MoT/wiki)

**Note** These files are in progress, particularly the .pdf instructions that need checking and revising please see [issues](https://github.com/cheapjack/ShrimpCraft/issues)
