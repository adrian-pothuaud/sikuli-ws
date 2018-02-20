"""
Module:  runner

Author:  arjs.net

License: http://opensource.org/licenses/mit-license.html; year=2013,2014; copyright holders=arjs.net

Main module for the sikuli system
"""
from case import *
from addons import *


#logging.basicConfig(level=logging.DEBUG, stream=sys.stderr, format="%(message)s")
logging.basicConfig(level=logging.INFO, stream=sys.stderr, format="%(message)s")
log = logging.getLogger('runner')


def onexit(f):
    """
    :param f: Exit function
    :type f: function
    :return:
    :rtype: function

    Marker for the exit function
    """
    import atexit

    atexit.register(f)
    return f


@onexit
def goodbye():
    """
    :rtype: None

    Exit function
    """
    if case.stats is not None:
        case.showstats()

    if len(case.testcontext.undefined) > 0:
        case.showinfo(case.NORMAL, '-' * 75)
        case.testcontext.listundefined()

    if len(case.testcontext.unknown) > 0:
        case.showinfo(case.NORMAL, '-' * 75)
        case.testcontext.listunknown()

    case.showinfo(case.NORMAL, '=' * 75)
    exit(case.stats.featurefailed)


def main():
    """
    :rtype: None

    Main function

    :raise e:
    """
    fname = sys._getframe().f_code.co_name
    case.showinfo(case.DEBUG, 'Entered %s' % fname)

    try:
        if len(sys.argv) <= 1:
            raise EnvironmentError("Not enough parameters")

        if len(sys.argv) > 3:
            raise EnvironmentError("Too many parameters!")

        # set the environment
        case.testcontext.environment = sys.argv[1]
        if case.testcontext.environment not in ['LOCAL', 'DEV', 'STAGE', 'PROD']:
            raise EnvironmentError("Environment not allowed!")

        # set the features or feature file
        fileorpath = str(sys.argv[2]) if len(sys.argv) == 3 else ''
        if not os.path.exists(fileorpath):
            raise EnvironmentError("File or Path not found! (%s)" % fileorpath)

        # set the base path
        bpath = os.path.dirname(os.path.realpath(fileorpath))
        case.showinfo(case.DEBUG, 'Features dirname = %s' % bpath)
        if 'features' in bpath:
            idx = bpath.rindex('features')
            case.showinfo(case.DEBUG, 'Current features idx = %d' % idx)
            bpath = bpath[:idx]
        case.showinfo(case.DEBUG, 'Current features base dirname = %s' % bpath)

        # set the current sikuli path
        rpath = os.path.realpath(os.path.dirname('.'))
        case.showinfo(case.DEBUG, 'Current jepysi dirname = %s' % rpath)

        # Create a chrome browser
        case.testcontext.browser = Chrome(bpath, rpath)

        # import the steps
        stepimporter()

        # loop over the features
        featurelooper(fileorpath)

    except Exception, e:
        logging.exception('Exception (%s): %s' % (fname, e.message))
        case.showinfo(case.ERROR, 'Exception (%s): %s' % (fname, e.message))
        raise e

    finally:
        case.showinfo(case.DEBUG, 'Returned from %s' % fname)


def stepimporter():
    """
    :rtype: None

    Imports the steps for the test cases

    :raise Exception:
    """
    fname = sys._getframe().f_code.co_name
    case.showinfo(case.DEBUG, 'Entered %s' % fname)

    soi = datetime.datetime.now()

    try:
        for path, dirs, files in os.walk(case.testcontext.browser.spath):
            case.showinfo(case.DEBUG, 'Looping path = %s' % path)
            for stepfile in files:
                if not stepfile.endswith('.py'):
                    continue

                case.showinfo(case.DEBUG, 'Processing step file %s in %s' % (stepfile, path))

                if not path in sys.path:
                    case.showinfo(case.DEBUG, 'Adding path %s' % path)
                    sys.path.append(path)

                case.showinfo(case.INFO, 'Importing step file %s' % stepfile)
                __import__(stepfile.replace('.py', ''), path)

    except Exception, e:
        logging.exception('Exception (%s): %s' % (fname, e.message))
        case.showinfo(case.ERROR, 'Exception (%s): %s' % (fname, e.message))
        raise e

    finally:
        eoi = datetime.datetime.now()
        case.showinfo(case.NORMAL, 'Import Took: %s' % str(eoi - soi))
        case.showinfo(case.DEBUG, 'Returned from %s' % fname)


