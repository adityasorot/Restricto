import ctypes
import os
import winreg as wreg
import time
import datetime
from subprocess import call

if os.name == 'nt':
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("\n Admin privilages needed!\n")
key= wreg.CreateKey(wreg.HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer")
wreg.SetValueEx(key,"DisallowRun",0,wreg.REG_DWORD,1)
key= wreg.CreateKey(wreg.HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\DisallowRun")
l = ['msedge.exe','chrome.exe']
for i,j in enumerate(l):
    wreg.SetValueEx(key,str(i),0,wreg.REG_SZ,j)
call('taskkill /F /IM explorer.exe & start explorer', shell=True)