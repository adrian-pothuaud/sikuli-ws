"""
Module:  counts

Author:  arjs.net

License: http://opensource.org/licenses/mit-license.html; year=2013,2014; copyright holders=arjs.net

Module for counts
"""


class Counts(object):
    """Counts: Keeps track of all important counts"""

    def __init__(self):
        """
        :rtype: Counts
        """
        super(Counts, self).__init__()
        self.imagestotal = 0
        self.imagesunknown = 0
        self.steptotal = 0
        self.steppassed = 0
        self.stepfailed = 0
        self.stepskipped = 0
        self.stepprocessed = 0
        self.stepundefined = 0
        self.scenariototal = 0
        self.scenariopassed = 0
        self.scenariofailed = 0
        self.scenarioskipped = 0
        self.scenarioprocessed = 0
        self.featuretotal = 0
        self.featurepassed = 0
        self.featurefailed = 0
        self.featureprocessed = 0

    def getstepstuple(self):
        """
        :param self:
        :return:
        :rtype: tuple

        Returns the steps counts tuple
        """
        return (
            self.steptotal, self.stepprocessed, self.steppassed, self.stepfailed, self.stepskipped, self.stepundefined
        )

    def getscenariotuple(self):
        """
        :param self:
        :return:
        :rtype: tuple

        Returns the scenacrio counts tuple
        """
        return \
            self.scenariototal, self.scenarioprocessed, self.scenariopassed, self.scenariofailed, self.scenarioskipped

    def getfeaturetuple(self):
        """
        :param self:
        :return:
        :rtype: tuple

        Returns the feature counts tuple
        """
        return self.featuretotal, self.featureprocessed, self.featurepassed, self.featurefailed

    def getimagestuple(self):
        """
        :param self:
        :return:
        :rtype: tuple

        Returns the images counts tuple
        """
        return self.imagestotal, self.imagesunknown
