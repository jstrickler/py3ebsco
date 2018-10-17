#!/usr/bin/env python
# (c) 2016 John Strickler
#
import requests
from pprint import pprint
import pyparsing as pp


def external_only(s, location, tokens):
    if not tokens[1][1].lower().startswith('http'):
        raise pp.ParseException('Invalid scheme')


def trim(s, location, tokens):
    return '** ' + s[:80].replace('\n', '').replace('\r', '') + ' **'

response = requests.get('http://www.python.org')

html = response.content

link_start, link_end = pp.makeHTMLTags('a')
link_content = pp.SkipTo(link_end).setResultsName('link')
link_start.setParseAction(external_only)
link_content.setParseAction(trim)
full_link = link_start + link_content + link_end.suppress()

for i, (token, _, _) in enumerate(full_link.scanString(html)):
    print("LINK {}:".format(i))
    print("{} ==> {}".format(token.link, token.href))
    print(('-' * 60))
