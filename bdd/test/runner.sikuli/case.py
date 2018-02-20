"""
Module:  case

Author:  arjs.net

License: http://opensource.org/licenses/mit-license.html; year=2013,2014; copyright holders=arjs.net

Module for test case
"""
import re
import os
import sys
import logging
import datetime
import xml.etree.cElementTree as elementTree

import cdata
import counts
import context

#logging.basicConfig(level=logging.INFO, stream=sys.stderr, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, stream=sys.stderr, format="%(message)s")
log = logging.getLogger('case')

# codes for the showinfo function
TITLE = 0
ERROR = 1
PASSED = 2
FAILED = 3
SKIP = 4
DEBUG = 5
NORMAL = 6
INFO = 7
WARNING = 8

# create testsuite for junit reports and set some elements
testsuite = elementTree.Element("testsuite")
testsuite.set('disabled', 'False')
testsuite.set('errors', '0')
testsuite.set('failures', '0')
testsuite.set('name', '')
testsuite.set('skipped', '0')
testsuite.set('tests', '0')
testsuite.set('time', '0.0')
testsuite.set('timestamp', '')
testsuite.set('package', '')
testsuite.set('id', '')
testsuite.set('hostname', '')

stats = counts.Counts()

testcontext = context.Context(stats)


class Case(object):
    """Case: Base for Feature, Sequence and Step classes"""

    def __init__(self, name):
        """
        :param name: Name of the Case
        :type name: str
        :rtype: object
        """
        self.description = []
        self.name = name


