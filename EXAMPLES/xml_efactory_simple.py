#!/usr/bin/env python
# (c) 2016 John Strickler
#
import lxml.etree as ET
from lxml.builder import E # <1>

xml = (
    E.animals(  # <2>
        E.animal('wombat', species="Vombatus ursinus"),
        E.animal('bushbaby', species="Galago senegalensis")
    )
)

print(ET.tostring(xml, pretty_print=True).decode())
