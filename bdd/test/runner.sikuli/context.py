"""
Module:  context

Author:  arjs.net

License: http://opensource.org/licenses/mit-license.html; year=2013,2014; copyright holders=arjs.net

Module for the test context
"""
import re
import logging

log = logging.getLogger('context')


class Context(object):
    """Context: Holds the context information for the tests"""

    def __init__(self, stats):
        """
        :param stats: Counts object
        :type stats: Counts
        :rtype: Context
        """
        super(Context, self).__init__()
        self.stats = stats
        self.browser = None
        self.info = ''
        self.before = None
        self.after = None
        self.setup = None
        self.cleanup = None
        self.extras = {}
        self.assets = {}
        self.features = {}
        self.example = None
        self.undefined = {}
        self.unknown = {}
        self.environment = 'DEV'
        self.environments = {}
        self.constants = {}
        self.gfunctions = {}
        self.wfunctions = {}
        self.tfunctions = {}

    def appendundefined(self, key, value):
        """
        :type value: object
        :type key: str
        :param key:
        :param value:
        :return:
        :rtype: None

        Append an undefined step to a list
        """
        if key in self.undefined.keys():
            return

        self.undefined[key] = value
        self.stats.stepundefined += 1

    def listundefined(self):
        """
        :rtype: None

        Outputs the list of undefined steps
        """
        for item in self.undefined.keys():
            log.info("@%s(u'%s')" % (str(self.undefined[item]).lower(), str(item)))
            log.info("def step_impl(testcontext):")
            reassets = re.findall('\s*"(.*)"\s*', str(item))
            if reassets:
                if len(reassets) > 1:
                    count = 0
                    for asset in reassets:
                        count += 1
                        log.info("\tasset%d = context.assets[\"%s\"]" % (count, asset))
                else:
                    log.info("\tasset = testcontext.assets[\"%s\"]" % (reassets[0]))

            log.info("\tassert testcontext.browser.failed(testcontext.info, asset), testcontext.info")
            log.info("\n")

    def appendenvironment(self, key, value, env=''):
        """
        :param key: key to use
        :type key: str
        :param value: Value to set
        :type value: object
        :param env: Environment key
        :type env: object
        :rtype: None

        Appends an environment
        """
        if env == '':
            env = self.environment

        if key not in self.environments.keys():
            self.environments[env] = {}

        if key not in self.environments[env].keys():
            self.environments[env][key] = None

        self.environments[env][key] = value

    def getenvironmentvalue(self, key, env=''):
        """
        :param key: Key to use
        :type key: str
        :param env: Environment to return
        :type env: object
        :return:
        :rtype: object

        Returns the environment values
        """
        if env == '':
            env = self.environment

        if key not in self.environments:
            return None

        if key not in self.environments[env]:
            return None

        return self.environments[env][key]

    def appendunknown(self, key, value):
        """
        :type value: object
        :type key: str
        :param key:
        :param value:
        :return:
        :rtype: None

        Append an undefined images to a list
        """
        if key in self.unknown.keys():
            return

        self.unknown[key] = value
        self.stats.imagesunknown += 1

    def listunknown(self):
        """
        :rtype: None

        Outputs the list of undefined images
        """
        for item in self.unknown.keys():
            log.info('"%s" = %s' % (str(item), str(self.unknown[item])))
