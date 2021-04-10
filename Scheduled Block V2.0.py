import ctypes
import os
import winreg as wreg
import time
import datetime
from subprocess import call
from threading import Thread




def block():
    while True:
        t = datetime.datetime.today()
        future = datetime.datetime(t.year, t.month, t.day, 8, 0)
        key= wreg.CreateKey(wreg.HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer")
        if t.weekday() == 5:
            future += datetime.timedelta(days=2)
            time.sleep((future-t).total_seconds())
        elif t.weekday() == 6:
            future += datetime.timedelta(days=1)
            time.sleep((future-t).total_seconds())
        elif 490 <= t.hour * 60 + t.minute <= 780:
            i=wreg.QueryValueEx(key, "DisallowRun")[0]
            if i==1:
                time.sleep(300)
            else:
                wreg.SetValueEx(key,"DisallowRun",0,wreg.REG_DWORD,1)
                call('taskkill /F /IM msedge.exe /IM chrome.exe', shell=True)
                call('taskkill /F /IM explorer.exe & start explorer', shell=True)
                time.sleep(300)
        time.sleep(300)
    return None

def unblock():
    while True:
        t = datetime.datetime.today()
        future = datetime.datetime(t.year, t.month, t.day, 8, 0)
        key= wreg.CreateKey(wreg.HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer")
        if t.weekday() == 5:
            future += datetime.timedelta(days=2)
            i=wreg.QueryValueEx(key, "DisallowRun")[0]
            if i==0:
                time.sleep((future-t).total_seconds())
                continue
            else:
                wreg.SetValueEx(key,"DisallowRun",0,wreg.REG_DWORD,0)
                call('taskkill /F /IM explorer.exe & start explorer', shell=True)
                time.sleep((future-t).total_seconds())
                continue
        elif t.weekday() == 6:
            future += datetime.timedelta(days=1)
            i=wreg.QueryValueEx(key, "DisallowRun")[0]
            if i==0:
                time.sleep((future-t).total_seconds())
                continue
            else:
                wreg.SetValueEx(key,"DisallowRun",0,wreg.REG_DWORD,0)
                call('taskkill /F /IM explorer.exe & start explorer', shell=True)
                time.sleep((future-t).total_seconds())
                continue
        elif not (490 <= t.hour * 60 + t.minute <= 780):
            i=wreg.QueryValueEx(key, "DisallowRun")[0]
            if i==0:
                time.sleep(300)
                continue
            else:
                wreg.SetValueEx(key,"DisallowRun",0,wreg.REG_DWORD,0)
                call('taskkill /F /IM explorer.exe & start explorer', shell=True)
                time.sleep(300)
                continue
        else:
            time.sleep(300)
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

