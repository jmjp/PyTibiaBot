import os
import time
from threading import Thread
from tkinter import *
from pynput import keyboard
from time import sleep
from core import winapi
from core import functions as core


bot = True
running = False
status_eatfood = False
status_treiner = False
status_walking = False
status_alerts = False
status_healer = False
status_runemaker = False
status_fishing = False
spell = ""
spell_time = 0

# CREATE KEYS
COMBINATION = [
    {keyboard.Key.ctrl, keyboard.Key.end},
    {keyboard.Key.shift, keyboard.Key.end}
    ]

current = set()

def execute():
    print("executed2")
    os._exit(1)

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATION]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATION):
            execute()

def on_release(key):
    pass

def listen():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

threads = list()
lt = Thread(target=listen)
threads.append(lt)
lt.start()


def focus():
    # FOCUS GAME
    w = winapi.WinApi()
    w.find_window_wildcard(".*Tibia.*")
    w.set_foreground()

def start():
    print("You've selected (0) START.")
    global running
    running = True
    print("Bot running.")

# MENU
def menu():

    print("SHIFT + END WILL CLOSE THE BOT")


    choice = input("Choice: ")

    if choice == "1":
        global status_fishing
        if(status_fishing == True):
            status_fishing = False
            print("Fishing Disable")
        else:
            status_fishing = True
            print("Fishing Enable")
        menu()
    elif choice == "2":
        global status_walking
        if (status_walking == True):
            status_walking = False
            print("Walking Disable")
        else:
            status_walking = True
            print("Walking Enable")
        menu()
    elif choice == "3":
        global status_healer
        if (status_healer == True):
            status_healer = False
            print("Healer Disable")
        else:
            status_healer = True
            print("Healer Enable")
        menu()
    elif choice == "4":
        global status_treiner
        if (status_treiner == True):
            status_treiner = False
            print("Mana Treiner Disable")
        else:
            status_treiner = True
            print("Mana Treiner Enable")
        menu()
    elif choice == "5":
        global status_eatfood
        if (status_eatfood == True):
            status_eatfood = False
            print("EatFood Disable")
        else:
            status_eatfood = True
            print("EatFood Enable")
        menu()
    elif choice == "6":
        sleep(3)
        start()
    else:
        print("Wrong choice!")
        input("Press any key to exit...")


# DEFAULT ROUTINE #
# IMAGES
# Move to images folder
os.chdir("images")

# Create an image list
image_list = ["health", "mana", "battle_list", "food","fishing"]
# Loop image_list to check if images exists, so we avoid calling null files
for i in image_list:
    if not os.path.isfile(i + ".png"):
        print("Unable to find image file: " + i + ".png")
        wait = input("Press any key to quit.")
        sys.exit(0)



while bot:
    if running:
        if(status_fishing):
            core.game.fishing(core.game)
        if(status_healer):
            core.game.heal(core.game,50,"exura infir",1)
        if (status_treiner):
            core.game.mp(core.game, 10, "exura infir", 1)
        if(status_eatfood):
            core.game.eat_food(core.game)
        if(status_walking):
            core.game.walk()
    else:
        menu()
    sleep(1)