# -*- coding:utf-8 -*-

"""
This module is intended to demonstrate how to use Sikuli applications module
e.g Launch google chrome
status: ?
"""

# import sikuli features
from sikuli import *

import specscontext

# import module
import applications

applications.launch_app("google chrome", wait_img=True, timeout=10)