def featurelooper(fileorpath):
    """
    :param fileorpath: Feature or Features path
    :type fileorpath: str
    :rtype: None

    Loop over the features

    :raise EnvironmentError:
    """
    fname = sys._getframe().f_code.co_name
    case.showinfo(case.DEBUG, 'Entered %s' % fname)

    sor = datetime.datetime.now()

    try:
        rpath = os.path.realpath(fileorpath)
        if not os.path.exists(rpath):
            raise EnvironmentError('%s not found!' % rpath)

        isfile = os.path.isfile(fileorpath)
        isall = case.testcontext.browser.fpath == rpath
        case.showinfo(case.DEBUG, 'Real path: %s; All features: %s; Is file: %s' % (
            os.path.realpath(fileorpath), str(isall), str(isfile))
        )

        # loop over the feature folders
        for path, dirs, files in os.walk(case.testcontext.browser.fpath):
            case.showinfo(case.DEBUG, 'Looping path = %s' % path)
            for featurefile in sorted(files):
                case.showinfo(case.DEBUG, 'Checking file = %s' % featurefile)
                if not featurefile.endswith('.feature'):
                    case.showinfo(case.DEBUG, 'Skipping none feature file = %s' % featurefile)
                    continue

                # only one feature file
                if isfile:
                    if not featurefile.startswith('_'):
                        case.showinfo(case.DEBUG, 'Skipping none special feature file = ' + featurefile)
                        continue

                    case.showinfo(case.DEBUG, 'Valid special feature file %s in %s' % (featurefile, path))
                    if path not in rpath:
                        case.showinfo(
                            case.DEBUG, 'Skipping valid but not relevant special feature file = %s' % featurefile
                        )
                        continue

                    case.showinfo(case.DEBUG, 'Processing special feature file %s in %s' % (featurefile, path))
                    if processfeature(path, featurefile):
                        reportfeatureresults(isall, path, featurefile)
                elif isall:
                    case.showinfo(case.DEBUG, 'Processing (1) feature file %s in %s' % (featurefile, path))
                    if processfeature(path, featurefile):
                        reportfeatureresults(isall, path, featurefile)
                else:
                    if path not in rpath:
                        case.showinfo(
                            case.DEBUG, 'Skipping valid but not relevant feature file %s in %s' % (featurefile, path)
                        )
                        continue

                    if not os.path.exists(os.path.join(rpath, featurefile)) and not featurefile.startswith('_'):
                        case.showinfo(case.DEBUG, 'Skipping none existing feature file %s in %s' % (featurefile, rpath))
                        continue

                    case.showinfo(case.DEBUG, 'Processing (2) feature file %s in %s' % (featurefile, path))
                    if processfeature(path, featurefile):
                        reportfeatureresults(isall, path, featurefile)

            # only one feature file
            if isfile:
                if path.endswith(os.path.dirname(fileorpath)):
                    case.showinfo(case.DEBUG, 'Ending loop since file %s in %s was found.' % (fileorpath, path))
                    break
            else:
                if not isall and path.endswith(fileorpath):
                    case.showinfo(case.DEBUG, 'Ending loop since path %s in %s was found.' % (fileorpath, path))
                    break

        # only one feature file
        if isfile:
            path, featurefile = os.path.split(rpath)
            case.showinfo(case.DEBUG, 'Processing feature file %s in %s' % (featurefile, path))
            if processfeature(path, featurefile):
                reportfeatureresults(isall, path, featurefile)

    except Exception, e:
        logging.exception('Exception (%s): %s' % (fname, e.message))
        case.showinfo(case.ERROR, 'Exception (%s): %s' % (fname, e.message))
        exit(1)

    finally:
        eor = datetime.datetime.now()
        case.showinfo(case.NORMAL, 'Features Took: %s' % (str(eor - sor)))
        case.showinfo(case.DEBUG, 'Returned from %s' % fname)


