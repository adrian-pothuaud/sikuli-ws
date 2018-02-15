# -*- coding:utf-8 -*-

'''
This module is intended to demonstrate how to use ou Sikuli scaffolding functions
e.g Create a Sikuli module
'''

# import sikuli features
from sikuli import *

import sys

# add a path to sys.path
print("\nAdding 'allos' path to execution path")
new_path = os.path.join(os.path.dirname(os.path.dirname(getBundlePath())), "allos")
if not new_path in sys.path:
    sys.path.append(new_path)

# import generate module
import path_utils, generate

# set path to specs folder to create a scenario
# alternatively set path to allos to create an utility module
specs_path = path_utils.get_parent_dirname(getBundlePath(), 1)
new_script_path = os.path.join(specs_path, "autogen_hello_sikuli")

# set content as a list of lines
# use generate.DEFAULT_SCRIPT_BASE to generate common basic script
new_script_content = generate.DEFAULT_SCRIPT_BASE + [r'print("Not default action")']

# call scaffolder
generate.create_sikuli_script(new_script_path, new_script_content)
