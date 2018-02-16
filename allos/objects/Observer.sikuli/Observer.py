# -*- coding:utf-8 -*-

from sikuli import *

from threading import Thread
import time
import shutil

class Observeur(Thread):
    """Thread charge d observer des changements dans une region donnee"""

    def __init__(self, reg=Screen(0), timeout=10, output=None):
        Thread.__init__(self)
        self.reg = reg
        self.timeout = timeout
        self.output = output
        self.currentRegImg = capture(self.reg)

    def __str__(self):
        return "Observeur (instance) {} sur la region {}".format(self.name, self.reg)

    # def run(self):
    #     """code a execuer pendant l execution du thread"""
    #     for i in range(self.timeout):
    #         if self.reg.exists(Pattern(self.currentRegImg).exact(), 1):
    #             pass
    #         else:
    #             self.currentRegImg = capture(self.reg)
    #             shutil.move(self.currentRegImg, self.output)
    #             break

    def onChange(self, event):
        ch = event.changes[0]
        self.currentRegImg = capture(ch)
        shutil.move(self.currentRegImg, self.output)

    def run(self):
        self.reg.onChange(self.onChange)
        self.observe(timeout)

if __name__ == '__main__':

    o1 = Observeur(Screen(0), 3, "test1.png")
    o2 = Observeur(Screen(0), 3, "test2.png")
    o3 = Observeur(Screen(0), 3, "test3.png")

    o1.start()
    wait(2)
    o2.start()
    wait(1)
    o3.start()

    o1.join()
    o2.join()
    o3.join()
