# -*- coding:utf-8 -*-

'''This module is an hml utility tool to create html file or reports for sikuli'''

from sikuli import *

def hello_world(output_file):
    '''Create an Hello World html file'''
    content = """
        <!doctype html>\n
        \n
        <html lang="en">\n
        <head>\n
        \t<meta charset="utf-8">\n
        \n
        \t<title>The HTML5 Herald</title>\n
        \t<meta name="description" content="The HTML5 Herald">\n
        \t<meta name="author" content="SitePoint">\n
        \n
        \t<link rel="stylesheet" href="css/styles.css?v=1.0">\n
        \n
        \t<!--[if lt IE 9]>\n
        \t\t<script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script>\n
        \t<![endif]-->\n
        </head>\n
        \n
        <body>\n
        \t<!--end of body-->\n
        </body>\n
        </html>
    """
    with open(output_file, 'w') as f:
        f.write(content)
