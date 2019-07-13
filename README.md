# PyTibiaBot
Simple bot made for tibia, with pyautogui, opencv and others.

The archive simulator.py is a simple cavebot with target, walk and looter in swamp trolls
Have another 2 archives, one is for misc tools and healler and another is only for test
this is my contribuition for Tibia.
Thanks!


## Configuration

- Controls: Classic Controls + Loot:Left
- Interface: Colourise Loot Value: None (this is for pyautogui find correct image inside bps)
- HUD: Show Status Bars (this is way for pyautogui find correct location of life/mana when change position of life widget)
- Battle List: I set battle list to get near creature first to attack.
- Minimap: I use the first waypoint mark for bot find my waypoints.

How to use this?  
Install python 3.7 in your computer and set python in pc path

What is the logic?  
Pyautogui can find image on screen faster, but he only find image with non-transparecy background, you need capture Names of creatures,
crop items, compare pixels (for healler) to make a good Bot without read memory or send packets to client.


