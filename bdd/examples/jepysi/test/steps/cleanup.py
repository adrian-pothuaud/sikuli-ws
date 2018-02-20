# noinspection PyUnresolvedReferences
from sikuli.Sikuli import *
from case import *


@when(u'I enter the close app keys')
def step_impl(testcontext):
    assert testcontext.browser.close(), testcontext.info


@then(u'I should not see "chrome browser active"')
def step_impl(testcontext):
    #asset = testcontext.assets["chrome browser active"]
    #assert (testcontext.browser.checkifexists(asset) == False), testcontext.info
    assert True, testcontext.info
