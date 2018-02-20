"""
Module:  region

Author:  arjs.net

License: http://opensource.org/licenses/mit-license.html; year=2013,2014; copyright holders=arjs.net

Module for the region dictionary
"""
import logging

# noinspection PyUnresolvedReferences
from sikuli.Sikuli import *


# noinspection PyUnresolvedReferences
class RegionDictionary:
    """RegionDictionary: Dictionary of some useful regions"""

    def __init__(self, screenwidth, screenheight):
        """
        :param screenwidth:
        :type screenwidth: int
        :param screenheight:
        :type screenheight: int
        :rtype: RegionDictionary
        """
        logging.debug("W: %s" % str(screenwidth))
        logging.debug("H: %s" % str(screenheight))
        self.regdict = {}
        self.addreg("topHalf", Region(0, 0, screenwidth, (screenheight / 2)))
        logging.debug("topHalf:%s" % str(self.regdict["topHalf"]))

        self.addreg("bottomHalf", Region(0, (screenheight / 2), screenwidth, (screenheight / 2)))
        logging.debug("bottomHalf:%s" % str(self.regdict["bottomHalf"]))

        self.addreg("leftHalf", Region(0, 0, (screenwidth / 2), screenheight))
        logging.debug("leftHalf:%s" % str(self.regdict["leftHalf"]))

        self.addreg("rightHalf", Region((screenwidth / 2), 0, (screenwidth / 2), screenheight))
        logging.debug("rightHalf:%s" % str(self.regdict["rightHalf"]))

        self.addreg("center", Region(((screenwidth * 2 / 3)), ((screenheight * 2 / 3)), ((screenwidth * 1 / 3)),
                                     ((screenheight * 1 / 3))))
        logging.debug("center:%s" % str(self.regdict["center"]))

        self.addreg("nw", Region(0, 0, (screenwidth / 2), (screenheight / 2)))
        logging.debug("nw:%s" % str(self.regdict["nw"]))

        self.addreg("sw", Region(0, (screenheight / 2), (screenwidth / 2), (screenheight / 2)))
        logging.debug("sw:%s" % str(self.regdict["sw"]))

        self.addreg("ne", Region((screenwidth / 2), 0, (screenwidth / 2), (screenheight / 2)))
        logging.debug("ne:%s" % str(self.regdict["ne"]))

        self.addreg("se", Region((screenwidth / 2), (screenheight / 2), (screenwidth / 2), (screenheight / 2)))
        logging.debug("se:%s" % str(self.regdict["se"]))

    def addreg(self, name, reg):
        """
        :param name: Name of the region
        :type name: str
        :param reg: Region defintion
        :type reg: Region
        :rtype: None

        Add a region
        """
        self.regdict[name] = reg

    def getreg(self, name):
        """
        :param name: Name of the region
        :type name: str
        :return:
        :rtype: Region

        Get a region by name
        """
        return self.regdict[name]