def processfeature(path, featurefile):
    """
    :param path: Path to the featurefile
    :type path: str
    :param featurefile: File with the feature
    :type featurefile: str
    :return:
    :rtype: bool

    Process one feature

    :raise EnvironmentError:
    """
    fname = sys._getframe().f_code.co_name
    case.showinfo(case.DEBUG, 'Entered %s' % fname)

    execute = True
    feature = None
    scenariocount = 0
    scenarioskipped = 0
    sof = datetime.datetime.now()

    base = featurefile.replace('.feature', '')

    try:
        filename = os.path.join(path, featurefile)
        case.showinfo(case.DEBUG, 'Processing features in ' + str(filename))
        feature, scenarios, error = extract(filename)
        case.showinfo(case.DEBUG, 'Extracted features from ' + str(filename))
        if error:
            case.showinfo(case.DEBUG, 'Error! Bailing out from ' + fname)
            exit(1)

        if featurefile.startswith('_'):
            if feature:
                case.showinfo(case.DEBUG, 'Added extra feature "%s"' % feature.name)
                case.testcontext.features[feature.name] = feature
                if scenarios:
                    for scenario in scenarios:
                        case.showinfo(case.DEBUG, 'Added feature scenario %s' % scenario.name)
                        case.testcontext.features[feature.name].scenarios[scenario.name] = scenario
            else:
                if scenarios:
                    for s in scenarios:
                        case.showinfo(case.DEBUG, 'Added extra scenario %s' % s.name)
                        case.testcontext.extras[s.name] = s
            return

        case.showinfo(case.NORMAL, '=' * 75)
        case.showinfo(case.NORMAL, '# File: %s' % filename)
        case.showinfo(case.NORMAL, '-' * 75)

        if not feature:
            raise EnvironmentError('No feature found!')

        # clear the testsuite and reset some values
        case.testsuite.clear()
        case.testsuite.set('errors', '0')
        case.testsuite.set('failures', '0')
        case.testsuite.set('skipped', '0')
        case.testsuite.set('tests', '0')
        case.testsuite.set('time', '0.0')
        case.testsuite.set('name', base + '.' + feature.name.replace(' ', '_').replace('.', '_'))

        if stats.stepundefined > 0:
            execute = False
            raise EnvironmentError("Undefined steps. Cannot continue!")

        # check if all assets that are used are really defined
        if not assetsdefinedcheck(feature.scenarios.values()):
            execute = False
            return

        if scenarios and not assetsdefinedcheck(scenarios):
            execute = False
            return

        # check if all assets that are used are really defined
        if not constantsdefinedcheck(feature.scenarios.values()):
            execute = False
            return

        if scenarios and not constantsdefinedcheck(scenarios):
            execute = False
            return

        # execute the feature
        feature()

        if case.testcontext.setup:
            execute = case.testcontext.setup()
            scenariocount += 1

        if execute:
            if scenarios:
                for scenario in scenarios:
                    case.showinfo(case.DEBUG, 'Execute scenario %s' % scenario.name)
                    execute = scenario() and execute
                    case.showinfo(case.DEBUG, 'Finished scenario %s' % scenario.name)
                    if scenario.examples:
                        scenariocount += len(scenario.examples)
                    else:
                        scenariocount += 1

            if feature.scenarios:
                for scenario in feature.scenarios:
                    case.showinfo(case.DEBUG, 'Execute extra scenario %s' % scenario)
                    execute = feature.scenarios[scenario]() and execute
                    case.showinfo(case.DEBUG, 'Finished extra scenario %s' % scenario)
                    if feature.scenarios[scenario].examples:
                        scenariocount += len(feature.scenarios[scenario].examples)
                    else:
                        scenariocount += 1
        else:
            if scenarios:
                for scenario in scenarios:
                    case.showinfo(case.DEBUG, 'Execute scenario %s' % scenario.name)
                    execute = scenario(execute) and execute
                    case.showinfo(case.DEBUG, 'Finished scenario %s' % scenario.name)
                    if scenario.examples:
                        case.stats.scenarioskipped += len(scenario.examples)
                        scenariocount += len(scenario.examples)
                        scenarioskipped += len(scenario.examples)
                    else:
                        case.stats.scenarioskipped += 1
                        scenariocount += 1
                        scenarioskipped += 1

                    case.showinfo(case.NORMAL, ' ')

            if feature.scenarios:
                for scenario in feature.scenarios:
                    case.showinfo(case.DEBUG, 'Execute extra scenario %s' % scenario)
                    execute = feature.scenarios[scenario](execute) and execute
                    case.showinfo(case.DEBUG, 'Finished extra scenario %s' % scenario)
                    if feature.scenarios[scenario].examples:
                        case.stats.scenarioskipped += len(feature.scenarios[scenario].examples)
                        scenariocount += len(feature.scenarios[scenario].examples)
                        scenarioskipped += len(feature.scenarios[scenario].examples)
                    else:
                        case.stats.scenarioskipped += 1
                        scenariocount += 1
                        scenarioskipped += 1

                    case.showinfo(case.NORMAL, ' ')

        if case.testcontext.cleanup:
            execute = case.testcontext.cleanup() and execute
            scenariocount += 1

        if execute:
            case.stats.featurepassed += 1
        else:
            case.stats.featurefailed += 1

    except Exception, e:
        if feature:
            case.stats.featurefailed += 1

        #logging.exception('Exception (%s): %s' % (fname, e.message))
        case.showinfo(case.ERROR, 'Exception (%s): %s' % (fname, e.message))

    finally:
        doreport = feature and not featurefile.startswith('_')
        if doreport:
            eof = datetime.datetime.now()

            if execute:
                case.showinfo(case.PASSED, 'Feature Took: %s' % (str(eof - sof)))
            else:
                case.showinfo(case.FAILED, 'Feature Took: %s' % (str(eof - sof)))

            case.stats.featureprocessed += 1

            case.testsuite.set('time', case.calculatems(str(eof - sof)))
            case.testsuite.set('tests', str(scenariocount))
            case.testsuite.set('skipped', str(scenarioskipped))

        case.showinfo(case.DEBUG, 'Returned from %s' % fname)
        return doreport


