# -*- coding:utf-8 -*-

'''This module is an hml utility tool to create html file or reports for sikuli'''

from sikuli import *

allosPath = os.path.dirname(getBundlePath())
if not allosPath in sys.path:
    sys.path.append(allosPath)

if __name__ == '__main__':

    from html import XHTML

    doc = XHTML('html')
    head = doc.head
    title = head.title("My title")
    body = doc.body
    nav = body.nav
    l = nav.ul(newlines=False)
    for i in [{"label":"Home", "link":"/"}, {"label":"About", "link":"/about"}]:
        l.li.a(i["label"], href=i["link"])
    section1 = body.section
    p1 = section1.p("Hello World!")
    foot = body.footer
    foot.p("eno.qa.cfg.chg")
    print(doc)