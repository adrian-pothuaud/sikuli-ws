from sikuli.Sikuli import *
from case import *

@then(u'I should see the "Navigation" on the left')
def step_impl(testcontext):
    asset = testcontext.assets["Navigation"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see the "JePySi Welcome" title')
def step_impl(testcontext):
    asset = testcontext.assets["JePySi Welcome"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see the "JePySi doc link"')
def step_impl(testcontext):
    asset = testcontext.assets["JePySi doc link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@given(u'I have an open a browser')
def step_impl(testcontext):
    assert testcontext.browser.open(), testcontext.info


@then(u'I should see the "Top Navigation" on the left top')
def step_impl(testcontext):
    asset = testcontext.assets["Top Navigation"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@when(u'I enter the [url] in a new tab')
def step_impl(testcontext):
    assert testcontext.browser.opentab(), testcontext.info
    envurl = testcontext.environments[testcontext.environment]["url"]
    assert testcontext.browser.navigateto(envurl), testcontext.info
    assert testcontext.browser.enterkey(Key.ENTER), testcontext.info
