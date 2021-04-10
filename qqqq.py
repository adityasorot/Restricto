import ctypes
import os
import winreg as wreg
import time
import datetime
from subprocess import call
from threading import Thread


def block():
    j=4
    for i in range(0,365):
        t = datetime.datetime.today()
        future = t+ datetime.timedelta(minutes=1)   # datetime.datetime(t.year, t.month, t.day, t.hour, 10)
        if j == 4:
            future += datetime.timedelta(minutes=1)
            print("weekday block")
            print('B-',future)
            j+=1
            time.sleep((future-t).total_seconds())
            continue
        elif j == 6:
            future += datetime.timedelta(minutes=1)
            print("weekday block")
            print('B-',future)
            j+=1
            time.sleep((future-t).total_seconds())
            continue
        elif 1321 <= t.hour * 60 + t.minute <= 1324:
            print("Blocked")
            future += datetime.timedelta(minutes=1)
        elif t.timestamp() > future.timestamp():
            future += datetime.timedelta(minutes=1)
        j+=1
        if os.name == 'nt':
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print("\n Admin privilages needed!\n")
        print('B-',future)
        time.sleep((future-t).total_seconds())
        #print("Blocked")
    return None

def unblock():
    j=4
    for i in range(0,365):
        t = datetime.datetime.today()
        future = t + datetime.timedelta(minutes=1)
        if j == 4:
            future += datetime.timedelta(minutes=1)
            print("weekday unblock")
            print('U-',future)
            j+=1
            time.sleep((future-t).total_seconds())
            continue
        elif j == 6:
            future += datetime.timedelta(minutes=1)
            print("weekday unblock")
            print('U-',future)
            j+=1
            time.sleep((future-t).total_seconds())
            continue
        elif not (1321 <= t.hour * 60 + t.minute <= 1324):
            print("UnBlocked")
            future += datetime.timedelta(minutes=1)
        elif t.timestamp() > future.timestamp():
            future += datetime.timedelta(minutes=1)
        j+=1
        if os.name == 'nt':
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print("\n Admin privilages needed!\n")
        print('U-',future)
        time.sleep((future-t).total_seconds())
        #print("UnBlocked")
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
    #set_values(list_to_be_passed)
    Thread(target = block).start()
    Thread(target = unblock).start()
