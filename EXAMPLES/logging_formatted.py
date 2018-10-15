#!/usr/bin/env python

import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s', # <1>
    filename='../TEMP/formatted.log',
    level=logging.INFO,
)

logging.info("this is information")
logging.warning("this is a warning")
logging.info("this is information")
logging.fatal("this is fatal")
