import win32gui
import win32api
from tkinter import *
import win32con


class WinApi:
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

    def getWindowSizes(self):
        win32gui.GetWindowRect(self._handle)

    def LeftClick(self, pos):
        client_pos = win32gui.ScreenToClient(self._handle, pos)
        tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
        win32api.PostMessage(self._handle, win32con.WM_MOUSEMOVE, 0, tmp)
        win32api.SendMessage(self._handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
        win32api.SendMessage(self._handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)

    def UseOn(self, pos,posy):
        client_pos = win32gui.ScreenToClient(self._handle, pos)
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

    def Write(self, spell):
        for i in spell:
            win32api.SendMessage(self._handle, win32con.WM_CHAR, ord(i), 0)
        win32api.SendMessage(self._handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32api.SendMessage(self._handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

    def MouseDrag(self, posx, posy):
        clientx = win32gui.ScreenToClient(self._handle, posx)
        lparamx = win32api.MAKELONG(clientx[0], clientx[1])
        clienty = win32gui.ScreenToClient(self._handle, posy)
        lparamy = win32api.MAKELONG(clienty[0], clienty[1])
        win32api.SendMessage(self._handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lparamx)
        win32api.SendMessage(self._handle, win32con.WM_MOUSEMOVE, 0, lparamy)
        win32api.SendMessage(self._handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lparamy)