from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

def produce_message(topic, object):
    producer.send(topic, value=object)
    producer.flush()

def consume_message(topic, consumer_group):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id=consumer_group,
        value_deserializer=lambda x: loads(x.decode('utf-8')))
    message = next(consumer)
    consumer.commit()
    return message.value

def consume_all(topic, consumer_group):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',
        enable_auto_commit=True,
        group_id=consumer_group,
        consumer_timeout_ms=300,
        value_deserializer=lambda x: loads(x.decode('utf-8')))
    for i in consumer:
        consumer.commit()
        continue
