"""
Module:  region
Author:  arjs.net
License: http://opensource.org/licenses/mit-license.html; year=2013,2014; copyright holders=arjs.net
"""

# noinspection PyUnresolvedReferences
from sikuli.Sikuli import *
from base import *
import case


#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
log = logging.getLogger('addons')


# noinspection PyUnresolvedReferences
class Chrome(Base):
    """Chrome: Extensions for chrome browser"""

    def __init__(self, bpath, rpath):
        """
        :param bpath:
        :type bpath: str
        :param rpath:
        :type rpath: str
        :rtype: Chrome
        """
        super(Chrome, self).__init__(bpath, rpath)

    def open(self, showdebug=False):
        """
        :param showdebug: Show debug information
        :type showdebug: bool
        :return:
        :rtype: object

        Open a chrome browser on linux, mac and windows

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        level = case.INFO if showdebug else case.DEBUG
        case.showinfo(level, '%s: Entered %s' % (datetime.datetime.now(), fname))

        try:
            case.showinfo(level, 'OS: ' + str(self.osname) + ' ' + str(self.osversion))
            if str(self.osname) == 'WINDOWS':
                argument = " --start-maximized"
                application = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                if not os.path.exists(application):
                    application = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            elif str(self.osname) == 'LINUX':
                argument = " --start-maximized"
                application = "/opt/google/chrome/chrome"
            else:
                argument = ""
                application = "Google Chrome"

            chrome = openApp(application + argument)
            if chrome is None:
                self.failed(fname, 'Chrome', True)
                raise EnvironmentError("No chrome browser opened!")
            else:
                self.passed(fname, 'Chrome', True)

            if self.doswitchapp:
                switchApp(application)

            if self.doopenwait:
                wait(self.openwaittime)

            if self.additionaltab:
                self.opentab()

            self.centermouse()

            return chrome

        except Exception, e:
            logging.exception('Exception: %s' % e.message)
            case.showinfo(case.ERROR, 'Exception: %s' % e.message)
            self.failed(fname, e.message, True)
            raise e

        finally:
            case.showinfo(level, '%s: Returned from %s' % (datetime.datetime.now(), fname))

    def close(self, showdebug=False):
        """
        :param showdebug: show debug information
        :type showdebug: bool
        :return:
        :rtype: bool

        Close the chrome browser

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        level = case.INFO if showdebug else case.DEBUG
        case.showinfo(level, '%s: Entered %s' % (datetime.datetime.now(), fname))

        try:
            case.showinfo(level, 'OS: ' + str(self.osname) + ' ' + str(self.osversion))
            if str(self.osname) == 'WINDOWS':
                application = "Chrome"
            elif str(self.osname) == 'LINUX':
                application = "/opt/google/chrome/chrome"
            else:
                application = "Google Chrome"

            if self.additionaltab:
                case.showinfo(level, 'Close Tab')
                self.closetab()

            case.showinfo(level, 'Close App: %s' % str(application))
            if str(self.osname) == 'WINDOWS':
                # type(Key.F4, KeyModifier.ALT)
                closeApp(application)
            elif str(self.osname) == 'LINUX':
                #type("W", KeyModifier.CTRL)
                closeApp(application)
                #else:
            #	closeApp(application)
            return self.passed(fname, 'Chrome', True)

        except Exception, e:
            logging.exception('Exception: %s' % e.message)
            case.showinfo(case.ERROR, 'Exception: %s' % e.message)
            return self.failed(fname, e.message, True)

        finally:
            case.showinfo(level, '%s: Returned from %s' % (datetime.datetime.now(), fname))

    def opentab(self, showdebug=False):
        """
        :param showdebug: show debug information
        :type showdebug: bool
        :return:
        :rtype: bool

        Open a new tab

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        level = case.INFO if showdebug else case.DEBUG
        case.showinfo(level, '%s: Entered %s' % (datetime.datetime.now(), fname))

        try:
            if str(self.osname) == 'MAC':
                type("t", KEY_CMD)
            else:
                type("t", KEY_CTRL)

            self.centermouse()

            return self.passed(fname, "", True)

        except Exception, e:
            logging.exception('Exception (%s): %s' % (fname, e.message))
            case.showinfo(case.ERROR, 'Exception: %s' % e.message)
            return self.failed(fname, e.message, True)

        finally:
            case.showinfo(level, '%s: Returned from %s' % (datetime.datetime.now(), fname))

    def closetab(self, showdebug=False):
        """
        :param showdebug:
        :type showdebug: bool
        :return:
        :rtype: bool

        Close a tab

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        level = case.INFO if showdebug else case.DEBUG
        case.showinfo(level, '%s: Entered %s' % (datetime.datetime.now(), fname))

        try:
            if str(self.osname) == 'MAC':
                type("w", KEY_CMD)
            else:
                type("w", KEY_CTRL)

            return self.passed(fname, "", True)

        except Exception, e:
            logging.exception('Exception (%s): %s' % (fname, e.message))
            case.showinfo(case.ERROR, 'Exception: %s' % e.message)
            return self.failed(fname, e.message, True)

        finally:
            case.showinfo(level, '%s: Returned from %s' % (datetime.datetime.now(), fname))

    def navigateto(self, url='', showdebug=False):
        """
        :param url: url to navigate to
        :type url: str
        :param showdebug: show debug information
        :type showdebug: bool
        :return:
        :rtype: bool

        Navigate to a url

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        level = case.INFO if showdebug else case.DEBUG
        case.showinfo(level, '%s: Entered %s' % (datetime.datetime.now(), fname))

        try:
            if url != '':
                paste(url)
                return self.passed(fname, url, True)
            else:
                return self.failed(fname, '', True)

        except Exception, e:
            logging.exception('Exception (%s): %s' % (fname, e.message))
            case.showinfo(case.ERROR, 'Exception: %s' % e.message)
            return self.failed(fname, e.message, True)

        finally:
            case.showinfo(level, '%s: Returned from %s' % (datetime.datetime.now(), fname))

    def enterkey(self, key='', showdebug=False):
        """
        :param key: key to type
        :type key: str
        :param showdebug: show debug information
        :type showdebug: bool
        :return:
        :rtype: bool

        Type a specific key

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        level = case.INFO if showdebug else case.DEBUG
        case.showinfo(level, '%s: Entered %s' % (datetime.datetime.now(), fname))

        try:
            type(key)
            return self.passed(fname, '', True)

        except Exception, e:
            logging.exception('Exception (%s): %s' % (fname, e.message))
            case.showinfo(case.ERROR, 'Exception: %s' % e.message)
            return self.failed(fname, e.message, True)

        finally:
            case.showinfo(level, '%s: Returned from %s' % (datetime.datetime.now(), fname))

    def pagestart(self, showdebug=False):
        """
        :param showdebug: show debug information
        :type showdebug: bool
        :return:
        :rtype: bool

        Goto page start

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        level = case.INFO if showdebug else case.DEBUG
        case.showinfo(level, '%s: Entered %s' % (datetime.datetime.now(), fname))

        try:
            if str(self.osname) == 'MAC':
                type(Key.UP, KEY_CMD)
            else:
                type(Key.HOME)
            return self.passed(fname, '', True)

        except Exception, e:
            logging.exception('Exception (%s): %s' % (fname, e.message))
            case.showinfo(case.ERROR, 'Exception: %s' % e.message)
            return self.failed(fname, e.message, True)

        finally:
            case.showinfo(level, '%s: Returned from %s' % (datetime.datetime.now(), fname))

    def pageend(self, showdebug=False):
        """
        :param showdebug: show debug information
        :type showdebug: bool
        :return:
        :rtype: bool

        Go to page end

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        level = case.INFO if showdebug else case.DEBUG
        case.showinfo(level, '%s: Entered %s' % (datetime.datetime.now(), fname))

        try:
            if str(self.osname) == 'MAC':
                type(Key.DOWN, KEY_CMD)
            else:
                type(Key.END)
            return self.passed(fname, '', True)

        except Exception, e:
            logging.exception('Exception (%s): %s' % (fname, e.message))
            case.showinfo(case.ERROR, 'Exception: %s' % e.message)
            return self.failed(fname, e.message, True)

        finally:
            case.showinfo(level, '%s: Returned from %s' % (datetime.datetime.now(), fname))

    def pageback(self, showdebug=False):
        """
        :rtype: bool
        :param showdebug: show debug information
        :type showdebug: bool
        :return:

        Go one page back

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        level = case.INFO if showdebug else case.DEBUG
        case.showinfo(level, '%s: Entered %s' % (datetime.datetime.now(), fname))

        try:
            type(Key.BACKSPACE)
            return self.passed(fname, '', True)

        except Exception, e:
            logging.exception('Exception (%s): %s' % (fname, e.message))
            case.showinfo(case.ERROR, 'Exception: %s' % e.message)
            return self.failed(fname, e.message, True)

        finally:
            case.showinfo(level, '%s: Returned from %s' % (datetime.datetime.now(), fname))

    def clearmouse(self, showdebug=False):
        """
        :rtype: bool

        Move the mouse to the top-left corner

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        level = case.INFO if showdebug else case.DEBUG
        case.showinfo(level, '%s: Entered %s' % (datetime.datetime.now(), fname))

        try:
            mouseMove(Location(0, 0))
            return self.passed(fname, '', True)

        except Exception, e:
            logging.exception('Exception (%s): %s' % (fname, e.message))
            case.showinfo(case.ERROR, 'Exception: %s' % e.message)
            return self.failed(fname, e.message, True)

        finally:
            case.showinfo(level, '%s: Returned from %s' % (datetime.datetime.now(), fname))

    def centermouse(self, showdebug=False):
        """
        :rtype: bool

        Move the mouse to the center of the screen

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        level = case.INFO if showdebug else case.DEBUG
        case.showinfo(level, '%s: Entered %s' % (datetime.datetime.now(), fname))

        try:
            mouseMove(Location(self.screenwidth / 2, self.screenheight / 2))
            return self.passed(fname, '', True)

        except Exception, e:
            logging.exception('Exception (%s): %s' % (fname, e.message))
            case.showinfo(case.ERROR, 'Exception: %s' % e.message)
            return self.failed(fname, e.message, True)

        finally:
            case.showinfo(level, '%s: Returned from %s' % (datetime.datetime.now(), fname))

    def waituntil(self, image, tstep=1, nmax=50, showdebug=False):
        """
        :param image: image to appear
        :type image: str
        :param tstep: how much time for the timeout in seconds
        :type tstep: int
        :param nmax: max tries
        :type nmax: int
        :param showdebug: show debug information
        :type showdebug: bool
        :return:
        :rtype: bool

        Wait until an image appears

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        level = case.INFO if showdebug else case.DEBUG
        case.showinfo(level, '%s: Entered %s (%s)' % (datetime.datetime.now(), fname, str(image)))

        try:
            r = Region(getScreen())
            for i in range(nmax):
                case.showinfo(level, 'i = ' + str(i))
                fr = r.exists(self.assets.getimage(image), tstep)
                if fr is not None:
                    # workaround, since highlight is not working on linux
                    if str(self.osname) == 'LINUX':
                        fr.hover()
                    else:
                        fr.highlight(1)

                    return self.passed(fname, image)

            return self.failed(fname, image)

        except Exception, e:
            logging.exception('Exception (%s): %s' % (fname, e.message))
            case.showinfo(case.ERROR, 'Exception: %s' % e.message)
            return self.failed(fname, e.message, True)

        except FindFailed:
            logging.exception('FindFailed (%s): %s' % (fname, image))
            case.showinfo(case.ERROR, 'FindFailed: %s' % image)
            return self.failed(fname, image, True)

        finally:
            case.showinfo(level, '%s: Returned from %s (%s)' % (datetime.datetime.now(), fname, str(image)))

    def checkifexists(self, image, regn=None, showdebug=False):
        """
        :param image: image to exist
        :type image: str
        :param regn: restrict region to look for the image
        :type regn: Region
        :param showdebug: show debug information
        :type showdebug: bool
        :return:
        :rtype: bool

        Check if an image exists

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        level = case.INFO if showdebug else case.DEBUG
        case.showinfo(level, '%s: Entered %s (%s)' % (datetime.datetime.now(), fname, str(image)))

        try:
            count = 0
            r = self.regions.getreg(regn) if regn is not None else Region(getScreen())
            while not r.exists(self.assets.getimage(image), 2):
                case.showinfo(level, str(datetime.datetime.now()) + ' ' + fname + ':Check failed:')
                if count <= 9:
                    if not r.exists(self.assets.getimage(image), 2):
                        case.showinfo(level, str(datetime.datetime.now()) + ' ' + fname + ':SPACE:' + str(count))
                        type(Key.SPACE)
                        count += 1
                else:
                    return self.failed(fname, image)

            fr = r.getLastMatch()
            # workaround, since highlight is not working on linux
            if str(self.osname) == 'LINUX':
                fr.hover()
            else:
                fr.highlight(1)

            return self.passed(fname, image)

        except Exception, e:
            logging.exception('Exception (%s): %s' % (fname, e.message))
            case.showinfo(case.ERROR, 'Exception: %s' % e.message)
            return self.failed(fname, e.message, True)

        except FindFailed:
            logging.exception('FindFailed (%s): %s' % (fname, image))
            case.showinfo(case.ERROR, 'FindFailed: %s' % image)
            return self.failed(fname, image, True)

        finally:
            case.showinfo(level, '%s: Returned from %s (%s)' % (datetime.datetime.now(), fname, str(image)))

    def hoverifexists(self, image, clearmouse=False, dx=0, dy=0, regn=None, showdebug=False):
        """
        :param image: image to hover over
        :type image: str
        :param clearmouse: clear mouse bevor hover
        :type clearmouse: bool
        :param dx:
        :type dx: int
        :param dy:
        :type dy: int
        :param regn: restrict region to look for the image
        :type regn: Region
        :param showdebug: show debug information
        :type showdebug: bool
        :return:
        :rtype: object

        Hover over an image

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        level = case.INFO if showdebug else case.DEBUG
        case.showinfo(level, '%s: Entered %s (%s)' % (datetime.datetime.now(), fname, str(image)))

        try:
            if clearmouse:
                self.clearmouse()

            count = 0
            r = self.regions.getreg(regn) if regn is not None else Region(getScreen())
            while not r.exists(self.assets.getimage(image), 2):
                case.showinfo(level, str(datetime.datetime.now()) + ' ' + fname + ':Check failed:')
                if count <= 9:
                    if not r.exists(self.assets.getimage(image), 2):
                        case.showinfo(level, str(datetime.datetime.now()) + ' ' + fname + ':SPACE:' + str(count))
                        type(Key.SPACE)
                        count += 1
                else:
                    return self.failed(fname, image)

            ret = r.hover(Pattern(self.assets.getimage(image)).targetOffset(dx, dy))

            if ret:
                case.showinfo(level, str(datetime.datetime.now()) + ' ' + fname + ':Check ok:')
                return self.passed(fname, image)
            else:
                case.showinfo(level, str(datetime.datetime.now()) + ' ' + fname + ':Check not ok:')
                return self.failed(fname, image)

        except Exception, e:
            logging.exception('Exception (%s): %s' % (fname, e.message))
            case.showinfo(case.ERROR, 'Exception: %s' % e.message)
            return self.failed(fname, e.message, True)

        except FindFailed:
            logging.exception('FindFailed (%s): %s' % (fname, image))
            case.showinfo(case.ERROR, 'FindFailed: %s' % image)
            return self.failed(fname, image, True)

        finally:
            case.showinfo(level, '%s: Returned from %s (%s)' % (datetime.datetime.now(), fname, str(image)))

    def clicklink(self, image, dx=0, dy=0, showdebug=False):
        """
        :param image: image to click
        :type image: str
        :param showdebug: show debug information
        :type showdebug: bool
        :return:
        :rtype: bool

        Click on an image

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        level = case.INFO if showdebug else case.DEBUG
        case.showinfo(level, '%s: Entered %s (%s)' % (datetime.datetime.now(), fname, str(image)))

        try:
            ret = click(Pattern(self.assets.getimage(image)).targetOffset(dx, dy))

            if ret:
                case.showinfo(level, str(datetime.datetime.now()) + ' ' + fname + ':Check ok:')
                return self.passed(fname, image)
            else:
                case.showinfo(level, str(datetime.datetime.now()) + ' ' + fname + ':Check not ok:')
                return self.failed(fname, image)

        except Exception, e:
            logging.exception('Exception (%s): %s' % (fname, e.message))
            case.showinfo(case.ERROR, 'Exception: %s' % e.message)
            return self.failed(fname, e.message, True)

        except FindFailed:
            logging.exception('FindFailed (%s): %s' % (fname, image))
            case.showinfo(case.ERROR, 'FindFailed: %s' % image)
            return self.failed(fname, image, True)

        finally:
            case.showinfo(level, '%s: Returned from %s (%s)' % (datetime.datetime.now(), fname, str(image)))
