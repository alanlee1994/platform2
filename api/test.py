import signal_pb2
import pdb
import pika

# import proto_tutorial_pb2
import numpy as np
import time
import datetime

def dummy_engine():
    credential = pika.PlainCredentials('eon_dev', 'eon_dev')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='rabbitmq', 
            port = 5672, 
            virtual_host='eon_dev', 
            credentials=credential)
        )
    channel = connection.channel()
    channel.exchange_declare(exchange='amq.topic', exchange_type='topic', durable=True)
    # count = 0
    while True:
        fireworks = signal_pb2.Signal()
        sig_name=np.random.choice(['copula', 'regression', '9983 ER events', 'HMM'])
        fireworks.name = sig_name
        fireworks.instruments=np.random.choice(['HSI, HSCEI', 'NK, TP'])
        fireworks.signal_ts = str(datetime.datetime.now())
        signal_stats = fireworks.Stats.add()
        signal_stats.total_cnt = np.random.randint(10,100)
        signal_stats.winrate = 0.595
        signal_stats.avg_win = np.random.randint(10,100)
        signal_stats.avg_lose = np.random.randint(10,100)
        signal_stats.median_win = np.random.randint(10,100)
        signal_stats.median_lose = np.random.randint(10,100)
        signal_stats.sharpe = np.random.randint(1,500)/100
        signal_stats.kelly = np.random.randint(-500,500)/500
        signal_stats.signal_value = np.random.randint(10,100)
        enter_ts = datetime.time(np.random.choice([9,10,15]),np.random.choice([0,5,10,15,20,30,25]))
        exit_interval = np.random.choice([5,10,2,3,15])
        exit_ts  = datetime.time(enter_ts.hour, enter_ts.minute + exit_interval)
        signal_stats.enter_ts = str(enter_ts)
        signal_stats.exit_ts = str(exit_ts)
        signal_stats.comments = 'time span' 
        
        # count +=1 
        # if count % 5 == 0:
        #     print(f'{datetime.datetime.now()}: publishing heartbeat')
        #     heartBeat = signal_pb2.Heartbeat()
        #     heartBeat.name = sig_name
        #     heartBeat.status = "running"
        #     heartBeat.ts = str(datetime.datetime.now())
        #     channel.basic_publish(exchange='amq.topic', routing_key='heartbeat', body=heartBeat.SerializeToString())
        print(f'{datetime.datetime.now()}: publishing signal')
        channel.basic_publish(exchange='amq.topic', routing_key='signal', body=fireworks.SerializeToString())
        time.sleep(2)
        
if __name__ == "__main__":
    dummy_engine()
    # pdb.set_trace()

# To Create protofiles for py files.
# protoc --proto_path=api --python_out=api api/signal.proto

# protoc --proto_path=api --js_out=library=signal_pb,binary:api api/signal.proto

# protoc --proto_path=api --js_out=import_style=commonjs,binary:api api/signal.proto
# this line needs to be added to the generated js file /* eslint-disable */
