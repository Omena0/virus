from src.shared import *
import platform
import src.uep as uep

set_priority()

if not is_admin():
    exit()

if platform.system() != 'Windows':
    exit()

uep.check_all()





while True: ...
