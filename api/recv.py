import pika
from abc import ABC, abstractmethod 
import signal_pb2

class FeedListener(ABC):
    """
    FeedListener will take in the securities to listen and the type of message and return the data received.
    """
    def __init__(self, s_msgExchange, l_exchangeTopic, i_timezone, o_msg_object):
        self.exchangeTopic = l_exchangeTopic
        self.msgExchange = s_msgExchange
        self.timezone = i_timezone #GMT+ what?
        self.msg_object = o_msg_object

    def consume(self):
        """
        Making Connection to MDS server and receiving the message based on the protobuf message defined in Jeremy's MDS.
        """
        credential = pika.PlainCredentials('eon_dev', 'eon_dev')
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',port = 5672, virtual_host='eon_dev', credentials=credential))
        self.connection = connection
        channel = connection.channel()
        channel.exchange_declare(exchange=self.msgExchange, exchange_type = "topic", durable=True)
        result = channel.queue_declare('', exclusive=True)
        queue_name = result.method.queue
        binding_keys = self.exchangeTopic
        for binding_key in binding_keys:
            channel.queue_bind(exchange=self.msgExchange, queue=queue_name, routing_key=binding_key)
        channel.basic_consume(queue=queue_name, on_message_callback=self.callback, auto_ack=True)
        channel.start_consuming()
    
    @abstractmethod
    def callback(self):
        pass

class SignalListener(FeedListener):
    def __init__(self, s_msgExchange, l_exchangeTopic, i_timezone, o_msg_obj):
        super(SignalListener, self).__init__(s_msgExchange, l_exchangeTopic, i_timezone, o_msg_obj)

    def callback(self, ch, method, properties, body):
        pb = signal_pb2.Signal()
        pb.ParseFromString(body)
        # heart_beat = signal_pb2.Heartbeat()
        # heart_beat.ParseFromString(body)
        # print(heart_beat)
        print(pb)

if __name__ == '__main__':
    message = {}
    FL = SignalListener("amq.topic", ["signal"], 8, message)
    FL.consume()