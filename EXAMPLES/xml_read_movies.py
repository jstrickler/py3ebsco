#!/usr/bin/env python

# import xml.etree.ElementTree as ET
import lxml.etree as ET

movies_doc = ET.parse('movies.xml') # <1>

movies = movies_doc.getroot() # <2>

for movie in movies: # <3>
    print('{} by {}'.format(
            movie.get('name'), # <4>
            movie.findtext('director'), # <5>
        )
    )
