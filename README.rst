=====================================================
ZeroMQLog - A ZeroMQ Pub/Sub Logging Handler for Python
=====================================================

A logging handler for Python that publishes log messages using zeromq's 
pub/sub system.  You can use this to read or respond to streaming log
data in real time. If you are using sub-watcher then the messages can be
redirected back to redis or syslog as needed with all sorts of filter goodness.

This project and it's layout and details were inspired by Jed Parsons and
python-redis-log (currently hosted on GitHub).

Installation
------------

The current stable release ::

    pip install python-zeromq-log

or ::

    easy_install python-zeromq-log

The latest from github_ ::

    git clone git://github.com/rbucker881/python-zeromq-log.git
    cd python-zeromq-log
    python setup.py build
    python setup.py install --prefix=$HOME  # for example

.. _github: https://github.com/rbucker881/python-zeromq-log
    
Requirements
------------

- redis_ 
- The `Python redis client`_ by Andy McCurdy
- simplejson_ 

.. _redis: http://redis.io/
.. _Python redis client: https://github.com/andymccurdy/redis-py
.. _simplejson: https://github.com/simplejson/simplejson

Usage
-----

::

    >>> from zeromqlog import handlers, logger
    >>> l = logger.ZeroMQLogger('my.logger')
    >>> l.addHandler(handlers.ZeroMQHandler.to("my:channel"))
    >>> l.info("I like chocolate cake")
    >>> l.error("Belts?", exc_info=True)

ZeroMQ (rbucker881/sub-watcher) clients subscribed to ``my:channel`` will get a json log record like the
following (sent from function ``foo()`` in file ``test.py``: ::

    { username: 'richard',
      args: [],
      name: 'my.logger',
      level: 'info',
      line_no: 6,
      traceback: null,
      filename: 'qa.py',
      time: '2011-06-02T14:50:08.237052',
      msg: 'losing',
      funcname: 'bar',
      hostname: 'frosty.local' }

If an exception is raised, and ``exc_info`` is ``True``, the log will include
a formatted traceback in ``traceback``.

The date is stored as an ISO 8601 string in GMT.  


Contributors
------------

Just in case you missed this at the top of the readme.

This project and it's layout and details were inspired by Jed Parsons and
python-redis-log (currently hosted on GitHub).
