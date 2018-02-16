# -*- coding: utf-8 -*-

'''
Notepad++ features
'''

from sikuli import *

def open_menu(menu_name):
    '''Open a menu in noepad++ app'''
    click("menu_{}.png".format(menu_name))

def menuAppeared(event):
    print(event)
    event.region.stopObserver()
    return event.reg

def find_menu_reg():
    '''Spy menu apparition'''
    print('Spy menu apparition')
    s = Screen(0)
    w = s.getBounds().width
    h = s.getBounds().height
    r = Region(0, 0, w, h)
    r.onChange(menuAppeared)
    r.observe(10)

def find_submenus(reg, sort='y'):
    '''find all submenus in a menu region'''
    submenus = reg.findAll("submenu_arrow.png")
    if sort == 'y':
        return sorted(submenus, key=lambda m:m.y)
    else:
        return sorted(submenus, key=lambda m:m.x)
