# -*- coding:utf-8 -*-

"""
This module is intended to demonstrate how to manipulate paths for Sikuli
e.g Manipulate Image Path
e.g Manipulate Execution Path

status: OK(02-12-2018)
"""

# import sikuli features
from sikuli import *

import sys

# get actual execution path
print("\nGetting actual execution path")
# also use path_utils.print_execution_path() in allos/pathUtils.sikuli
for p in sys.path:
    print(p)

# actual bundle is [ROOT]/.../paths.sikuli
print("\nGetting actual bundle")
print(getBundlePath())

# actual image path is the same
print("\nGetting actual image path")
print(getImagePath())

# add a path to sys.path
# also use path_utils.add_execution_path(new_path) in allos/pathUtils.sikuli
print("\nAdding a path to execution pathV F")
new_path = os.path.join(os.path.dirname(os.path.dirname(getBundlePath())), "src")
if not new_path in sys.path:
    sys.path.append(new_path)
# makes changes (add one path)
for p in sys.path:
    print(p)
# adding a path to exec path do not add it to image path
print("\nDoesn t change image path:")
print(getImagePath())

# now path has changed so we can import modules from new_path and use their functions
print("\nImporting a new sikuli module")
import path_utils
path_utils.print_execution_path()
# importing a sikuli module will also add it to image path
path_utils.print_image_path()

# if [ROOT]/.../allos is in sys.path, we can now add path(s) with ...
# use path_utils.get_parent_dirname(path, level) to get level x parent dirname
root_path = path_utils.get_parent_dirname(getBundlePath(), 2)
new_path1 = os.path.join(root_path, "src", "objects")
path_utils.add_execution_path(new_path1)
path_utils.print_execution_path()
# path already exists mistake is handled
path_utils.add_execution_path(new_path1)
# incorrect path will raise Error
try:
    path_utils.add_execution_path((123, 'ZE'))
except Exception as e:
    print(e)

# we can add path to image path
path_utils.add_image_path(os.path.join(root_path, "imgs"))
path_utils.print_image_path()
# this doesn t change execution path
path_utils.print_execution_path()