def reportfeatureresults(isall, path, featurefile):
    """
    :param isall: Flag if to create a more detailed folder structure
    :type isall: bool
    :param path: PAth to the reports
    :type path: str
    :param featurefile: Feature file name
    :type featurefile: str
    :rtype: None

    Write the test report to the report folder depending on the kind of test
    """
    fname = sys._getframe().f_code.co_name
    case.showinfo(case.DEBUG, 'Entered %s' % fname)

    try:
        if isall:
            reportspath = path.replace('features', 'reports')
        else:
            reportspath = case.testcontext.browser.reports

        if not os.path.exists(reportspath):
            os.makedirs(reportspath)

        case.writereport(os.path.join(reportspath, 'TESTS-%s.xml' % featurefile))

    except Exception, e:
        logging.exception('Exception (%s): %s' % (fname, e.message))
        case.showinfo(case.ERROR, 'Exception (%s): %s' % (fname, e.message))

    finally:
        case.showinfo(case.DEBUG, 'Returned from %s' % fname)


def assetsdefinedcheck(scenarios):
    """
    :param scenarios: Scenario to check for assets
    :type scenarios: []
    :rtype: bool

    Check if used assets are defined
    """
    fname = sys._getframe().f_code.co_name
    case.showinfo(case.DEBUG, 'Entered %s' % fname)

    fail = False

    try:
        checkassets = []
        for scenario in scenarios:
            if scenario.before:
                extractusedassets(checkassets, scenario.before.given)
                extractusedassets(checkassets, scenario.before.when)
                extractusedassets(checkassets, scenario.before.then)

            extractusedassets(checkassets, scenario.given)
            extractusedassets(checkassets, scenario.when)
            extractusedassets(checkassets, scenario.then)

            if scenario.after:
                extractusedassets(checkassets, scenario.after.given)
                extractusedassets(checkassets, scenario.after.when)
                extractusedassets(checkassets, scenario.after.then)

        for ca in checkassets:
            case.showinfo(case.DEBUG, "Check Asset '%s'..." % ca)
            if '<' in ca and '>' in ca:
                continue

            if '#' in ca:
                ca = replaceconstants(ca).strip()

            #print ca
            #print testcontext.assets.keys()
            #print case.testcontext.browser.assets.imgdict.values()
            if ca not in testcontext.assets.keys():
                case.showinfo(case.ERROR, "Asset definition '%s' not found!" % ca)
                case.testcontext.appendunknown(ca, '?')
                fail = True
            elif testcontext.assets[ca] not in case.testcontext.browser.assets.imgdict.values():
                case.showinfo(case.ERROR, "Asset '%s' not found!" % ca)
                case.testcontext.appendunknown(ca, '?')
                fail = True

        if fail:
            raise EnvironmentError("Missing assets. Cannot continue!")

    except Exception, e:
        fail = True
        if scenarios:
            case.stats.featurefailed += 1

        #logging.exception('Exception (%s): %s' % (fname, e.message))
        case.showinfo(case.ERROR, 'Exception (%s): %s' % (fname, e.message))

    finally:
        case.showinfo(case.DEBUG, 'Returned from %s' % fname)
        return not fail


