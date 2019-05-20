import os
import time
import pyautogui
from time import sleep
from core import winapi
from tkinter import *


w = winapi.WinApi()
w.find_window_wildcard(".*Tibia.*")

class game:
    global w
    def __init__ (self):
        self._handle = None

    def eat_food(self):
        try:
            foodlist = ['fish']
            for i in foodlist:
                pos = pyautogui.locateOnScreen(i + ".png")
                w.RightClick((pos.left, pos.top))
        except:
            Exception("Food Eater")

    def useOnLocation(self,x, y, name):
        try:
            loc = pyautogui.locateOnScreen(name + '.png')
            w.UseOn((loc.left, loc.top), (x, y))
        except:
            Exception("Use on Location")

    def getLife(self):
        health = pyautogui.locateOnScreen("health.png")
        if (pyautogui.pixelMatchesColor((health.left + 105), (health.top + 7), (219, 79, 79))):
            return 100
        elif (pyautogui.pixelMatchesColor((health.left + 94), (health.top + 7), (219, 79, 79))):
            return 90
        elif (pyautogui.pixelMatchesColor((health.left + 74), (health.top + 7), (219, 79, 79))):
            return 70
        elif (pyautogui.pixelMatchesColor((health.left + 54), (health.top + 7), (219, 79, 79))):
            return 50
        elif (pyautogui.pixelMatchesColor((health.left + 34), (health.top + 7), (219, 79, 79))):
            return 30
        elif (pyautogui.pixelMatchesColor((health.left + 24), (health.top + 7), (219, 79, 79))):
            return 20
        elif (pyautogui.pixelMatchesColor((health.left + 14), (health.top + 7), (219, 79, 79))):
            return 15
        elif (pyautogui.pixelMatchesColor((health.left + 5), (health.top + 7), (219, 79, 79))):
            return 10
        return 0

    def getMana(self):
        health = pyautogui.locateOnScreen("mana.png")
        if (pyautogui.pixelMatchesColor((health.left + 105), (health.top + 5), (67, 64, 192))):
            return 100
        elif (pyautogui.pixelMatchesColor((health.left + 94), (health.top + 5), (67, 64, 192))):
            return 90
        elif (pyautogui.pixelMatchesColor((health.left + 74), (health.top + 5), (67, 64, 192))):
            return 70
        elif (pyautogui.pixelMatchesColor((health.left + 54), (health.top + 5), (67, 64, 192))):
            return 50
        elif (pyautogui.pixelMatchesColor((health.left + 34), (health.top + 7), (219, 79, 79))):
            return 30
        elif (pyautogui.pixelMatchesColor((health.left + 24), (health.top + 7), (219, 79, 79))):
            return 20
        elif (pyautogui.pixelMatchesColor((health.left + 14), (health.top + 7), (219, 79, 79))):
            return 15
        elif (pyautogui.pixelMatchesColor((health.left + 5), (health.top + 28), (219, 79, 79))):
            return 10
        return 0

    def heal(self,percent, spell,time):
        life = self.getLife(self)
        while life < percent:
            w.Write(spell)
            sleep(time)
            life = self.getLife(self)

    def mp(self,percent, spell,time):
        mana = self.getMana(self)
        while mana > percent:
            w.Write(spell)
            sleep(time)
            mana = self.getMana(self)

    def dancing(self):
        pyautogui.hotkey("ctrl", "up")
        pyautogui.hotkey("ctrl", "left")
        pyautogui.hotkey("ctrl", "right")
        pyautogui.hotkey("ctrl", "down")

    def equipItem(self,name, slot):
        ref = pyautogui.locateOnScreen("slots.png")
        w.find_window_wildcard(".*Tibia.*")
        if (slot == "head"):
            item = pyautogui.locateOnScreen(name + ".png", grayscale=True)
            w.MouseDrag((item.left, item.top), ((ref.left - 22, ref.top + 19)))
        elif (slot == "armor"):
            item = pyautogui.locateOnScreen(name + ".png", grayscale=True)
            w.MouseDrag((item.left, item.top), ((ref.left - 21, ref.top + 50)))
        elif (slot == "legs"):
            item = pyautogui.locateOnScreen(name + ".png", grayscale=True)
            w.MouseDrag((item.left, item.top), ((ref.left - 21, ref.top + 90)))
        elif (slot == "boots"):
            item = pyautogui.locateOnScreen(name + ".png", grayscale=True)
            w.MouseDrag((item.left, item.top), ((ref.left - 21, ref.top + 130)))
        elif (slot == "necklace"):
            item = pyautogui.locateOnScreen(name + ".png", grayscale=True)
            w.MouseDrag((item.left, item.top), ((ref.left - 57, ref.top + 25)))
        elif (slot == "lhand"):
            item = pyautogui.locateOnScreen(name + ".png", grayscale=True)
            w.MouseDrag((item.left, item.top), ((ref.left - 55, ref.top + 70)))
        elif (slot == "rhand"):
            item = pyautogui.locateOnScreen(name + ".png", grayscale=True)
            w.MouseDrag((item.left, item.top), ((ref.left - 20, ref.top + 70)))
        elif (slot == "ring"):
            item = pyautogui.locateOnScreen(name + ".png", grayscale=True)
            w.MouseDrag((item.left, item.top), ((ref.left - 57, ref.top + 100)))
        elif (slot == "backpack"):
            item = pyautogui.locateOnScreen(name + ".png", grayscale=True)
            w.MouseDrag((item.left, item.top), ((ref.left - 20, ref.top + 25)))
        elif (slot == "free"):
            item = pyautogui.locateOnScreen(name + ".png", grayscale=True)
            w.MouseDrag((item.left, item.top), ((ref.left - 20, ref.top + 100)))

    def making_runes(self,rune_spell, rune_time):
        while rune_spell != "":
            try:
                pyautogui.locateOnScreen("mana.png", grayscale=True)
                # Make the rune
                w.Write(self.spell)
                sleep(1)
                self.eat_food()
            except:
                print("Except: making runes")
            print("Making runes: " + rune_spell)
            time.sleep(rune_time)

            
    def fishing(self):
        try:
            loc = pyautogui.locateOnScreen("water.png", confidence=.8)
            self.useOnLocation(self,loc.left,loc.top,"fishing")
        except:
            Exception("Fishing")
        