# noinspection PyUnresolvedReferences
from sikuli.Sikuli import *
from case import *


@given(u'I goto the page end')
def step_impl(testcontext):
    assert testcontext.browser.pageend(), testcontext.info


@when(u'I go to the page end')
def step_impl(testcontext):
    assert testcontext.browser.pageend(), testcontext.info
