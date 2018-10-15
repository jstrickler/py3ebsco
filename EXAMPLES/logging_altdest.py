#!/usr/bin/env python
import sys
import logging
import logging.handlers

logger = logging.getLogger('ThisApplication') # <1>
logger.setLevel(logging.DEBUG)  # <2>

if sys.platform == 'win32':
    eventlog_handler = logging.handlers.NTEventLogHandler("Python Log Test") # <3>
    logger.addHandler(eventlog_handler) # <4>
else:
    syslog_handler = logging.handlers.SysLogHandler() # <5>
    logger.addHandler(syslog_handler) # <6>

# note -- use your own SMTP server...
email_handler = logging.handlers.SMTPHandler(
    ('smtpcorp.com',8025),
    'LOGGER@pythonclass.com',
    ['jstrick@mindspring.com'],
    'ThisApplication Log Entry',
    ('jstrickpython', 'python(monty)'),
)  # <7>

logger.addHandler(email_handler) # <8>

logger.debug('this is debug') # <9>
logger.critical('this is critical') # <9>
logger.warning('this is a warning') # <9>
