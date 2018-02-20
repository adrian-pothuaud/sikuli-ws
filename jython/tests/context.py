import os
import sys

DEBUG = True

rootpath = os.path.dirname(os.path.dirname(__file__))
src_path = os.path.join(rootpath, "src")
if DEBUG:
    print("src_path in test context: {}".format(src_path))

out_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "out")

if src_path not in sys.path:
    sys.path.insert(0, src_path)
