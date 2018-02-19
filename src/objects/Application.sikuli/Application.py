# -*- coding:utf-8 -*-

"""

"""

class Application:
    """

    """
    def __init__(self, app_name, exec_path):
        self.name = app_name
        self.path = exec_path

    def __str__(self):
        return "Application '{}'".format(self.name)

    def open(self):
        """

        """
        if not App(self.name).isRunning():
            App.open(self.path)
        App.focus(self.name)

    def wait_is_openned(self):
        """

        """
        pass
