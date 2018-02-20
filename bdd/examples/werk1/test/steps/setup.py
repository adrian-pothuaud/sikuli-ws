# noinspection PyUnresolvedReferences
from sikuli.Sikuli import *
from case import *


@given(u'I open a chrome browser')
def step_impl(testcontext):
    assert testcontext.browser.open(), testcontext.info


@then(u'I see the "chrome browser active"')
def step_impl(testcontext):
    asset = testcontext.assets["chrome browser active"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see "browser url field"')
def step_impl(testcontext):
    asset = testcontext.assets["browser url field"]
    assert testcontext.browser.checkifexists(asset), testcontext.info
