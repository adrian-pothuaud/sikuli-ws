# -*- coding:utf-8 -*-

'''
This module is a demo scenario for Notepad++
'''

# import sikuli features
from sikuli import *

import sys

# add a path to sys.path
print("\nAdding 'allos' path to execution path")
new_path = os.path.join(os.path.dirname(os.path.dirname(getBundlePath())), "allos")
if not new_path in sys.path:
    sys.path.append(new_path)
print("\nAdding 'win' path to execution path")
new_path = os.path.join(os.path.dirname(os.path.dirname(getBundlePath())), "win")
if not new_path in sys.path:
    sys.path.append(new_path)

# import module
import applications, notepadpp

applications.launch_app("notepad++", wait_img=True, timeout=10)
r = notepadpp.find_menu_reg()
notepadpp.open_menu('view')

print(r)
