# -*- coding:utf-8 -*-

"""
    file: src/sample.py

    Sample Source file
    ==================

    Description
    -----------

    Sample description ...

    Content
    -------

    - say_hello_sikuli

    Status
    ------

    Test with: tests/sample.py
    last verification date: xx/xx/xxxx
    last verification status: XX

"""

from sikuli import *


def say_hello_sikuli():
    """

    :return:
    """
    popup("Hello World !", title="Sikuli")