def extractusedassets(checkassets, possibleassets):
    """
    :param checkassets: Assets to check
    :type checkassets: []
    :param possibleassets: Possible assets
    :type possibleassets: []
    :rtype: None

    Extract the assets from the current used steps
    """
    fname = sys._getframe().f_code.co_name
    case.showinfo(case.DEBUG, 'Entered %s' % fname)

    try:
        if possibleassets:
            for s in possibleassets:
                m = reAsset.match(s.name)
                if m:
                    asset = m.group(1)
                    case.showinfo(case.DEBUG, "Asset: %s" % asset)
                    if asset not in checkassets:
                        checkassets.append(asset)

    finally:
        case.showinfo(case.DEBUG, 'Returned from %s' % fname)


def constantsdefinedcheck(scenarios):
    """
    :param scenarios: Scenario to check for constants
    :type scenarios: []
    :rtype: bool

    Check if used constantes are defined
    """
    fname = sys._getframe().f_code.co_name
    case.showinfo(case.DEBUG, 'Entered %s' % fname)

    fail = False

    try:
        checkconstants = []
        for scenario in scenarios:
            if scenario.before:
                extractusedconstants(checkconstants, scenario.before.given)
                extractusedconstants(checkconstants, scenario.before.when)
                extractusedconstants(checkconstants, scenario.before.then)

            extractusedconstants(checkconstants, scenario.given)
            extractusedconstants(checkconstants, scenario.when)
            extractusedconstants(checkconstants, scenario.then)

            if scenario.after:
                extractusedconstants(checkconstants, scenario.after.given)
                extractusedconstants(checkconstants, scenario.after.when)
                extractusedconstants(checkconstants, scenario.after.then)

        for cc in checkconstants:
            if cc not in testcontext.constants.keys():
                case.showinfo(case.WARNING, "Constant '%s' not found!" % cc)
                fail = True

        if fail:
            raise EnvironmentError("Missing constants. Cannot continue!")

    except Exception, e:
        fail = True
        if scenarios:
            case.stats.featurefailed += 1

        #logging.exception('Exception (%s): %s' % (fname, e.message))
        case.showinfo(case.ERROR, 'Exception (%s): %s' % (fname, e.message))

    finally:
        case.showinfo(case.DEBUG, 'Returned from %s' % fname)
        return not fail


def extractusedconstants(checkconstants, possibleconstants):
    """
    :param checkconstants: Constants to check
    :type checkconstants: []
    :param possibleconstants: Possible constants
    :type possibleconstants: []
    :rtype: None

    Extract the constants from the current used steps
    """
    fname = sys._getframe().f_code.co_name
    case.showinfo(case.DEBUG, 'Entered %s' % fname)

    try:
        if possibleconstants:
            for s in possibleconstants:
                m = reConstant.match(s.name)
                if m:
                    constant = m.group(1)
                    case.showinfo(case.DEBUG, "Constant: %s" % constant)
                    if constant not in checkconstants:
                        checkconstants.append(constant)

    finally:
        case.showinfo(case.DEBUG, 'Returned from %s' % fname)


