#!/usr/bin/env python
# (c) 2016 John Strickler
#
import requests
import pyparsing as pp

response = requests.get('http://git-scm.com')

if response.status_code == requests.codes.OK:

    html = response.content

    def skip_github(s, loc, tokens):
        if "github" in tokens[1][1]:
            raise pp.ParseException("github links not allowed")

    link_start, link_end = pp.makeHTMLTags('a')
    link_content = pp.SkipTo(link_end).setResultsName('link')
    link_start.setParseAction(skip_github)
    full_link = link_start + link_content + link_end.suppress()

    with open('git_links.tsv', 'w') as git_links_out:
        for token, _, _ in full_link.scanString(html):
            if token.href.lower().startswith('http'):
                git_links_out.write(
                    "{}\t{}\n".format(token.link.upper(), token.href)
                )
else:
    print("Unable to connect")
