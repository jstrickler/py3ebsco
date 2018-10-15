#!/usr/bin/env python
# (c) 2016 John Strickler
#
import requests
import pyparsing as pp

def external_only(s, location, tokens):  # <1>
    if not tokens[1][1].lower().startswith('http'):
        raise pp.ParseException('Invalid scheme')

response = requests.get('http://www.python.org')

html = response.content #

link_start, link_end = pp.makeHTMLTags('a')
link_content = pp.SkipTo(link_end).setResultsName('link')
link_start.setParseAction(external_only) # <2>
full_link = link_start + link_content + link_end.suppress()

for i, (token, _, _) in enumerate(full_link.scanString(html)):
    print("LINK {}:".format(i))
    print("{} ==> {}".format(token.link, token.href))
    print(('-' * 60))
