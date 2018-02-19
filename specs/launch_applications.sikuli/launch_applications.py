# -*- coding:utf-8 -*-

"""
This module is intended to demonstrate how to use Sikuli applications module
e.g Launch google chrome
status: ?
"""

# import sikuli features
from sikuli import *

import sys

# add a path to sys.path
print("\nAdding 'allos' path to execution path")
new_path = os.path.join(os.path.dirname(os.path.dirname(getBundlePath())), "allos")
if not new_path in sys.path:
    sys.path.append(new_path)

# import module
import applications

applications.launch_app("google chrome", wait_img=True, timeout=10)
