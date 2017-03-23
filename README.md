
# MoT (Minecraft Of Things)

![CloudMaker](https://github.com/cheapjack/cheapjack.github.io/blob/master/tumblr_files/Cloudmaker.png)


### Background

[The Minecraft Of Things](http://minecraftofthings.tumblr.com) sprang from research with [FACT](http://fact.co.uk/), [Dr Mark Wright](https://twitter.com/dr_mark_wright), [Adrian McEwen](http://www.mcqn.com/) and Paul Harter of [PrintCraft](http://www.printcraft.org/) funded by [IT as a Utility (ITaaU) Network](http://www.itutility.ac.uk) for the [CloudMaker](https://github.com/cheapjack/CloudMaker) project

### Resources

This is a repository of code prototypes and workshop examples of using mcpi with sensors and buttons.  

<img="https://cloud.githubusercontent.com/assets/128456/24247663/823bc272-0fc4-11e7-913a-0aad5788bdf3.png" width="400">

[RF-Craft](https://github.com/cheapjack/RF-Craft) is an open-source raspberry Pi HAT to send simple serial messages wirelessly on the 868Mhz radio band from an onboard button, analog inputs and a digital pin for temperature sensing. 

It's also designed to act as a standalone radio arduino board.

This uses Martin O'Hanlon's [mcpi API](https://github.com/martinohanlon/mcpi) the Minecraft: Pi Edition API Python Library and his and Zhuowei's [Canary Raspberry Juice](https://github.com/martinohanlon/CanaryRaspberryJuice) plugin for use with FACT's CloudMaker Minecraft Server

You can view the [Minecraft CloudMaker Server with this link](http://89.34.96.47:8125)

### Requirements

To use the `mcpi` API, you will need to install `Python v2.7` from [here](https://www.python.org/about/gettingstarted/) and then you can follow the tutorials at [Raspberry Pi here](https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/worksheet/)

I'd recommend looking at the [Hitchhiker's Guide To Python](http://docs.python-guide.org/en/latest/) for extensive tips on installing `Python 2.7` (much of what we use is not ready for `Python 3`) and although you can run from the command line I'd recommend using the Idle IDE. I'd also consider using Virtual Environments  [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

You then need to clone this repo into your home directory and edit the `server.py` file depending on whether you are connecting to CloudMaker on a pi or not.

Change the flag `is_pi = True` if you are using a Pi to interact with the server
Change the flag `is_pi = False` if you are using PC/MAC/Linux to interact with the server

You also need to edit your minecraft user profile to play `version 1.7.9` to make sure all our plugins work nicely.

### Quickstart

There are many many ways of interacting with real world sensors and buttons in Minecraft. There is no 'right' way; but we hope to show a simple sensible way but with some added features. 

Its designed to work on board a Raspberry Pi or connected over serial to another computer or on its own as an arduino UNO board. 

#### Hello World!

You generally talk to the server with the API like this:
```
    from mcpi import minecraft
    import server

    mc = minecraft.Minecraft.create(server.address)
```
If you open `Idle` and run the `HelloWorld.py` module you can see what happens on the CloudMaker server. 

Alternatively run from the command line in the mcpi directory in the enclosing directory you cloned `MoT` into (**ie** `~/MoT/mcpi`) using 
```
    pi$ python HelloWorld.py
```
Other unfinished more detailed setup guides and resources are on the [Minecraft of Things](http://minecraftofthings.tumblr.com/resources) but updating, simplifying and migrating to the Wiki in due course

You can also play with all of the code in Martin O'Hanlon and David Whale's excellent book **Adventures in Minecraft** which you can get from [the Wiley publishers' website](http://eu.wiley.com/WileyCDA/Section/id-823690.html)

To make it work with our setup remember to just add the server module

    import server
    
And add `(server.address)` to the mc object to make sure you send your API calls to the CloudMaker server    

Of course you also need to be playing minecraft `v1.7.9` to see what's happening if you decide to use the FACT CloudMaker Server

### RF-Craft

### Why Play with Minecraft like this?

After much research we felt that Martin O'Hanlon's work with mcpi was the most user friendly way to interct with Minecraft and around his work was a strong supportive community and the most creative ideas from a twitter bot to environmental sensors on the AstroPi onboard the International Space Station. 

There is also a book you can buy to get you started with mcpi written by Martin and David Whale.

Part of our brief was to use existing open source resources and not just build a propriety platform from scratch: we've tried to build on the existing resources out there and give something useful to the community back.

We also wanted to form a model for how we thing people should be approaching the Internet Of Things: open source, following popular standards and simple. 

We also wanted it to be able to work in all kind of situations knowing that the real world of teaching the internet of things meant you could not always rely on perfect internet conditions!

The resources here are designed around a Raspberry Pi Hat: a custom PCB that is effectively an independent arduino board with an RF module onboard allowing encrypted wireless communication independent of WiFi; something that could work in a castle in the Lake District or a school with restrictive network setup on a local minecraft server running on a Pi.

It also lets you send messages to the FACT Minecraft server which is an open public PC server to experiment in and explore. The Pi would struggle to host more than 2 users. Its also useable as an arduino board for wireless radio communication and can act as a transmitter or receiver and it is meant to be an entry point for building your own Internet of Things.

We also were aware of e-waste and an ever saturated market for arduino boards for young makers so aswell as this shiny plug and play arduino HAT there are designs for breadboard versions of the HAT; a ebreadboard arduino water temperature kits


### Shrimps

We've used mcpi with the *brilliant* **Shrimped Arduino kits** from [Shrimping.it](http://shrimping.it/blog/) at its core and used prototype methods for visualising raw temperature and turbdiity data on onboard LED flashers, in Processing and in Minecraft. We used this method for the [ShrimpCraft](https://github.com/cheapjack/ShrimpCraft) workshops with Octopus Collective and Amanda Steggell.

### Server Features

 * Printbot
 * ScriptCraft
 * WorldEdit
 * Essentials

### Minecraft of Things Wiki

[Read the Wiki here](https://github.com/cheapjack/MoT/wiki)

**Note** These files are in progress, particularly the .pdf instructions that need checking and revising please see [issues](https://github.com/cheapjack/ShrimpCraft/issues)
