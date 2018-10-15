#!/usr/bin/env python
import requests
from pprint import pprint
import pyparsing as pp

response = requests.get('http://www.python.org')

html = response.content  # <1>

link_start, link_end = pp.makeHTMLTags('a')  # <2>
link_content = pp.SkipTo(link_end).setResultsName('link') # <3>
full_link = link_start + link_content + link_end.suppress() # <4>

count = 1
for token, _, _ in full_link.scanString(html): # <5>
    if token.href.lower().startswith('http'): # <6>
        print("LINK {}:".format(count))
        print("{} ==> {}".format(token.link, token.href))
        print(('-' * 60))
        count += 1
