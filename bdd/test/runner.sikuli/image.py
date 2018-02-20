"""
Module:  image

Author:  arjs.net

License: http://opensource.org/licenses/mit-license.html; year=2013,2014; copyright holders=arjs.net

Module for the image dictionary
"""
import os
import logging

# noinspection PyUnresolvedReferences
from sikuli.Sikuli import *


# noinspection PyUnresolvedReferences
class ImagesDictionary:
    """ImagesDictionary: Dictionary for all images in the images folders"""

    def __init__(self, imagespath, specificpath):
        """
        :param imagespath:
        :type imagespath: str
        :param specificpath:
        :type specificpath: str
        :rtype: ImagesDictionary
        """
        self.imgdict = {}
        self.imagespath = imagespath
        self.specificpath = specificpath

        addImagePath(imagespath)
        addImagePath(os.path.join(imagespath, specificpath))
        logging.debug("folder: %s" % imagespath)
        logging.debug("specific: %s" % specificpath)
        logging.debug("specific folder: %s" % os.path.join(imagespath, specificpath))

        self.addimagesfromfolder(imagespath, specificpath)
        for k in self.imgdict.keys():
            logging.debug("%s = %s" % (k, self.imgdict[k]))

    def addimage(self, name, img):
        """
        :param name: Image name
        :type name: str
        :param img: Image path
        :type img: img
        :rtype: None

        Add a image to dictionary

        """
        self.imgdict[name] = img

    def getimage(self, name):
        """
        :param name: Image name
        :type name: str
        :return:
        :rtype: None

        Retruns the requested image

        :raise EnvironmentError:
        """
        if name.endswith('.png') or name.endswith('.gif') or name.endswith('.jpg'):
            if name[:-4] in self.imgdict.keys():
                return self.imgdict[name[:-4]]
            else:
                raise EnvironmentError("No image '%s' found." % name)
        else:
            if name in self.imgdict.keys():
                return self.imgdict[name]
            else:
                raise EnvironmentError("No image '%s' found." % name)

    def addimagesfromfolder(self, folder, specific):
        """
        :param folder: Image folder
        :type folder: str
        :param specific: Filter for specific endings
        :type specific: str
        :rtype: None

        Add images from a folder
        """
        for path, dirs, files in os.walk(folder):
            logging.debug("path: %s" % path)
            if path.replace(folder, ''):
                if not path.endswith(specific[:-1]):
                    continue

            for filename in files:
                logging.debug("filename: %s" % filename)
                if filename.endswith('.png'):
                    self.addimage(filename[:-4], filename)
                    continue

                if filename.endswith('.gif'):
                    self.addimage(filename[:-4], filename)
                    continue

                if filename.endswith('.jpg'):
                    self.addimage(filename[:-4], filename)
                    continue

                if filename.startswith('.'):
                    continue

                logging.info("filename '%s' ignored..." % filename)
