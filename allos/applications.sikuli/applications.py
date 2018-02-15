# -*- coding:utf-8 -*-

'''Control Applications with Sikuli features
https://github.com/RaiMan/SikuliX-2014/blob/develop/API/src/main/java/org/sikuli/script/App.java
App class needs application path to be executed so final functions will be declared in os specific libraries
in this module we define os independent reusable behaviors'''

from sikuli import getBundlePath, Key, Env, App

import os, glob

# import modules
import path_utils, image_utils

def launch_app(app_name, wait_img=False, timeout=10):
    '''Process to launch an app (os independent)'''
    ws_root = path_utils.get_ws_root_path()
    os_path = None
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
