#!/usr/bin/env python

import logging

logging.basicConfig( # <1>
    filename='../TEMP/exception.log',
    level=logging.WARNING,  # <2>
)

for i in range(3):
    try:
        result = i/0
    except ZeroDivisionError:
        logging.exception('Logging with exception info') # <3>
