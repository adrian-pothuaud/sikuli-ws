# noinspection PyUnresolvedReferences
from sikuli.Sikuli import *
from case import *


@when(u'I click the "Bitbucket link"')
def step_impl(testcontext):
    asset = testcontext.assets["Bitbucket link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info
    assert testcontext.browser.clicklink(asset), testcontext.info


@when(u'I press the DOWN key #count# times')
def step_impl(testcontext):
    count = int(testcontext.constants["count"])
    for press in xrange(0,count):
        assert testcontext.browser.enterkey(Key.DOWN), testcontext.info
        wait(1)


@then(u'I should see the "#page# title"')
def step_impl(testcontext):
    asset = testcontext.assets[replaceconstants("#page# title")]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see the "arjs.net company logo" after 5s')
def step_impl(testcontext):
    asset = testcontext.assets["arjs.net company logo"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should be able to close the "arjs.net company logo" tab after 5s')
def step_impl(testcontext):
    asset = testcontext.assets["arjs.net company logo"]
    wait(5)
    assert testcontext.browser.checkifexists(asset), testcontext.info
    assert testcontext.browser.closetab(), testcontext.info


@then(u'I should see the "JePySi title" after 1s')
def step_impl(testcontext):
    asset = testcontext.assets["JePySi title"]
    wait(1)
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see the "Bitbucket logo" after 5s')
def step_impl(testcontext):
    asset = testcontext.assets["Bitbucket logo"]
    wait(5)
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should be able to close the "Bitbucket logo" tab after 5s')
def step_impl(testcontext):
    asset = testcontext.assets["Bitbucket logo"]
    wait(5)
    assert testcontext.browser.checkifexists(asset), testcontext.info
    assert testcontext.browser.closetab(), testcontext.info


@then(u'I should be able to close the "Bintray url" tab after 5s')
def step_impl(testcontext):
    asset = testcontext.assets["Bintray url"]
    wait(5)
    assert testcontext.browser.checkifexists(asset), testcontext.info
    assert testcontext.browser.closetab(), testcontext.info


@then(u'I should see the "Bintray url" after 5s')
def step_impl(testcontext):
    asset = testcontext.assets["Bintray url"]
    wait(5)
    assert testcontext.browser.checkifexists(asset), testcontext.info


@when(u'I click the "Bintray link"')
def step_impl(testcontext):
    asset = testcontext.assets["Bintray link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info
    assert testcontext.browser.clicklink(asset), testcontext.info


@given(u'I see a "Bintray link"')
def step_impl(testcontext):
    asset = testcontext.assets["Bintray link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@when(u'I click the "JePySi title link"')
def step_impl(testcontext):
    asset = testcontext.assets["JePySi title link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info
    assert testcontext.browser.clicklink(asset), testcontext.info


@when(u'I click the "arjs.net link"')
def step_impl(testcontext):
    asset = testcontext.assets["arjs.net link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info
    assert testcontext.browser.clicklink(asset), testcontext.info


@given(u'I see the "JePySi title link"')
def step_impl(testcontext):
    asset = testcontext.assets["JePySi title link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@when(u'I click the "impressum link"')
def step_impl(testcontext):
    asset = testcontext.assets["impressum link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info
    assert testcontext.browser.clicklink(asset), testcontext.info


@then(u'I should see the "imprint title" after 5s')
def step_impl(testcontext):
    asset = testcontext.assets["imprint title"]
    wait(5)
    assert testcontext.browser.checkifexists(asset), testcontext.info


@when(u'I click the "imprint link"')
def step_impl(testcontext):
    asset = testcontext.assets["imprint link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info
    assert testcontext.browser.clicklink(asset), testcontext.info


@then(u'I should see a "imprint link"')
def step_impl(testcontext):
    asset = testcontext.assets["imprint link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@given(u'I see a "Bitbucket link"')
def step_impl(testcontext):
    asset = testcontext.assets["Bitbucket link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@given(u'I see a "arjs.net link"')
def step_impl(testcontext):
    asset = testcontext.assets["arjs.net link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see a "arjs.net link"')
def step_impl(testcontext):
    asset = testcontext.assets["arjs.net link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see a "#page# text" message')
def step_impl(testcontext):
    asset = testcontext.assets[replaceconstants("#page# text")]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@given(u'I see the "first page" selected')
def step_impl(testcontext):
    asset = testcontext.assets["first page"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see the "impressum title"')
def step_impl(testcontext):
    asset = testcontext.assets["impressum title"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@given(u'I see a "imprint link"')
def step_impl(testcontext):
    asset = testcontext.assets["imprint link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@given(u'I can hover of the "impressum link"')
def step_impl(testcontext):
    asset = testcontext.assets["impressum link"]
    assert testcontext.browser.hoverifexists(asset, True), testcontext.info


@then(u'I should see a "Bitbucket link"')
def step_impl(testcontext):
    asset = testcontext.assets["Bitbucket link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see a "Bintray link"')
def step_impl(testcontext):
    asset = testcontext.assets["Bintray link"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see a "Tested with" message')
def step_impl(testcontext):
    asset = testcontext.assets["Tested with"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see a "black Tested with" message')
def step_impl(testcontext):
    asset = testcontext.assets["black Tested with"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see the "Address" block')
def step_impl(testcontext):
    asset = testcontext.assets["Address"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see the "Release date" block at the page end')
def step_impl(testcontext):
    testcontext.browser.pageend()
    asset = testcontext.assets["Release date"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see the "UstId" block')
def step_impl(testcontext):
    asset = testcontext.assets["UstId"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see the "imprint" title')
def step_impl(testcontext):
    asset = testcontext.assets["imprint"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see the "imprint" title after 5s')
def step_impl(testcontext):
    asset = testcontext.assets["imprint"]
    wait(5)
    assert testcontext.browser.checkifexists(asset), testcontext.info


@given(u'I see the "buttons sidebar"')
def step_impl(testcontext):
    asset = testcontext.assets["buttons sidebar"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@given(u'I see the "JePySi title"')
def step_impl(testcontext):
    asset = testcontext.assets["JePySi title"]
    assert testcontext.browser.checkifexists(asset), testcontext.info


@when(u'I hover over the "<button> dot"')
def step_impl(testcontext):
    asset = replacevariables(testcontext.assets["<button> dot"], testcontext.example)
    ox = int(testcontext.example["dx"])
    oy = int(testcontext.example["dy"])
    assert testcontext.browser.hoverifexists(asset, True, ox, oy), testcontext.info


@when(u'I click the "<button> dot"')
def step_impl(testcontext):
    asset = replacevariables(testcontext.assets["<button> dot"], testcontext.example)
    ox = int(testcontext.example["dx"])
    oy = int(testcontext.example["dy"])
    assert testcontext.browser.clicklink(asset, ox, oy), testcontext.info


@then(u'I should see the "<title> title after 1s"')
def step_impl(testcontext):
    asset = replacevariables(testcontext.assets["<title> title"], testcontext.example)
    wait(1)
    assert testcontext.browser.checkifexists(asset), testcontext.info


@then(u'I should see the "<title> dot"')
def step_impl(testcontext):
    asset = replacevariables(testcontext.assets["<title> dot"], testcontext.example)
    assert testcontext.browser.checkifexists(asset), testcontext.info
