# -*- coding:utf-8 -*-

"""

    The '''path_utils''' module
    ===========================

    Use it to import applications functions.

    Module content
    --------------

    - launch_app

    Module state
    ------------
    status: ?
    test: run specs/launch_applications.sikuli

    .. sectionauthor:: Adrian Pothuaud <adrianpothuaud2@gmail.com>

"""

from sikuli import *

import os
import glob

# src modules
import specscontext
import path_utils, image_utils

DEBUG = True


def launch_app(app_name, app_path=None, wait_img=False, timeout=10):
    '''Process to launch an app (os independent)'''
    app_path = None
    os_img_lib = None
    if Env.isWindows():
        os_path = os.path.join(ws_root, 'win')
        os_img_lib = 'win'
        maximize_shortcut = (Key.UP, Key.WIN)
    elif Env.isMac():
        os_path = os.path.join(ws_root, 'osx')
        os_img_lib = 'osx'
        maximize_shortcut = None
    elif Env.isLinux():
        os_path = os.path.join(ws_root, 'linux')
        os_img_lib = 'linux'
        maximize_shortcut = None
    path_utils.add_execution_path(os_path)
    import os_applications
    app = App(os_applications.APPS[app_name]["path"])
    if not App(app_name).isRunning():
        app.open()
    else:
        app.focus()
    if wait_img:
        print("Waiting for app to be openned...")
        img_lib = os.path.join(
            path_utils.get_parent_dirname(getBundlePath(), 2),
            "imgs"
        )
        imgs = glob.glob(
            "{}{}start{}*.png".format(
                os.path.join(img_lib, os_img_lib, app_name.replace(' ', '_').replace('+', 'p')),
                os.sep,
                os.sep
            )
        )
        image_utils.wait_all(imgs)
        print("App is openned !")
    type(maximize_shortcut)