def extract(filename):
    """
    :param filename: Feature file
    :type filename: str
    :return:
    :rtype: tuple

    Extract the feature details from the feature file
    """
    fname = sys._getframe().f_code.co_name
    case.showinfo(case.DEBUG, 'Entered %s' % fname)

    error = False
    skiplines = False
    scenarios = []
    columns = []
    state = ''
    feature = None
    co = None   # current object
    eh = False  # example header
    before = case.testcontext.before
    after = case.testcontext.after

    try:
        finput = open(filename)

        while True:
            line = finput.readline()
            case.showinfo(case.DEBUG, ':' + line)
            if not line:
                break

            # skip multiline comments
            if line.startswith('#*'):
                skiplines = True
                continue

            # skip multiline comments
            if line.startswith('*#'):
                skiplines = False
                continue

            # skip till multiline comment is done
            if skiplines:
                continue

            # skip comments
            if line.startswith('#'):
                continue

            m = reEmptyLine.match(line)
            if m:
                state = ''
                co = None
                eh = True
                continue

            m = reVariable.match(line)
            if m:
                case.showinfo(case.DEBUG, '### Found a variable.')
                case.showinfo(case.DEBUG, (' ' * 4) + m.group(1))

            if state == 'feature':
                case.showinfo(case.DEBUG, '### Found a feature description.')
                case.showinfo(case.DEBUG, (' ' * 4) + line[:-1].strip())
                if co:
                    co.description.append(line[:-1].strip())

                continue

            if state == 'examples':
                case.showinfo(case.DEBUG, '### Found an example table entry.')
                if eh:
                    columns = line.split('|')[1:-1]
                    eh = False
                else:
                    row = {}
                    values = line.split('|')[1:-1]
                    for i in range(0, len(values)):
                        row[columns[i].strip()] = values[i].strip()

                    if co:
                        co.examples.append(row)

                continue

            if state == 'assets':
                case.showinfo(case.DEBUG, '### Found an asset entry.')
                m = reAssetLine.match(line)
                if not m:
                    continue

                assetname = str(m.group(1))
                asset = str(m.group(2))
                case.showinfo(case.DEBUG, 'Key	: %s, Value: %s' % (assetname, asset))
                if '|' in line:
                    marker = case.testcontext.browser.osspecificimagesfolder
                    case.showinfo(case.DEBUG, 'Marker: %s' % marker)

                    asset = ''
                    choices = m.group(2).split('|')
                    case.showinfo(case.DEBUG, 'Choices: %s' % str(choices))
                    for choice in choices:
                        if choice.strip().startswith(marker):
                            asset = choice
                            break

                    if not asset:
                        raise EnvironmentError("No valid choice for special image folder!")

                    asset = asset.replace(marker, '').strip()
                    case.showinfo(case.DEBUG, 'asset: %s' % asset)

                case.testcontext.assets[assetname] = asset
                stats.imagestotal += 1

                if ('<' in assetname and '>' in assetname) or '#' in assetname:
                    continue
                elif asset not in case.testcontext.browser.assets.imgdict.values():
                    case.showinfo(case.WARNING, "Asset not found: '%s'" % assetname)
                    case.testcontext.appendunknown(assetname, asset)

                continue

            if state == 'environments':
                case.showinfo(case.DEBUG, '### Found an environment entry.')
                m = reEnvironmentLine.match(line)
                if not m:
                    continue

                case.showinfo(case.DEBUG, 'Env	: %s' % m.group(1))
                case.showinfo(case.DEBUG, 'Key	: %s' % m.group(2))
                case.showinfo(case.DEBUG, 'Value: %s' % m.group(3))
                case.testcontext.appendenvironment(m.group(2).strip(), m.group(3).strip(), m.group(1).strip())
                continue

            if state == 'constants':
                case.showinfo(case.DEBUG, '### Found an constant entry.')
                m = reConstantLine.match(line)
                if not m:
                    continue

                case.showinfo(case.DEBUG, 'Key	: %s' % m.group(1))
                case.showinfo(case.DEBUG, 'Value: %s' % m.group(2))
                case.testcontext.constants[m.group(1).strip()] = m.group(2).strip()
                continue

            m = reFeature.match(line)
            if m:
                if feature:
                    raise EnvironmentError('"Feature" already used.')

                case.showinfo(case.DEBUG, '### Found a feature.')
                case.showinfo(case.DEBUG, (' ' * 4) + m.group(1))
                state = 'feature'
                name = m.group(1) if m.group(1) != '' else 'Feature'
                co = Feature(name)
                feature = co
                continue

            m = reExtraFeature.match(line)
            if m:
                if feature:
                    raise EnvironmentError('"Extra Feature" already used.')

                case.showinfo(case.DEBUG, '### Found an extra feature.')
                case.showinfo(case.DEBUG, (' ' * 4) + m.group(1))
                state = 'extra feature'
                if not case.testcontext.features:
                    raise EnvironmentError("No extra features found!")

                if m.group(1) not in case.testcontext.features:
                    raise EnvironmentError("No extra feature with name '%s' found" % (m.group(1)))

                feature = case.testcontext.features[m.group(1)]
                continue

            m = reSetup.match(line)
            if m:
                case.showinfo(case.DEBUG, '### Found a setup.')
                case.showinfo(case.DEBUG, (' ' * 4) + m.group(1))
                state = 'setup'
                name = m.group(1) if m.group(1) != '' else 'Setup scenario'
                co = case.Setup(name)
                case.testcontext.setup = co
                continue

            m = reCleanup.match(line)
            if m:
                case.showinfo(case.DEBUG, '### Found a cleanup.')
                case.showinfo(case.DEBUG, (' ' * 4) + m.group(1))
                state = 'cleanup'
                name = m.group(1) if m.group(1) != '' else 'Cleanup scenario'
                co = case.Cleanup(name)
                case.testcontext.cleanup = co
                continue

            m = reBefore.match(line)
            if m:
                case.showinfo(case.DEBUG, '### Found a before scenario.')
                case.showinfo(case.DEBUG, (' ' * 4) + m.group(1))
                state = 'before'
                name = m.group(1) if m.group(1) != '' else 'Before scenario'
                co = case.Before(name)
                before = co
                case.testcontext.before = before
                continue

            m = reAfter.match(line)
            if m:
                case.showinfo(case.DEBUG, '### Found a after scenario.')
                case.showinfo(case.DEBUG, (' ' * 4) + m.group(1))
                state = 'after'
                name = m.group(1) if m.group(1) != '' else 'After scenario'
                co = case.After(name)
                after = co
                case.testcontext.after = after
                continue

            m = reScenarioOutline.match(line)
            if m:
                case.showinfo(case.DEBUG, '### Found a scenario outline.')
                case.showinfo(case.DEBUG, (' ' * 4) + m.group(1))
                state = 'scenario outline'
                name = m.group(1) if m.group(1) != '' else 'Outline scenario'
                co = case.Scenario(name)
                scenarios.append(co)
                if before:
                    co.before = before

                if after:
                    co.after = after

                continue

            m = reScenario.match(line)
            if m:
                case.showinfo(case.DEBUG, '### Found a scenario.')
                case.showinfo(case.DEBUG, (' ' * 4) + m.group(1))
                state = 'scenario'
                name = m.group(1) if m.group(1) != '' else 'Scenario'
                co = case.Scenario(name)
                scenarios.append(co)
                if before:
                    co.before = before

                if after:
                    co.after = after

                continue

            m = reExtraScenario.match(line)
            if m:
                case.showinfo(case.DEBUG, '### Found an extra scenario.')
                case.showinfo(case.DEBUG, (' ' * 4) + m.group(1))
                state = 'extra scenario'
                if not case.testcontext.extras:
                    raise EnvironmentError("No extra scenarios found!")

                if m.group(1) not in case.testcontext.extras:
                    raise EnvironmentError("No extra scenario with name '%s' found" % (m.group(1)))

                co = case.testcontext.extras[m.group(1)]
                scenarios.append(co)
                if before:
                    co.before = before

                if after:
                    co.after = after

                continue

            m = reExamples.match(line)
            if m:
                case.showinfo(case.DEBUG, '### Found examples.')
                case.showinfo(case.DEBUG, (' ' * 4) + m.group(1))
                state = 'examples'
                if scenarios:
                    co = scenarios[-1]

                continue

            m = reGiven.match(line)
            if m:
                step = str(m.group(1))
                case.showinfo(case.DEBUG, '### Found a given.')
                case.showinfo(case.DEBUG, (' ' * 4) + step)
                state = 'given'
                if co:
                    co.given.append(case.Given(step))

                if step not in case.testcontext.gfunctions.keys():
                    case.showinfo(case.WARNING, 'given step not found: %s' % step)
                    case.testcontext.appendundefined(step, state)

                continue

            m = reWhen.match(line)
            if m:
                step = str(m.group(1))
                case.showinfo(case.DEBUG, '### Found a when.')
                case.showinfo(case.DEBUG, (' ' * 4) + step)
                state = 'when'
                if co:
                    co.when.append(case.When(step))

                if step not in case.testcontext.wfunctions.keys():
                    case.showinfo(case.WARNING, 'when step not found: %s' % step)
                    case.testcontext.appendundefined(step, state)

                continue

            m = reThen.match(line)
            if m:
                step = str(m.group(1))
                case.showinfo(case.DEBUG, '### Found a then.')
                case.showinfo(case.DEBUG, (' ' * 4) + step)
                state = 'then'
                if co:
                    co.then.append(case.Then(step))

                if step not in case.testcontext.tfunctions.keys():
                    case.showinfo(case.WARNING, 'then step not found: %s' % step)
                    case.testcontext.appendundefined(step, state)

                continue

            m = reAnd.match(line)
            if m:
                step = str(m.group(1))
                if state == 'given':
                    case.showinfo(case.DEBUG, '### Found a given and.')
                    case.showinfo(case.DEBUG, (' ' * 4) + step)
                    state = 'given'
                    if co:
                        co.given.append(case.Given(step))

                    if step not in case.testcontext.gfunctions.keys():
                        case.showinfo(case.WARNING, 'given step not found: %s' % step)
                        case.testcontext.appendundefined(step, state)

                    continue

                if state == 'when':
                    case.showinfo(case.DEBUG, '### Found a when and.')
                    case.showinfo(case.DEBUG, (' ' * 4) + step)
                    state = 'when'
                    if co:
                        co.when.append(case.When(step))

                    if step not in case.testcontext.wfunctions.keys():
                        case.showinfo(case.WARNING, 'when step not found: %s' % step)
                        case.testcontext.appendundefined(step, state)

                    continue

                if state == 'then':
                    case.showinfo(case.DEBUG, '### Found a then and.')
                    case.showinfo(case.DEBUG, (' ' * 4) + step)
                    state = 'then'
                    if co:
                        co.then.append(case.Then(step))

                    if step not in case.testcontext.tfunctions.keys():
                        case.showinfo(case.WARNING, 'then step not found: %s' % step)
                        case.testcontext.appendundefined(step, state)

                    continue

            m = reAssets.match(line)
            if m:
                state = 'assets'
                continue

            m = reEnvironments.match(line)
            if m:
                state = 'environments'
                continue

            m = reConstants.match(line)
            if m:
                state = 'constants'
                continue

            case.showinfo(case.NORMAL, '--- (' + state + ') ' + line[:-1])

    except Exception, e:
        logging.exception('Exception (%s): %s' % (fname, e.message))
        case.showinfo(case.ERROR, 'Exception (%s): %s' % (fname, e.message))
        error = True

    finally:
        case.showinfo(case.DEBUG, 'Returned from %s' % fname)
        return feature, scenarios, error


