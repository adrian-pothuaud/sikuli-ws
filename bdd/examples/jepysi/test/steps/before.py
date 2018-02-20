# noinspection PyUnresolvedReferences
from sikuli.Sikuli import *
from case import *


@given(u'I see the "chrome browser active"')
def step_impl(testcontext):
    asset = testcontext.assets["chrome browser active"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@given(u'I open a new browser tab')
def step_impl(testcontext):
    assert testcontext.browser.opentab(), testcontext.info


@given(u'I see the "browser url field"')
def step_impl(testcontext):
    asset = testcontext.assets["browser url field"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@when(u'I enter [url] into the "browser url field"')
def step_impl(testcontext):
    envurl = testcontext.environments[testcontext.environment]["url"]
    assert testcontext.browser.navigateto(envurl), testcontext.info


@when(u'I press the ENTER Key')
def step_impl(testcontext):
    assert testcontext.browser.enterkey(Key.ENTER), testcontext.info


@then(u'I should see the "JePySi title link"')
def step_impl(testcontext):
    asset = testcontext.assets["JePySi title link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info