class Feature(Case):
    """Feature: Class for all feature specific things"""

    def __init__(self, name):
        """
        :param name: Name of the feature
        :type name: str
        :rtype: Feature
        """
        super(Feature, self).__init__(name)
        self.scenarios = {}
        stats.featuretotal += 1

    def __call__(self):
        """
        :rtype: None

        Execute the objects standard tasks

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        showinfo(DEBUG, 'Entered feature %s' % fname)

        try:
            showinfo(TITLE, self.__class__.__name__ + ': ' + replaceconstants(replaceenvironments(self.name)))
            if self.description:
                for description in self.description:
                    showinfo(NORMAL, replaceconstants(replaceenvironments(description)), ' ' * 9)

        except Exception, e:
            showinfo(ERROR, 'Exception (%s): %s' % (self.__class__.__name__, e.message))
            raise e

        finally:
            showinfo(NORMAL, '-' * 75)
            showinfo(DEBUG, 'Returned feature from %s' % fname)


class Sequence(Case):
    """Sequence: Base Class for all sequence related classes"""

    def __init__(self, name):
        """
        :param name: Name of the sequence
        :type name: str
        :rtype: Sequence
        """
        super(Sequence, self).__init__(name)
        self.given = []
        self.when = []
        self.then = []
        self.examples = []
        self.before = None
        self.after = None
        self.type = self.__class__.__name__
        self.special = self.type == 'Before' or self.type == 'After'
        if not self.special:
            stats.scenariototal += 1

    def __call__(self, execute=True):
        """
        :param execute: Specifies if the sequence should be skipped
        :type execute: bool
        :return:
        :rtype: None

        Execute the objects standard tasks
        """
        fname = sys._getframe().f_code.co_name
        showinfo(DEBUG, 'Entered sequence %s (%s)' % (fname, self.type))

        if not self.special:
            if self.examples:
                stats.scenarioprocessed += len(self.examples)
            else:
                stats.scenarioprocessed += 1

        try:
            if not execute:
                showinfo(SKIP, '%s: %s' % (self.type, self.name), ' ' * 2)
                testcase = elementTree.SubElement(testsuite, "testcase")
                testcase.set('classname', testsuite.attrib['name'])
                testcase.set('name', self.name)
                testcase.set('status', 'skipped')
                testcase.set('time', '0.0')
                testcase.set('assertions', '0')
                elementTree.SubElement(testcase, "skipped")
                elementTree.SubElement(testcase, "system-out")

            else:
                if self.examples:
                    first = True
                    if not self.special:
                        showinfo(TITLE, '%s Outline: %s' % (self.type, self.name), ' ' * 2)

                    for example in self.examples:
                        execute = self.handlesequence(execute, example, first)

                        if first:
                            first = False

                else:
                    execute = self.handlesequence(execute, None, True)

        except Exception, e:
            stats.scenariofailed += 1
            testsuite.set('errors', str(stats.scenariofailed))
            showinfo(ERROR, 'Exception (%s): %s' % (self.__class__.__name__, e.message))
            logging.exception('Exception (%s): %s' % (self.__class__.__name__, e.message))
            execute = False

        finally:
            testsuite.set('failures', str(stats.scenariofailed))
            testsuite.set('skipped', str(stats.scenarioskipped))
            testsuite.set('tests', str(stats.scenariototal))

            showinfo(DEBUG, 'Returned from sequence %s (%s)' % (fname, self.type))
            return execute

    def handlesequence(self, execute, example, first):
        """
        :param execute: Execute or Skip
        :type execute: bool
        :param example: Example array in case of an outline scenario
        :type example: []
        :param first: Signals if it is the first execution
        :type first: bool
        :rtype: bool

        Helper method to execute a sequence
        """

        title = replaceconstants(self.name)
        prefix = "Outline: " if example else ""
        output = "%s%s (%s)" if example else "%s%s"
        tupleinfo = (prefix, title, str(example)) if example else (prefix, title)

        if not self.special:
            testcontext.browser.starttimer()
            testcase = elementTree.SubElement(testsuite, "testcase")
            testcase.set('classname', testsuite.attrib['name'])
            testcase.set('status', '')
            testcase.set('time', '0.0')
            testcase.set('assertions', '0')

            if example:
                testcase.set('name', '%s (%s)' % (title, str(example)))
            else:
                testcase.set('name', title)

            if not execute:
                showinfo(SKIP, output % tupleinfo, ' ' * 2)
            else:
                showinfo(TITLE, output % tupleinfo, ' ' * 2)
        else:
            testcase = None

            if not execute:
                showinfo(SKIP, output % tupleinfo, ' ' * 4)
            else:
                showinfo(TITLE, output % tupleinfo, ' ' * 4)

        message = ''
        systemout = []

        if execute and self.before:
            message = self.before.type + ': ' + self.before.name
            sosb = datetime.datetime.now()
            execute = self.before(execute)
            eosb = datetime.datetime.now()

            if not execute:
                message += ' ... failed'
            else:
                message += ' ... passed'

            systemout.append(message + ' in ' + str(eosb - sosb))
            message = 'Before steps'

            if execute:
                showinfo(TITLE, '%s: ' % self.type, ' ' * 4)

        if execute:
            for step in self.given:
                message = step.name
                step.values = example
                execute = step(execute, systemout)
                if not execute:
                    break

        if execute:
            for step in self.when:
                message = step.name
                step.values = example
                execute = step(execute, systemout)
                if not execute:
                    break

        if execute:
            for step in self.then:
                message = step.name
                step.values = example
                execute = step(execute, systemout)
                if not execute:
                    break

        if execute and self.after:
            message = self.after.type + ': ' + self.after.name
            sosa = datetime.datetime.now()
            execute = self.after(execute)
            eosa = datetime.datetime.now()
            if not execute:
                message += ' ... failed'
            else:
                message += ' ... passed'

            systemout.append(message + ' in ' + str(eosa - sosa))
            message = 'After steps'

        if not self.special:
            testcontext.browser.stoptimer()
            testcase.set('time', str(calculatems(str(testcontext.browser.timerdiff))))

            if execute:
                stats.scenariopassed += 1
                testcase.set('status', 'passed')
            else:
                if first:
                    stats.scenariofailed += 1
                    testcase.set('status', 'failed')
                    subelement = elementTree.SubElement(testcase, "failure")
                    if message:
                        message += ' failed'

                    subelement.set('message', message)
                    subelement.set('type', 'failure')
                else:
                    stats.scenarioskipped += 1
                    testcase.set('status', 'skipped')
                    elementTree.SubElement(testcase, "skipped")

            testsystemout = elementTree.SubElement(testcase, "system-out")
            if systemout:
                line = '\n@scenario.begin\n'
                line += '  %s: %s\n' % (self.type, title)
                for info in systemout:
                    line += ' ' * 4 + info + '\n'
                line += '@scenario.end\n'
                line += '-' * 75 + '\n'
                testsystemout.append(cdata.cdata(line))

            showinfo(INFO, 'Scenario Took: ' + testcontext.browser.timerdiff, ' ' * 4)
            showinfo(INFO, ' ')

        return execute


class Setup(Sequence):
    """Setup: Setup sequence; runs before all steps"""

    def __init__(self, name):
        """
        :param name: Name of the sequence
        :type name: str
        :rtype: Setup
        """
        super(Setup, self).__init__(name)


class Cleanup(Sequence):
    """Cleanup: Cleanup sequence; runs after all steps"""

    def __init__(self, name):
        """
        :param name: Name of the sequence
        :type name: str
        :rtype: Cleanup
        """
        super(Cleanup, self).__init__(name)


class Before(Sequence):
    """Before: Before sequence; runs before each scenario; except Setup and Cleanup"""

    def __init__(self, name):
        """
        :param name: Name of the sequence
        :type name: str
        :rtype: Before
        """
        super(Before, self).__init__(name)


class After(Sequence):
    """After: After sequence; runs after each scenario; except Setup and Cleanup"""

    def __init__(self, name):
        """
        :param name: Name of the sequence
        :type name: str
        :rtype: After
        """
        super(After, self).__init__(name)


class Scenario(Sequence):
    """Scenario: Scenario sequence; runs the actual scenario"""

    def __init__(self, name):
        """
        :param name: Name of the sequence
        :type name: str
        :rtype: Scenario
        """
        super(Scenario, self).__init__(name)


class Step(Case):
    """Step: Base class for the actual steps"""

    def __init__(self, name, values=None):
        """
        :param name: Name of the step
        :type name: str
        :param values: The actual values for an outline scenario
        :type values: {}
        :rtype: Step
        """
        super(Step, self).__init__(name)
        self.values = values if values else {}

    def __call__(self, execute=True, systemout=None):
        """
        :param execute: Execute of skip
        :type execute: bool
        :param systemout: Array for the output information
        :type systemout: []
        :return:
        :rtype: bool

        Execute the objects standard tasks

        :raise Exception:
        """
        fname = sys._getframe().f_code.co_name
        showinfo(DEBUG, 'Entered step %s (%s)' % (fname, self.name))

        info = ''
        retvalue = execute
        sos = datetime.datetime.now()

        try:
            info = self.name

            # replace variables
            if self.values:
                info = replacevariables(info, self.values)

            # replace environments
            info = replaceenvironments(info)

            # replace constants
            info = replaceconstants(info)

            testcontext.info = self.__class__.__name__
            testcontext.example = self.values
            if testcontext.info == 'Given':
                testfunctions = testcontext.gfunctions
            elif testcontext.info == 'When':
                testfunctions = testcontext.wfunctions
            elif testcontext.info == 'Then':
                testfunctions = testcontext.tfunctions
            else:
                raise EnvironmentError("No functions defined.")

            testcontext.info += ': ' + info
            if self.name in testfunctions:
                showinfo(DEBUG, 'testfunction %s from %s' % (self.name, str(testfunctions[self.name])))
                if execute:
                    testfunctions[self.name](testcontext)
                    eos = datetime.datetime.now()
                    showinfo(PASSED, '%s ... passed in %s' % (testcontext.info, str(eos - sos)), ' ' * 4)
                    systemout.append('%s ... passed in %s' % (testcontext.info, str(eos - sos)))
                    stats.steppassed += 1
                else:
                    eos = datetime.datetime.now()
                    showinfo(SKIP, '%s ... skipped in %s' % (testcontext.info, str(eos - sos)), ' ' * 4)
                    systemout.append('%s ... skipped in %s' % (testcontext.info, str(eos - sos)))
                    stats.stepskipped += 1
            else:
                testcontext.appendundefined(self.name, self.__class__.__name__)
                assert False, 'Undefined: %s: %s' % (self.__class__.__name__, self.name)

        except AssertionError, e:
            eos = datetime.datetime.now()
            stats.stepfailed += 1
            showinfo(FAILED, '%s ... failed in %s' % (e.message, str(eos - sos)), ' ' * 4)
            systemout.append('%s ... failed in %s' % (testcontext.info, str(eos - sos)))
            retvalue = False

        except Exception, e:
            eos = datetime.datetime.now()
            stats.stepfailed += 1
            showinfo(ERROR, 'Exception: %s: %s - %s' % (self.__class__.__name__, info, str(e.message)), ' ' * 4)
            systemout.append(testcontext.info + ' ... error in ' + str(eos - sos))
            retvalue = False
            raise e

        finally:
            showinfo(DEBUG, 'Returned from step %s (%s)' % (fname, self.name))
            stats.stepprocessed += 1
            return retvalue


class Given(Step):
    """Given: Given step"""

    def __init__(self, name, values=None):
        """
        :param name: Name of the step
        :type name: str
        :param values: Values for the outline
        :type values: {}
        :rtype: Then
        """
        values = values if values else {}
        super(Given, self).__init__(name, values)


class When(Step):
    """When: When step"""

    def __init__(self, name, values=None):
        """
        :param name: Name of the step
        :type name: str
        :param values: Values for the outline
        :type values: {}
        :rtype: Then
        """
        values = values if values else {}
        super(When, self).__init__(name, values)


class Then(Step):
    """Then: Then step"""

    def __init__(self, name, values=None):
        """
        :param name: Name of the step
        :type name: str
        :param values: Values for the outline
        :type values: {}
        :rtype: Then
        """
        values = values if values else {}
        super(Then, self).__init__(name, values)


def given(text):
    """
    :param text: Name of the actual step
    :type text: str
    :return:
    :rtype: function

    Marker for a given implementation
    """
    def register(f):
        """
        :param f:
        :type f: function
        :return:
        :rtype: function

        Register the implementation function
        """
        if text in testcontext.gfunctions.keys():
            stats.stepskipped += 1
            showinfo(ERROR, 'ignored given %s for \"%s\"' % (str(f.__name__), str(text)))
        else:
            testcontext.gfunctions[text] = f
            stats.steptotal += 1
            showinfo(DEBUG, 'registered given %s for \"%s\"' % (str(f.__name__), str(text)))

        return f

    return register


def when(text):
    """
    :param text: Name of the actual step
    :type text: str
    :return:
    :rtype: function

    Marker for a when implementation
    """
    def register(f):
        """
        :param f:
        :type f: function
        :return:
        :rtype: function

        Register the implementation function
        """
        if text in testcontext.wfunctions.keys():
            stats.stepskipped += 1
            showinfo(ERROR, 'ignored when %s for \"%s\"' % (str(f.__name__), str(text)))
        else:
            testcontext.wfunctions[text] = f
            stats.steptotal += 1
            showinfo(DEBUG, 'registered when %s for \"%s\"' % (str(f.__name__), str(text)))

        return f

    return register


def then(text):
    """
    :param text: Name of the actual step
    :type text: str
    :return:
    :rtype: function

    Marker for a then implementation
    """
    def register(f):
        """
        :param f:
        :type f: function
        :return:
        :rtype: function

        Register the implementation function
        """
        if text in testcontext.tfunctions.keys():
            stats.stepskipped += 1
            showinfo(ERROR, 'ignored then %s for \"%s\"' % (str(f.__name__), str(text)))
        else:
            testcontext.tfunctions[text] = f
            stats.steptotal += 1
            showinfo(DEBUG, 'registered then %s for \"%s\"' % (str(f.__name__), str(text)))

        return f

    return register


def replacevariables(line, values):
    """
    :param line: Line with variables
    :type line: str
    :param values:
    :type values: []
    :rtype: str

    Replace variables within a line
    """
    revariables = re.findall('<([^<>]+)>', line)
    if not revariables:
        return line

    for variable in revariables:
        line = line.replace('<' + variable + '>', values[variable])

    return line


def replaceenvironments(line):
    """
    :param line: Line with environment value
    :type line: str
    :rtype: str

    Replace an environment value within a line
    """
    reenv = re.findall('\[([^\[\]]+)\]', line)
    if not reenv:
        return line

    for variable in reenv:
        line = line.replace('[' + variable + ']', testcontext.environments[testcontext.environment][variable])

    return line


def replaceconstants(line):
    """
    :param line: Line with constants
    :type line: str
    :rtype: str

    Replace constants within a line
    """
    reconsts = re.findall('#([^#]+)#', line)
    if not reconsts:
        return line

    for variable in reconsts:
        line = line.replace('#' + variable + '#', testcontext.constants[variable])

    return line


def writereport(filename):
    """
    :param filename: junit report filename
    :type filename: str
    :rtype: None

    Write the junit report
    """
    tree = cdata.ElementTreeCDATA(testsuite)
    tree.write(filename, 'UTF-8')


def showstats():
    """
    :rtype: None

    Outputs the statistics
    """
    if stats is not None:
        showinfo(NORMAL, ' ')
        showinfo(
            NORMAL,
            '%d loaded steps, %d processed, %d passed, %d failed, %d skipped, %d undefined' %
            stats.getstepstuple()
        )
        showinfo(
            NORMAL,
            '%d loaded scenarios, %d processed, %d passed, %d failed, %d skipped' %
            stats.getscenariotuple()
        )
        showinfo(
            NORMAL,
            '%d loaded features, %d processed, %d passed, %d failed' %
            stats.getfeaturetuple()
        )
        showinfo(
            NORMAL,
            '%d loaded assets, %d unknown' %
            stats.getimagestuple()
        )


def calculatems(timediff):
    """
    :param timediff:
    :type timediff: str
    :return:
    :rtype: str

    Returns a string with the miliseconds
    """
    h, m, s = (['0', '0'] + timediff.split(':'))[-3:]
    if '.' in s:
        s, ms = s.split('.')
    else:
        ms = '0'

    ms = round(
        float(
            (3600000 * int(h) + 60000 * int(m) + 1000 * float(s) + round(float(ms) / 1000)) / 1000
        ), 2
    )

    return str(ms)


def showinfo(color, text, indent=''):
    """
    :param color: Color code
    :type color: int
    :param text: Text to display
    :type text: str
    :param indent: Indent to use
    :type indent: str
    :rtype: None

    Outputs a color coded, if possible, string of information
    """
    info = text.strip()
    ignorecolor = False

    if hasattr(testcontext, 'browser') and testcontext.browser:
        ignorecolor = testcontext.browser.ignorecolor

    if os.getenv('OS') and 'Win' in os.getenv('OS'):
        ignorecolor = True

    if os.getenv('JENKINS_HOME'):
        ignorecolor = True

    colorcode = indent
    if ignorecolor:
        if color == ERROR:
            colorcode += 'ERROR: '
        elif color == SKIP:
            colorcode += 'SKIPPED: '
        elif color == PASSED:
            colorcode += 'PASSED: '
        elif color == FAILED:
            colorcode += 'FAILED: '
        elif color == DEBUG:
            colorcode += 'DEBUG: '
        elif color == WARNING:
            colorcode += 'WARNING: '
    else:
        info += '\033[0m'
        if color == ERROR:
            colorcode += '\033[91mERROR: '
        elif color == SKIP:
            colorcode += '\033[95mSKIPPED: \033[0m'
        elif color == TITLE:
            colorcode += '\033[94m'
        elif color == PASSED:
            colorcode += '\033[92mPASSED: \033[0m'
        elif color == FAILED:
            colorcode += '\033[91mFAILED: \033[0m'
        elif color == NORMAL:
            colorcode += '\033[0m'
        elif color == INFO:
            colorcode += '\033[0m'
        elif color == WARNING:
            colorcode += '\033[93mWARNING: \033[0m'
        else:
            colorcode = '\033[0mDEBUG: '

    if color == DEBUG:
        log.debug(colorcode + info)
    else:
        log.info(colorcode + info)
