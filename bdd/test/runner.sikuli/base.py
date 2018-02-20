"""
Module:  base

Author:  arjs.net

License: http://opensource.org/licenses/mit-license.html; year=2013,2014; copyright holders=arjs.net

Module for the test base
"""
import datetime
import shutil
import sys
import ConfigParser

# noinspection PyUnresolvedReferences
from sikuli.Sikuli import *
from image import *
from region import *


#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
log = logging.getLogger('base')


# noinspection PyUnresolvedReferences
class Base(object):
    """Base: Some basic stuff for handling the tests"""

    def __init__(self, bpath, rpath):
        """
        :param bpath: Test base path
        :type bpath: str
        :param rpath: Runner base path
        :type rpath: str
        :rtype: Base
        :raise EnvironmentError:
        """
        super(Base, self).__init__()

        # set os and os version
        self.osname = Env.getOS()
        self.osversion = Env.getOSVersion()

        # workaround for the linux OS detection problem
        if '-generic' in self.osversion:
            self.osname = 'LINUX'

        if str(self.osname) == 'WINDOWS':
            self.osspecificimagesfolder = 'win/'
        elif str(self.osname) == 'LINUX':
            self.osspecificimagesfolder = 'linux/'
        elif str(self.osname) == 'MAC':
            self.osspecificimagesfolder = 'mac/'
        else:
            raise EnvironmentError("Unknown OS environment!")

        # init the variables which are set by the config file(s)
        self.findfailedcounter = 0
        self.findfailedlimit = 0
        self.openwaittime = 0
        self.doopenwait = False
        self.doswitchapp = False
        self.showactions = False
        self.ignorecolor = False
        self.additionaltab = False
        self.usetimestampforscreenshots = False
        self.site = ""
        self.chrome = ""
        self.firefox = ""
        self.ie = ""
        self.dateformatstring = ""

        # set the sikuli base path
        self.rpath = rpath
        log.debug('Current sikuli base dirname = %s' % self.rpath)
        if not self.rpath in sys.path:
            sys.path.append(self.rpath)

        # noinspection PyUnresolvedReferences
        self.rspath = os.path.realpath(getBundlePath())
        log.debug('Current sikuli runner dirname = %s' % self.rspath)
        if not self.rspath in sys.path:
            sys.path.append(self.rspath)

        # set the base path
        self.bpath = bpath

        # set the test path
        self.tpath = bpath
        log.debug('Current test dirname = %s' % self.tpath)

        # set the feature path
        self.fpath = os.path.join(self.tpath, 'features')
        log.debug('Current features dirname = %s' % self.fpath)
        if not os.path.exists(self.fpath):
            raise EnvironmentError("File or Path not found! (%s)" % self.fpath)

        # set the steps path
        self.spath = os.path.join(self.tpath, 'steps')
        log.debug('Current steps dirname = %s' % self.spath)
        if not os.path.exists(self.spath):
            raise EnvironmentError("File or Path not found! (%s)" % self.spath)

        # set the images path
        self.ipath = os.path.join(self.tpath, 'images')
        log.debug('Current images dirname = %s' % self.ipath)
        if not os.path.exists(self.ipath):
            raise EnvironmentError("File or Path not found! (%s)" % self.ipath)

        # read the config file and get the variables
        config = ConfigParser.RawConfigParser()
        configfile = os.path.join(self.tpath, os.path.join('config', 'config.txt'))
        if os.path.exists(configfile):
            self.processconfig(config, configfile)
        else:
            raise EnvironmentError("Config file '%s' not found!!!\n" % configfile)

        # read environment specific values
        configfile = os.path.join(self.tpath, os.path.join(os.path.join('config', str(self.osname)), 'config.txt'))
        if os.path.exists(configfile):
            self.processconfig(config, configfile)

        # create new junit reports directory
        self.reports = os.path.join(self.tpath, 'reports')
        if not os.path.exists(self.reports):
            createdirectory(self.reports)

        # create new logs directory
        self.logsfolder = os.path.join(self.tpath, 'logs')
        if self.usetimestampforscreenshots:
            self.logsfolder = os.path.join(self.logsfolder, self.timestamp)

        # create log path if not exists
        if not os.path.exists(self.logsfolder):
            createdirectory(self.logsfolder)

        # set csv file and screenshot path
        self.csvpath = os.path.join(self.logsfolder, "logFile.txt")
        self.screenshotpath = self.logsfolder

        # set default csv delimiter
        self.delim = ","

        # init timers
        self.startoftimer = ""
        self.endoftimer = ""

        # init screen size with current screen
        self.screenwidth = getScreen().getW()
        self.screenheight = getScreen().getH()

        # get region dictionary
        self.regions = RegionDictionary(self.screenwidth, self.screenheight)

        # get images dictionary
        self.assets = ImagesDictionary(self.ipath, self.osspecificimagesfolder)

        # set sikuli defaults
        setShowActions(self.showactions)

    def processconfig(self, config, configfile):
        """
        :param config: Configparser object
        :type config: ConfigParser.RawConfigParser
        :param configfile: file with configs
        :type configfile: str
        :rtype: None

        Process the config values from a config file

        """
        logging.debug('configfile: %s' % configfile)
        config.read(configfile)

        # grab each variable seperately
        if checkconfigvalue(config, "vars", "failCount"):
            self.findfailedcounter = int(config.get("vars", "failCount"))

        if checkconfigvalue(config, "vars", "failLimit"):
            self.findfailedlimit = int(config.get("vars", "failLimit"))

        if checkconfigvalue(config, "vars", "dateFormat"):
            self.dateformatstring = config.get("vars", "dateFormat")

        if checkconfigvalue(config, "vars", "iePath"):
            self.ie = config.get("vars", "iePath")

        if checkconfigvalue(config, "vars", "firefoxPath"):
            self.firefox = config.get("vars", "firefoxPath")

        if checkconfigvalue(config, "vars", "chromePath"):
            self.chrome = config.get("vars", "chromePath")

        if checkconfigvalue(config, "vars", "site"):
            self.site = config.get("vars", "site")

        if checkconfigvalue(config, "vars", "useTimeStampForScreenShots"):
            self.usetimestampforscreenshots = bool(config.get('vars', 'useTimeStampForScreenShots') == 'True')

        if checkconfigvalue(config, "vars", "additionalTab"):
            self.additionaltab = bool(config.get('vars', 'additionalTab') == 'True')

        if checkconfigvalue(config, "vars", "ignoreColor"):
            self.ignorecolor = bool(config.get('vars', 'ignoreColor') == 'True')

        if checkconfigvalue(config, "vars", "showActions"):
            self.showactions = bool(config.get('vars', 'showActions') == 'True')

        if checkconfigvalue(config, "vars", "doOpenWait"):
            self.doopenwait = bool(config.get('vars', 'doOpenWait') == 'True')

        if checkconfigvalue(config, "vars", "openWaitTime"):
            self.openwaittime = int(config.get('vars', 'openWaitTime'))

        if checkconfigvalue(config, "vars", "doSwitchApp"):
            self.doswitchapp = bool(config.get('vars', 'doSwitchApp') == 'True')

    def criticalerror(self, test):
        """
        :param test: Test name
        :type test: str
        :rtype: None

        Terminate the test when an error is too critical to continue

        """
        # if findFailedCounter equals findFailedLimit the handlefindfailed method terminates the test
        self.findfailedcounter = self.findfailedlimit

        # terminate the test
        self.handlefindfailed(test)

    def handlefindfailed(self, test):
        """
        :param test: Test name
        :type test: str
        :rtype: bool

        Determine whether or not to terminate the test after an error

        :raise SystemExit:
        """
        if self.findfailedcounter < self.findfailedlimit:
            self.findfailedcounter += 1
        else:
            raise SystemExit("Critical Error(s) have occurred @ test (%s) Script is stopping." % test)

    def passed(self, test, comment="", skipcapture=False):
        """
        :param test: Test name
        :type test: str
        :param comment: Optional comment
        :type comment: str
        :param skipcapture: Optional screenshot
        :type skipcapture: bool
        :return:
        :rtype: bool

        Pass the test and do an optional screenshot

        """
        try:
            status = "PASSED"

            stamp = datetime.datetime.now().strftime(self.dateformatstring)
            if not skipcapture:
                self.takescreenshot(status, stamp)

            self.writecsvfile(comment, stamp, status, test)

        finally:
            return True

    def failed(self, test, comment="", skipcapture=False):
        """
        :param test: Test name
        :type test: str
        :param comment: Optional comment
        :type comment: str
        :param skipcapture: Optional screenshot
        :type skipcapture: bool
        :return:
        :rtype: bool

        Fail the test and take an optional screenshot

        """
        try:
            status = "FAILED"

            stamp = datetime.datetime.now().strftime(self.dateformatstring)
            if not skipcapture:
                self.takescreenshot(status, stamp)

            self.writecsvfile(comment, stamp, status, test)

            self.handlefindfailed(test)

        finally:
            return False

    def takescreenshot(self, status, stamp):
        """
        :param status: Status to add
        :type status: str
        :param stamp: Timestamp to add
        :type stamp: str
        :rtype: None

        Takes a screenshot of the entire screen

        """
        # take screenshot
        shot = capture(Region(0, 0, self.screenwidth, self.screenheight))

        # create the file's name
        filename = stamp + "." + status + ".png"

        # create the path to save the screenshot
        targetpath = os.path.join(self.screenshotpath, filename)

        # save the screenshot to the specified directory
        shutil.move(shot, targetpath)

    def writecsvfile(self, comment, stamp, status, test):
        """
        :param comment: Comment
        :type comment: str
        :param stamp: Timestamp
        :type stamp: str
        :param status: Status
        :type status: str
        :param test: Test name
        :type test: str
        :rtype: None

        Write the log string to the csv file

        """
        info = stamp + self.delim + status + self.delim + self.site + self.delim + test + self.delim \
            + comment + "\n"

        logfile = open(self.csvpath, 'a')
        logfile.write(info)
        logfile.close()

    def starttimer(self):
        """
        :rtype: None

        Set the current start time

        """
        self.startoftimer = datetime.datetime.now()

    def stoptimer(self):
        """
        :rtype: None

        Set the current end time

        """
        self.endoftimer = datetime.datetime.now()

    @property
    def timerdiff(self):
        """
        :rtype: str
        :return:

        Return the difference of the timers

        """
        return str(self.endoftimer - self.startoftimer)

    @property
    def timestamp(self):
        """
        :rtype: str
        :return:

        Get a timestamp

        """
        return datetime.datetime.now().strftime(self.dateformatstring)


def createdirectory(path):
    """
    :param path: path to create
    :type path: str
    :rtype: object

    Create a path

    """
    os.makedirs(path)
    if not os.path.exists(path):
        raise EnvironmentError("Path (%s) couldn't be created!" % path)


def checkconfigvalue(config, section, name):
    """
    :param config: Configparser object
    :type config: ConfigParser.RawConfigParser
    :param section: Section name
    :type section: str
    :param name: Config name
    :type name: str
    :return:
    :rtype: bool

    Check if a config name in a section exists

    """
    if not config.has_section(section):
        return False

    if not config.has_option(section, name):
        return False

    logging.debug('(%s : %s : "%s")' % (section, name, config.get(section, name)))
    return True
