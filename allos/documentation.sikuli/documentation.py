# -*- coding:utf-8 -*-

'''This script is a module for auto documentation about sikuli framework/scenarios'''

from sikuli import *

import os, sys, glob, json

DOC = {}

ws_root = os.path.dirname(os.path.dirname(getBundlePath()))

folders_in_ws = glob.glob("{}{}*".format(ws_root, os.sep))
python_files_in_ws = []
sikuli_modules_in_ws = []
text_files_in_ws = []
html_files_in_ws = []
for f in folders_in_ws:
    if '.' in f and 'py' == f.split('.')[-1]:
        folders_in_ws.remove(f)
        python_files_in_ws.append(f)
    if '.' in f and'sikuli' == f.split('.')[-1]:
        folders_in_ws.remove(f)
        sikuli_modules_in_ws.append(f)
    if '.' in f and 'txt' == f.split('.')[-1]:
        folders_in_ws.remove(f)
        text_files_in_ws.append(f)
    if '.' in f and 'html' == f.split('.')[-1]:
        folders_in_ws.remove(f)
        html_files_in_ws.append(f)

DOC["ws_root"] = {
    "folders": folders_in_ws,
    "files": {
        "python": python_files_in_ws,
        "text": text_files_in_ws,
        "html": html_files_in_ws
    },
    "sikuli modules": sikuli_modules_in_ws
}
"""
for f in folders_in_ws:
    folders_in_f = glob.glob("{}{}*".format(f, os.sep))
    python_files_in_f = []
    sikuli_modules_in_f = []
    text_files_in_f = []
    html_files_in_f = []
    for fo in f:
        if '.' in fo and 'py' == fo.split('.')[-1]:
            folders_in_f.remove(fo)
            python_files_in_f.append(fo)
        if '.' in fo and'sikuli' == fo.split('.')[-1]:
            folders_in_f.remove(fo)
            sikuli_modules_in_f.append(fo)
        if '.' in fo and 'txt' == fo.split('.')[-1]:
            folders_in_f.remove(fo)
            text_files_in_f.append(fo)
        if '.' in fo and 'html' == fo.split('.')[-1]:
            folders_in_f.remove(fo)
            html_files_in_f.append(fo)

    DOC[f] = {
        "folders": folders_in_f,
        "files": {
            "python": python_files_in_f,
            "text": text_files_in_f,
            "html": html_files_in_f
        },
        "sikuli modules": sikuli_modules_in_f
    }
"""
with open(os.path.join(getBundlePath(), "out.json"), "w") as f:
    f.write(json.dumps(DOC, indent=4, sort_keys=True))