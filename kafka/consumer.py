import json
from datetime import datetime
from kafka import KafkaConsumer
from zookeeper_and_kafka_manager import KafkaManager
import  time

def get_dict(value):
    return {'data': value}



def main():
    consumer = KafkaConsumer(
        'quotes',
        bootstrap_servers='localhost:9092',
        group_id='my-group',
        consumer_timeout_ms=120000
    )
    path = "E:\\streaming_data\\quotes\\"
    for message in consumer:
        data = get_dict(json.loads(message.value)[0])
        print(json.loads(message.value)[0])
        print(data)
        filename = datetime.now().strftime("%Y%m%d%H%M%S")
        with open(path + filename + '.json', 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == '__main__':
    kafka_manager = KafkaManager(r"C:\kafka")
    kafka_manager.start()
    main()
    kafka_manager.stop()