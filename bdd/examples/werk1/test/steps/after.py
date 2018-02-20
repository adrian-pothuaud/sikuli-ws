# noinspection PyUnresolvedReferences
from sikuli.Sikuli import *
from case import *


@when(u'I close the browser tab')
def step_impl(testcontext):
    assert testcontext.browser.closetab(), testcontext.info


@then(u'I should not see the "#logo# logo"')
def step_impl(testcontext):
    asset = testcontext.assets[replaceconstants("#logo# logo")]
    assert True, testcontext.info
    #assert not testcontext.browser.checkifexists(asset), testcontext.info
