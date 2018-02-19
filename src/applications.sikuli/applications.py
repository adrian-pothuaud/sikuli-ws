# -*- coding:utf-8 -*-

"""

    The '''path_utils''' module
    ===========================

    Use it to import applications functions.

    Module content
    --------------

    - APPS
    - SHORTCUTS
    - launch_app

    Module state
    ------------
    status: ok (2/19/2018)
    test: run specs/launch_applications.sikuli
    unit tests:
        - run tests/applications_tests.sikuli
        - results: out/test_reports/applications_tests

    .. sectionauthor:: Adrian Pothuaud <adrianpothuaud2@gmail.com>

"""

from sikuli import *

import os
import glob

# src modules
import path_utils, image_utils

DEBUG = True


APPS = {
    "MAC": {
        "google chrome": {
            "path": r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        }
    },
    "WINDOWS": {
        "google chrome": {
            "path": r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        }
    },
    "LINUX": {
        "google chrome": {
            "path": ""
        }
    }
}

"""
    Shortcuts for MAC requires to be created
        - System Preferences -> Keyboard
        - Keyboard shortcuts -> Applications shortcuts

    Create the followings:
        - Application: ALL, Name: Zoom, shortcut:
"""
SHORTCUTS = {
    "MAC": {
        "maximize": [Key.CTRL, Key.CMD, '=']
    },
    "WINDOWS": {
        "maximize": (Key.UP, Key.WIN)
    },
    "LINUX": {
        "maximize": ()
    }
}

def launch_app(app_name=None, app_path=None, wait_img=False, timeout=10):
    """
    Open an application.

    Give:
    - app_name and ensure APPS[app_name] is defined
    - if APPS[app_name] is undefined, then give app_path
    - choose either to wait or not for images in imgs/app_name/start
    -> wait: set wait_img as True
    - default timeout is 10
    This will define a Sikuli App() instance and run it.

    :param app_name: application_name as in APPS
    :type path: str
    :param app_path: path to application executable or script
    :type app_path: str
    :param wait_img: wait for imgs in imgs/app_name/start or not
    :type wait_img: boolean
    :param timeout: timeout for wait for imgs in imgs/app_name/start or not
    :type timeout: int
    :return: Nothing
    :rtype: None

    """
    if DEBUG:
        print("Trying to launch application with parameters:")
        print("app_name: {}, app_path: {}, wait_img: {}, timeout: {}".format(
            app_name,
            app_path,
            wait_img,
            timeout
        ))
        print("Actual OS is {}".format(Env.getOS()))
    # guess image library
    img_lib = os.path.join(
        path_utils.get_parent_dirname(
            getBundlePath(), 2
        ),
        "imgs",
        app_name.replace(' ', '_')
    )
    if DEBUG:
        print("img_lib: {}".format(img_lib))
    maximize_shortcut = SHORTCUTS[str(Env.getOS())]["maximize"]
    if DEBUG:
        print("maximize_shortcut: {}".format(maximize_shortcut))
    app = App(APPS[str(Env.getOS())][app_name]["path"])
    if not App(app_name).isRunning():
        if DEBUG:
            print("App {} currently not running.".format(app_name))
        app.open()
        if DEBUG:
            print("App {} should now be openned.".format(app_name))
    else:
        if DEBUG:
            print("App {} currently running, trying to focus ont it...".format(app_name))
        app.focus()
    if wait_img:
        print("Waiting for app images to ensure it is openned...")
        start = os.path.join(
            img_lib,
            "start"
        )
        imgs = glob.glob(
            os.path.join(start, "*")
        )
        if DEBUG:
            print("All images to wait:")
            for im in imgs:
                print("\t{},".format(im))
        img2 = []
        for im in imgs:
            im = im.split(os.sep)[-1]
            img2.append(im)
        path_utils.add_image_path(start)
        path_utils.print_image_path()
        image_utils.wait_all(img2)
        if DEBUG:
            print("App is openned !")
    if Env.isWindows():
        type(*maximize_shortcut)
    # ToDo: fix shortcuts for MAC
    if DEBUG:
        print('App should now be maximized.')
