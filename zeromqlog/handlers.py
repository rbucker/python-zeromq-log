"""copied almost byte for byte from jedp/python-redis-log
There was no copyright in the original. Therefore, none here.
"""
import logging
import zmq
import simplejson as json

class ZeroMQFormatter(logging.Formatter):
    def format(self, record):
        """
        JSON-encode a record for serializing through redis.

        Convert date to iso format, and stringify any exceptions.
        """
        data = record._raw.copy()

        # serialize the datetime date as utc string
        data['time'] = data['time'].isoformat()

        # stringify exception data
        if data.get('traceback'):
            data['traceback'] = self.formatException(data['traceback'])
    
        return json.dumps(data)

class ZeroMQHandler(logging.Handler):
    """
    Publish messages to a zmq channel.

    As a convenience, the classmethod to() can be used as a 
    constructor, just as in Andrei Savu's mongodb-log handler.
    """

    @classmethod
    def to(cklass, channel, url='localhost', port=5555, level=logging.NOTSET):
        context = zmq.Context()
        publisher = context.socket (zmq.PUB)
        return cklass(channel, publisher.bind(url+':'+str(port)), level=level)

    def __init__(self, channel, zmq_client, level=logging.NOTSET):
        """
        Create a new logger for the given channel and zmq_client.
        """
        logging.Handler.__init__(self, level)
        self.channel = channel
        self.zmq_client = zmq_client
        self.formatter = ZeroMQFormatter()

    def emit(self, record):
        """
        Publish record to redis logging channel
        """
        try :
            msg = zmq.log.handlers.TOPIC_DELIM.join([self.channel,self.format(record)])
            self.zmq_client.send(msg)
        except zmq.core.error.ZMQError:
            pass
 
class ZeroMQListHandler(logging.Handler):
    """
    Publish messages to redis a redis list.

    As a convenience, the classmethod to() can be used as a
    constructor, just as in Andrei Savu's mongodb-log handler.

    If max_messages is set, trim the list to this many items.
    """

    @classmethod
    def to(cklass, key, max_messages=None, url='localhost', port=5555, level=logging.NOTSET):
        context = zmq.Context()
        publisher = context.socket (zmq.PUB)
        return cklass(key, max_messages, publisher.bind(url+':'+str(port)), level=level)

    def __init__(self, key, max_messages, zmq_client, level=logging.NOTSET):
        """
        Create a new logger for the given key and redis_client.
        """
        logging.Handler.__init__(self, level)
        self.key = key
        self.zmq_client = zmq_client
        self.formatter = ZeroMQFormatter()
        self.max_messages = max_messages

    def emit(self, record):
        """
        Publish record to redis logging list
        """
        try :
            self.zmq_client.send(record)
        except zmq.core.error.ZMQError:
            pass

# __END__
