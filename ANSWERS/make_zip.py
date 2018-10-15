#!/usr/bin/env python
"""

@author: jstrick
Created on Thu Mar 21 00:20:43 2013

"""
import zipfile

zfile = zipfile.ZipFile('potus.zip','w')
zfile.write('save_potus_info.py')
zfile.write('read_potus_info.py')
zfile.write('potus.pic')
zfile.close()
