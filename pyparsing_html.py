#!/usr/bin/env python
# (c) 2016 John Strickler
#
import requests
from pprint import pprint
import pyparsing as pp


response = requests.get('http://www.python.org')

html = response.content

link_start, link_end = pp.makeHTMLTags('a')
link_content = pp.SkipTo(link_end).setResultsName('link')
full_link = link_start + link_content + link_end.suppress()

count = 1
for token, _, _ in full_link.scanString(html):
    if token.href.lower().startswith('http'):
        print("LINK {}:".format(count))
        print("{} ==> {}".format(token.link, token.href))
        print(('-' * 60))
        count += 1
