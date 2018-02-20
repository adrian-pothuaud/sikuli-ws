import os
import sys

DEBUG = True

src_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src")
if DEBUG:
    print("src_path in test context: {}".format(src_path))

if src_path not in sys.path:
    sys.path.insert(0, src_path)