if __name__ == '__main__':
    # set some regular expressions
    reEmptyLine = re.compile('^$')
    reFeature = re.compile('^Feature:\s+(.*)$')
    reExtraFeature = re.compile('^Extra Feature:\s+(.*)$')
    reSetup = re.compile('^Setup:\s+(.*)$')
    reCleanup = re.compile('^Cleanup:\s+(.*)$')
    reBefore = re.compile('^Before:\s+(.*)$')
    reAfter = re.compile('^After:\s+(.*)$')
    reAsset = re.compile('.*\"(.*)\".*')
    reAssets = re.compile('^Assets:\s+(.*)$')
    reAssetLine = re.compile('^\s+"(.*)"\s*=\s*(.*)\s+$')
    reEnvironments = re.compile('^Environments:\s+(.*)$')
    reEnvironmentLine = re.compile('^\s+(.*)\s*:\s+(.*)\s*=\s*(.*)\s+$')
    reConstant = re.compile('.*#(.*)#.*')
    reConstants = re.compile('^Constants:\s+(.*)$')
    reConstantLine = re.compile('^\s+(.*)\s*=\s*(.*)\s+$')
    reScenario = re.compile('^Scenario:\s+(.*)$')
    reScenarioOutline = re.compile('^Scenario Outline:\s+(.*)$')
    reExtraScenario = re.compile('^Extra Scenario:\s+(.*)$')
    reVariable = re.compile('.*<(.*)>.*')
    reExamples = re.compile('^Examples:\s+(.*)$')
    reExampleEntry = re.compile('\s+\|\s*(.*)\s*\|\s*$')
    reGiven = re.compile('\s+Given\s+(.*)$')
    reWhen = re.compile('\s+When\s+(.*)$')
    reThen = re.compile('\s+Then\s+(.*)$')
    reAnd = re.compile('\s+And\s+(.*)$')

    # execute the main function
    main()
