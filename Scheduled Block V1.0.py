import ctypes
import os
import winreg as wreg
import time
import datetime
from subprocess import call
from threading import Thread


def block():
    for _ in range(0,365):
        t = datetime.datetime.today()
        future = datetime.datetime(t.year, t.month, t.day, 8, 10)
        if t.weekday() == 5:
            future += datetime.timedelta(days=2)
            key= wreg.CreateKey(wreg.HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer")
            wreg.SetValueEx(key,"DisallowRun",0,wreg.REG_DWORD,0)
            call('taskkill /F /IM explorer.exe & start explorer', shell=True)
            print(future)
            time.sleep((future-t).total_seconds())
            continue
        elif t.weekday() == 6:
            future += datetime.timedelta(days=1)
            key= wreg.CreateKey(wreg.HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer")
            wreg.SetValueEx(key,"DisallowRun",0,wreg.REG_DWORD,0)
            call('taskkill /F /IM explorer.exe & start explorer', shell=True)
            time.sleep((future-t).total_seconds())
            continue
        elif 490 <= t.hour * 60 + t.minute <= 780:
            key= wreg.CreateKey(wreg.HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer")
            wreg.SetValueEx(key,"DisallowRun",0,wreg.REG_DWORD,1)
            call('taskkill /F /IM explorer.exe & start explorer', shell=True)
            future += datetime.timedelta(days=1)
        elif t.timestamp() > future.timestamp():
            future += datetime.timedelta(days=1)
        if os.name == 'nt':
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print("\n Admin privilages needed!\n")
        print(future)
        time.sleep((future-t).total_seconds())
    return None

def unblock():
    for _ in range(0,365):
        t = datetime.datetime.today()
        future = datetime.datetime(t.year, t.month, t.day, 13, 0)
        if t.weekday() == 5:
            future += datetime.timedelta(days=2)
            key= wreg.CreateKey(wreg.HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer")
            wreg.SetValueEx(key,"DisallowRun",0,wreg.REG_DWORD,0)
            call('taskkill /F /IM explorer.exe & start explorer', shell=True)
            print(future)
            time.sleep((future-t).total_seconds())
            continue
        elif t.weekday() == 6:
            future += datetime.timedelta(days=1)
            key= wreg.CreateKey(wreg.HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer")
            wreg.SetValueEx(key,"DisallowRun",0,wreg.REG_DWORD,0)
            call('taskkill /F /IM explorer.exe & start explorer', shell=True)
            time.sleep((future-t).total_seconds())
            continue
        elif not (490 <= t.hour * 60 + t.minute <= 780):
            key= wreg.CreateKey(wreg.HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer")
            wreg.SetValueEx(key,"DisallowRun",0,wreg.REG_DWORD,0)
            call('taskkill /F /IM explorer.exe & start explorer', shell=True)
            future += datetime.timedelta(days=1)
        elif t.timestamp() > future.timestamp():
            future += datetime.timedelta(days=1)
        if os.name == 'nt':
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print("\n Admin privilages needed!\n")
        print(future)
        time.sleep((future-t).total_seconds())
    return None

def set_values(l):
    if os.name == 'nt':
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("\n Admin privilages needed!\n")
    key= wreg.CreateKey(wreg.HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer")
    wreg.SetValueEx(key,"DisallowRun",0,wreg.REG_DWORD,0)
    key= wreg.CreateKey(wreg.HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\DisallowRun")
    for i,j in enumerate(l):
        wreg.SetValueEx(key,str(i),0,wreg.REG_SZ,j)
    return None

if __name__ == "__main__":
    list_to_be_passed = ['msedge.exe','chrome.exe']
    set_values(list_to_be_passed)
    Thread(target = block).start()
    Thread(target = unblock).start()
