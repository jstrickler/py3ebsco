#!/usr/bin/env python

import sys
from subprocess import check_output, Popen, CalledProcessError, STDOUT, PIPE # <1>
from glob import glob
import shlex

if sys.platform == 'win32':
    CMD = 'cmd /c dir'
    FILES = r'..\DATA\t*'
else:
    CMD = 'ls -ld'
    FILES = '../DATA/t*'

cmd_words = shlex.split(CMD)
cmd_files = glob(FILES)

full_cmd = cmd_words + cmd_files

# <2>
try:
    output = check_output(full_cmd) # <3>
    print("Output:", output.decode(), sep='\n') # <4>
except CalledProcessError as e:
    print("Process failed with return code", e.returncode)

print('-' * 50)

# <5>
try:
    cmd = cmd_words + cmd_files + ['spam.txt']
    proc = Popen(cmd, stdout=PIPE, stderr=STDOUT) # <6>
    stdout, stderr = proc.communicate() # <7>
    print("Output:", stdout.decode()) # <8>
except CalledProcessError as e:
    print("Process failed with return code", e.returncode)

print('-' * 50)

try:
    cmd = cmd_words + cmd_files + ['spam.txt']
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE) # <9>
    stdout, stderr = proc.communicate() # <10>
    print("Output:", stdout.decode()) # <11>
    print("Error:", stderr.decode()) # <11>
except CalledProcessError as e:
    print("Process failed with return code", e.returncode)

print('-' * 50)
