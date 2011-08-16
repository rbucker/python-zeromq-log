"""
zeromqlog - a zeromq logging handler for python

>>> from zeromqlog import handlers, logger
>>> l = logger.ZeroMQLogger('my.logger')
>>> l.addHandler(handlers.ZeroMQHandler.to("my:channel"))
>>> l.info("I like breakfast cereal!")
>>> l.error("Oh snap crackle pop", exc_info=True)

ZeroMQ clients subscribed to my:channel will get a json log record.
depends on : https://github.com/zeromq/pyzmq.git

On errors, if exc_info is True, a printed traceback will be included.
"""

__author__ = 'Richard Bucker <richard@bucker.net>'
__version__ = (0, 0, 1)

import logging
import logger

logging.setLoggerClass(logger.ZeroMQLogger)


