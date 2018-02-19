# -*- coding:utf-8 -*-

"""
This module is intended to demonstrate how to use ou Sikuli scaffolding functions
e.g Create a Sikuli module


status: OK (02-19-2018)
"""

# import sikuli features
from sikuli import *

import specscontext

# import generate module
import path_utils, generate

# set path to specs folder to create a scenario
# alternatively set path to allos to create an utility module
new_script_path = os.path.join(os.path.dirname(getBundlePath()), "autoHelloSample.sikuli")

# set content as a list of lines
# use generate.DEFAULT_SCRIPT_BASE to generate common basic script
new_script_content = generate.DEFAULT_SCRIPT_BASE + [r'print("Not default action")']

# call scaffolder
generate.create_sikuli_script(new_script_path, new_script_content)
