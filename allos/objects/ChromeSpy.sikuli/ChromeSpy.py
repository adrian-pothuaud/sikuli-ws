# -*- coding:utf-8 -*-

"""Google Chrome UI spy object"""

from sikuli import *

from Observer import Observeur
from ChromeApp import Chrome

class ChromeSpy(Observeur):
    """Spy Thread for Google Chrome application"""

    def __str__(self):
        return "ChromeSpy (instance) {} sur la region {}".format(self.name, self.reg)

if __name__ == '__main__':

    c = Chrome()
    c.open()

    wait(2)

    spy1 = ChromeSpy(output=os.path.join(getBundlePath(), "1.png"))
    spy1.start()

    wait(1)

    c.bookmark()

    spy1.join()

    find("1.png").highlight(1)
