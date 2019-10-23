'''Modulo de IBM conexion '''
import json
import util
import pymqi

class ibmmq:
    '''MQConnection class'''
    
    @classmethod
    def __init__(cls, **kwargs):
        '''Create IBM MQ Connection'''
        keys = util.DICT2KEYS(kwargs, 'manager', 'channel', 'host', 'port', 'queue', 'user', 'pwd')
        queue_manager, channel, host, port, queue_name, user, password = keys
        conn_info = '%s(%s)' % (host, port)
        cls.qmgr = pymqi.connect(queue_manager, channel, conn_info, user, password)
        cls.queue = pymqi.Queue(cls.qmgr, queue_name)

    @classmethod
    def send_json(cls, message):
        '''Send json message to IBM MQ Queue'''
        cls.queue.put(json.dumps(message).encode("utf-8"))

    @classmethod
    def close_connection(cls):
        '''Close IBM MQ Connection'''
        cls.queue.close()
        cls.qmgr.disconnect()