import os
import time
import pyautogui
import win32api
import win32gui
from pynput import keyboard
from time import sleep
import win32con
from threading import Thread
from tkinter import *



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

botcores = []

threads = list()
lt = Thread(target=listen)
threads.append(lt)
lt.start()



class WindowMgr:
    # FOCUS GAME
    def __init__ (self):
        self._handle = None

    def find_window(self, class_name, window_name=None):
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        win32gui.SetForegroundWindow(self._handle)

    def getWindowSize(self):
        rect = win32gui.GetWindowRect(self._handle)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        return x,y,w,h

    def LeftClick(self, pos):
        client_pos = win32gui.ScreenToClient(self._handle, pos)
        tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
        win32api.PostMessage(self._handle, win32con.WM_MOUSEMOVE, 0, tmp)
        win32api.SendMessage(self._handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
        win32api.SendMessage(self._handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)

    def UseOn(self, posx,posy):
        client_pos = win32gui.ScreenToClient(self._handle, posx)
        tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
        win32api.PostMessage(self._handle, win32con.WM_MOUSEMOVE, 0, tmp)
        win32api.SendMessage(self._handle, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, tmp)
        win32api.SendMessage(self._handle, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, tmp)
        client_posy = win32gui.ScreenToClient(self._handle, posy)
        tmpy = win32api.MAKELONG(client_posy[0], client_posy[1])
        win32api.PostMessage(self._handle, win32con.WM_MOUSEMOVE, 0, tmpy)
        win32api.SendMessage(self._handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmpy)
        win32api.SendMessage(self._handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmpy)

    def RightClick(self, pos):
        client_pos = win32gui.ScreenToClient(self._handle, pos)
        tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
        win32api.PostMessage(self._handle,win32con.WM_MOUSEMOVE, 0,tmp)
        win32api.SendMessage(self._handle, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, tmp)
        win32api.SendMessage(self._handle, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, tmp)

    def MoveToDefault(self):
        client_pos = win32gui.ScreenToClient(self._handle, (500,500))
        tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
        win32api.PostMessage(self._handle,win32con.WM_MOUSEMOVE, 0,tmp)

    def Write(self, spell):
        for i in spell:
            win32api.SendMessage(self._handle, win32con.WM_CHAR, ord(i), 0)
        win32api.SendMessage(self._handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32api.SendMessage(self._handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

    def MouseDrag(self,posx,posy):
        clientx = win32gui.ScreenToClient(self._handle,posx)
        lparamx = win32api.MAKELONG(clientx[0],clientx[1])
        clienty = win32gui.ScreenToClient(self._handle,posy)
        lparamy = win32api.MAKELONG(clienty[0],clienty[1])
        win32api.SendMessage(self._handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lparamx)
        win32api.SendMessage(self._handle, win32con.WM_MOUSEMOVE, 0, lparamy)
        win32api.SendMessage(self._handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lparamy)

    def KeyStrokes(self,key1,ctrl):

        if(ctrl == True):
            win32api.SendMessage(self._handle, win32con.WM_KEYDOWN, win32con.WM_SYSCOMMAND, 0)
            sleep(1)
            if(key1 == "up"):
                win32api.SendMessage(self._handle, win32con.WM_KEYDOWN, win32con.VK_UP, 0)
                win32api.SendMessage(self._handle, win32con.WM_KEYUP, win32con.VK_UP, 0)
            elif(key1 == "down"):
                win32api.SendMessage(self._handle, win32con.WM_KEYDOWN, win32con.VK_UP, 0)
                win32api.SendMessage(self._handle, win32con.WM_KEYUP, win32con.VK_UP, 0)
            elif(key1 == "left"):
                win32api.SendMessage(self._handle, win32con.WM_KEYDOWN, win32con.VK_UP, 0)
                win32api.SendMessage(self._handle, win32con.WM_KEYUP, win32con.VK_UP, 0)
            elif(key1 == "right"):
                win32api.SendMessage(self._handle, win32con.WM_KEYDOWN, win32con.VK_UP, 0)
                win32api.SendMessage(self._handle, win32con.WM_KEYUP, win32con.VK_UP, 0)
            elif(key1):
                win32api.SendMessage(self._handle, win32con.WM_CHAR, ord(key1), 0)

            win32api.SendMessage(self._handle, win32con.WM_KEYUP, win32con.WM_SYSCOMMAND, 0)
        else:
            if (key1 == "up"):
                win32api.SendMessage(self._handle, win32con.WM_KEYDOWN, win32con.VK_UP, 0)
                win32api.SendMessage(self._handle, win32con.WM_KEYUP, win32con.VK_UP, 0)
            elif (key1 == "down"):
                win32api.SendMessage(self._handle, win32con.WM_KEYDOWN, win32con.VK_UP, 0)
                win32api.SendMessage(self._handle, win32con.WM_KEYUP, win32con.VK_UP, 0)
            elif (key1 == "left"):
                win32api.SendMessage(self._handle, win32con.WM_KEYDOWN, win32con.VK_UP, 0)
                win32api.SendMessage(self._handle, win32con.WM_KEYUP, win32con.VK_UP, 0)
            elif (key1 == "right"):
                win32api.SendMessage(self._handle, win32con.WM_KEYDOWN, win32con.VK_UP, 0)
                win32api.SendMessage(self._handle, win32con.WM_KEYUP, win32con.VK_UP, 0)
            elif (key1):
                win32api.SendMessage(self._handle, win32con.WM_CHAR, ord(key1), 0)



w = WindowMgr()
w.find_window_wildcard(".*Tibia.*")

def focus():
    # FOCUS GAME
    w.set_foreground()

def getwindowRect(type):
    rect = w.getWindowSize()
    if(type == "width"):
        return rect[2]
    elif(type == "height"):
        return rect[3]
    elif(type == "positionX"):
        return rect[0]
    elif(type == "positionY"):
        return rect[1]



os.chdir("images")

# Create an image list
image_list = ["health", "mana", "battle_list", "food","fishing","Rat","bp"]
# Loop image_list to check if images exists, so we avoid calling null files
for i in image_list:
    if not os.path.isfile(i + ".png"):
        print("Unable to find image file: " + i + ".png")
        wait = input("Press any key to quit.")
        sys.exit(0)


def attack(name):
    monster = pyautogui.locateOnScreen(name+".png", confidence=.9)
    w.LeftClick((monster.left, monster.top))
    w.MoveToDefault()
    sleep(1)
    while(pyautogui.locateOnScreen("attacking.png", confidence=.5)):
        if(pyautogui.locateOnScreen("follow.png") != None):
            follow = pyautogui.locateOnScreen("follow.png")
            w.LeftClick((follow.left,follow.top))
        sleep(3)
    
    
def loot(bpname,lootitems):
    loc = pyautogui.locateOnScreen(bpname+".png")
    w.RightClick((453,280))
    sleep(0.5)
    w.RightClick((500,280))
    sleep(0.5)
    w.RightClick((544,280))
    sleep(0.5)
    w.RightClick((461,325))
    sleep(0.5)
    w.RightClick((462,362))
    sleep(0.5)
    w.RightClick((507,365))
    sleep(0.5)
    w.RightClick((544,368))
    sleep(0.5)
    w.RightClick((548,322))
    sleep(1)
    count = len(lootitems)
    for i in range(0,(count - 1)):
        gold = pyautogui.locateAllOnScreen(lootitems[i]+'.png', confidence=.9, region=(1196,422, 1368, 726))
        for item in gold:
            w.MouseDrag((item.left,item.top),(loc.left,(loc.top+20)))
            sleep(1)

focus()
sleep(1)
stop = False
wptindex = 0

items = ["goldcoin","medicinepouch"]
target_list = ["swamptroll"]
while(stop == False):
    loc = list(pyautogui.locateAllOnScreen(os.getcwd()+"\\Wpt\\"+"1.png"))
    for i in target_list:
        try:
            if(pyautogui.locateOnScreen(i+".png", confidence=.9) != None):
                attack(i)
                sleep(1)
                if(pyautogui.locateOnScreen(i+".png",confidence=.9) == None):
                    loot("backpack",items)
        except:
            Exception("CaveBot")
    if(loc != None):
        if(loc[wptindex].left != 1242 and loc[wptindex].top != 79):
            try:
                w.LeftClick((loc[wptindex].left,loc[wptindex].top))
            except:
                Exception("Walk")
        else:
            if(wptindex >= (len(loc) - 1)):
                wptindex = 0
            else:
                wptindex = wptindex + 1
    sleep(1)
    