'''Module main'''
import json
import os
from rabbitmq import RabbitMQ
from pika import exceptions
from parameter import Parameter
from send_grid import SendGrid
from traceability import Traceability
from transform import Transform
import uuid

class App:
    '''class Application'''

    @classmethod
    def __init__(cls):
        '''Method init'''
        cls.accountName = os.getenv('ACCOUNT_NAME')
        print('cls.accountName ',cls.accountName)
        #cls.accountKey = os.getenv('ACCOUNT_KEY')
        print('cls.accountKey ', cls.accountKey )
        cls.config = Parameter(cls.accountName, cls.accountKey).get_parameters()
    @classmethod
    def callback(cls, channel, method, properties, body):
        '''Receive message '''
        try:
            del properties
            transaction_id = str(uuid.uuid4())
            businessKey = cls.config['traceability']['businessKey']
            data = json.loads(body.decode('utf-8'))            
            #print(data)        
            #ibmmq(**cls.config['traceability']).send_json('message')
            #Traceability(**cls.config['traceability']).save(
            #    businessKey,transaction_id,"Desencolar topico",
            #    "Subscriber-Callback", "IN", str(data), 
            #    "OK", "Mensaje recibido") 

            print('Transform.transformacion(data)', Transform.transformacion(data))

        except Exception as error:
            print(error)
            SendGrid().create_message(
                cls.config['sendGrid']['apiKey'],
                cls.config['sendGrid']['fromEmail'],
                cls.config['sendGrid']['toEmail'],
                str(error))   
            #Traceability(**cls.config['traceability']).save(
            #    businessKey,transaction_id,"Error en la calidad del mensaje enviado",
            #    "Subscriber", "IN", str(body),
            #    "ERROR", "Lectura Fallida, "+str(error))
        finally:
            channel.basic_ack(delivery_tag=method.delivery_tag)

    @classmethod
    def main(cls):
        while True:
            try:
                objqueue = RabbitMQ(**cls.config['source'])
                objqueue.connect()
                objqueue.channel.basic_consume(
                    queue=cls.config['source']['queue'],
                    on_message_callback=cls.callback,
                    auto_ack=False
                )
                #cls.traceability = Traceability(**cls.config['traceability'])
                try:
                    objqueue.channel.start_consuming()
                except KeyboardInterrupt:                    
                    objqueue.disconnect()
                    objqueue.channel.stop_consuming()
                    break
            except (exceptions.ConnectionClosedByBroker,exceptions.AMQPChannelError,exceptions.AMQPConnectionError) as error_connection:
                print('Conexion cerrada con a RabbitMQ', error_connection)
                continue
                  
if __name__ == '__main__':
    App().main()
