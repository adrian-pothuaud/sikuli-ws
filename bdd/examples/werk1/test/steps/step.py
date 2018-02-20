# noinspection PyUnresolvedReferences
from sikuli.Sikuli import *
from case import *


@given(u'I see a "social menu"')
def step_impl(testcontext):
    asset = testcontext.assets["social menu"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@given(u'I should see the "imprint link" at the page end')
def step_impl(testcontext):
    assert testcontext.browser.pageend(), testcontext.info
    asset = testcontext.assets["imprint link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@given(u'I see a "top menu"')
def step_impl(testcontext):
    asset = testcontext.assets["top menu"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see the "Imprint title" block')
def step_impl(testcontext):
    asset = testcontext.assets["Imprint title"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@given(u'I see the "#logo# logo" at the top')
def step_impl(testcontext):
    assert testcontext.browser.pagestart(), testcontext.info
    asset = testcontext.assets[replaceconstants("#logo# logo")]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see the "#logo# logo" block')
def step_impl(testcontext):
    asset = testcontext.assets["Werk1 logo"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see the "Address text" block')
def step_impl(testcontext):
    asset = testcontext.assets["Address text"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@when(u'I click the "imprint link"')
def step_impl(testcontext):
    asset = testcontext.assets["imprint link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info
    assert testcontext.browser.clicklink(asset), testcontext.info

##

@then(u'I should see the "<submenu> submenu" block')
def step_impl(testcontext):
    asset = testcontext.assets[replacevariables("<submenu> submenu", testcontext.example)]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@when(u'I hover the "<menu> item"')
def step_impl(testcontext):
    asset = testcontext.assets[replacevariables("<menu> item", testcontext.example)]
    assert testcontext.browser.hoverifexists(asset), testcontext.info

##

@then(u'I should be able to hover over the "<items>" submenu items and see it highlighted')
def step_impl(testcontext):
    showinfo(
        NORMAL,
        replacevariables('Processing: I should be able to hover over the "<items>" submenu items...', testcontext.example),
        4 * ' '
    )
    elements = testcontext.example['items'].split(',')
    for element in elements:
        showinfo(NORMAL, '... Processing item: "%s"' % element.strip(), 6 * ' ')
        asset = testcontext.assets["<items>"]
        asset = asset.replace(":item:", element.strip())
        assert testcontext.browser.hoverifexists(asset), testcontext.info
        asset = testcontext.assets["highlighted <items>"]
        asset = asset.replace(":item:", element.strip())
        assert testcontext.browser.checkifexists(asset), testcontext.info

##

@then(u'I should be able to see the "<page>" title after 5s')
def step_impl(testcontext):
    asset = replacevariables(testcontext.assets["<page>"], testcontext.example)
    wait(5)
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should be able to click the "<item>" submenu')
def step_impl(testcontext):
    asset = replacevariables(testcontext.assets["<item>"], testcontext.example)
    assert testcontext.browser.clicklink(asset), testcontext.info

##

@then(u'I should see the "#logo# logo" after 1s')
def step_impl(testcontext):
    asset = testcontext.assets[replaceconstants("#logo# logo")]
    wait(1)
    assert testcontext.browser.checkifexists(asset), testcontext.info


@given(u'I see the "#logo# logo"')
def step_impl(testcontext):
    asset = testcontext.assets[replaceconstants("#logo# logo")]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@when(u'I click the "#logo# logo"')
def step_impl(testcontext):
    asset = testcontext.assets[replaceconstants("#logo# logo")]
    assert testcontext.browser.clicklink(asset), testcontext.info


@then(u'I should see "footer" block at the page end')
def step_impl(testcontext):
    asset = testcontext.assets["footer"]
    testcontext.browser.pageend()
    assert testcontext.browser.checkifexists(asset), testcontext.info


@given(u'I see a "facebook like" logo at the page end')
def step_impl(testcontext):
    asset = testcontext.assets["facebook like"]
    testcontext.browser.pageend()
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should be able to hover over the "facebook like" logo')
def step_impl(testcontext):
    asset = testcontext.assets["facebook like"]
    assert testcontext.browser.hoverifexists(asset), testcontext.info


@given(u'I see a "hotspot link"')
def step_impl(testcontext):
    asset = testcontext.assets["hotspot link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should be able to hover over the "hotspot link"')
def step_impl(testcontext):
    asset = testcontext.assets["hotspot link"]
    assert testcontext.browser.hoverifexists(asset), testcontext.info


@then(u'I should see the "imprint title" block after 1s')
def step_impl(testcontext):
    asset = testcontext.assets["imprint title"]
    wait(1)
    assert testcontext.browser.checkifexists(asset), testcontext.info


@given(u'I see the "bottom menu" block at the page end')
def step_impl(testcontext):
    asset = testcontext.assets["bottom menu"]
    testcontext.browser.pageend()
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should be able to hover over the "facebook logo" link')
def step_impl(testcontext):
    asset = testcontext.assets["facebook logo"]
    assert testcontext.browser.hoverifexists(asset), testcontext.info


@given(u'I see the "social menu" block')
def step_impl(testcontext):
    asset = testcontext.assets["social menu"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should be able to hover over the "twitter logo" link')
def step_impl(testcontext):
    asset = testcontext.assets["twitter logo"]
    assert testcontext.browser.hoverifexists(asset), testcontext.info


@then(u'I should be able to hover over the "rss logo" link')
def step_impl(testcontext):
    asset = testcontext.assets["rss logo"]
    assert testcontext.browser.hoverifexists(asset), testcontext.info


@then(u'I should be able to hover over the "events link"')
def step_impl(testcontext):
    asset = testcontext.assets["events link"]
    assert testcontext.browser.hoverifexists(asset), testcontext.info


@then(u'I should be able to hover over the "mieterwerden link"')
def step_impl(testcontext):
    asset = testcontext.assets["mieterwerden link"]
    assert testcontext.browser.hoverifexists(asset), testcontext.info


@then(u'I should be able to hover over the "imprint link"')
def step_impl(testcontext):
    asset = testcontext.assets["imprint link"]
    assert testcontext.browser.hoverifexists(asset), testcontext.info


@then(u'I should be able to hover over the "anfahrt link"')
def step_impl(testcontext):
    asset = testcontext.assets["anfahrt link"]
    assert testcontext.browser.hoverifexists(asset), testcontext.info


@then(u'I should be able to hover over the "press link"')
def step_impl(testcontext):
    asset = testcontext.assets["press link"]
    assert testcontext.browser.hoverifexists(asset), testcontext.info


@then(u'I should be able to hover over the "mieterinfos link"')
def step_impl(testcontext):
    asset = testcontext.assets["mieterinfos link"]
    assert testcontext.browser.hoverifexists(asset), testcontext.info
