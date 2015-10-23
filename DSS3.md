# Do Something Saturdays

## Workshop 4 The Minecraft Of Things Part 2

![Things](http://36.media.tumblr.com/ab3d03e2a3ee6432030c4bbe6e943658/tumblr_n3vrhu2RYX1tytl75o1_500.jpg)

**Lesions in the Landscape** by *Shona Illingworth* refers to the islands of **St Kilda** as a a landscape haunted by traces of cultural memory; the community of people who lived there altho
ugh small inhabited the islands for over 2000 years. She also hints at its more contemporary id
entity as a strategic point in the infrastructure of mapping and tracking technology often for semi-military applications. In her video installation she seems to link this to the forcible relocation of inhabitants in the 1930s; hinting at contemporary technology's control and tracking of cultural *externalised* memory. 

Today we are going to learn about the consequences of this kind of infrastructure and our digital identities by thinking about the [Internet of Things](https://en.wikipedia.org/wiki/Internet_of_Things).

Soon almost everything will be connected to the internet, you can turn your heating off as soon as your phone leaves your street or alert people that you need help or make sure your gran can keep in touch with her family and friends.

The basic principles of the internet of things can be learned in Minecraft: you as a player are a `client` on a minecraft `server` that sends you information; where are you, what you are looking at, and then your client (the game on your computer) interprets that data to let you play the game.

## Using the `mcpi` API with `CloudSwitch.py`

We will be doing this in more detail soon but we can make things happen in minecraft with the `mcpi` **API**

We are going to do something a little scary, go under the bonnet of our computer using the **command line** the programming language `python` and a text editing tool called `vim`
 
 * Open a terminal window; it's the black screen logo in the mac dock
 * Type `cd ~/MoT-master` this **c**hanges **d**irectory to the `MoT-master` folder
 * Type `ls` and you can **l**i**s**t the contents 
 * Type `vim CloudSwitch.py` and use the cursor keys to move around and edit; see the vim instructions below but if you look through the code you can change the `beacon()` function to build beacons in the game based on minecraft coordinates. By default the code will build one near your player
 * You can 'hack' this code and delete the `#` character in different functions to make certain funtions run and stop others from running 
 * Try comment **ie** add a `#` to the `beacon_near_player.py` file and uncomment **ie** remove a `#` from the line ` #jump(blocks)` and change it to `jump(20)`  
 * When you've finished type `:w` to save it and then run the changed code by typing `python CloudSwitch.py`
 * When you've hacked the `beacon` function you can make your switch build or unbuild beacons in the game. You save any changes by typing `:wq` and press return
 * You run your python programme by typing in the terminal `python CloudSwitch.py` and press return

####Vim

[Vim](http://vim.rtorr.com/) (a version of Vi) is a text editor that lives pretty much on every server on the internet

Basically you move with the cursor keys and if you want to type something press `i` and you can type and delete as normal. When you're finished hit escape `esc` and if you want to `write` your changes type `:wq`  

 * `i` - insert text
 * `cursor keys` - move in the text
 * `esc` - stop inserting text
 * `:w` - write your changes
 * `:wq` - write your changes and quit vim

![stkilda](https://cloud.githubusercontent.com/assets/128456/10695131/fe4a3dde-7999-11e5-8d1d-287943fd217e.png)

## Mapping St Kilda

Now for the rest of the workshop we are going to use information and satellite imagery from Google Maps to generate our own thing on the internet; A real map of St Kilda kindly made by [Gemma May Latham](https://twitter.com/gemmamaylatham) using [WorldPainter](http://worldpainter.net/)

We are going to work together using the power of the crowd (by that I mean us!) to make buildings and pathways ontop of the map Gemma has put together for us.

Think about the features that [Ordnance survey used](http://www.ordnancesurvey.co.uk/innovate/developers/minecraft-map-britain.html) and how we could make features that give people information:
 
 * Locations of radar stations 
 * Paths and Roads
 * Buildings
 * Mobs: What kind of people could we represent as mobs? Scientists? Villagers from the past
 * Animals
 * Signs and giant signs

