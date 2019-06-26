import logging
import sys

from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Wrapper():
    def __init__(self, input_topic, output_topic):
        self.input_topic = input_topic
        self.output_topic = output_topic
        self.consumer, self.producer = self.initialize_kafka()

    def initialize_kafka(self):
        logging.info("Initializing consumer")
        """
        Auto_offset_reset: Where to start reading after breaking.
        Earliest will start reading from latest committed offset.
        group_id: Which consumer group to use for this consumer.
        """
        consumer = KafkaConsumer(
            self.input_topic,
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: loads(x.decode('utf-8')))

        logging.info("Initializing producer")
        # TODO: Replace host with config. Serializer to how to serialize when sending.
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                 value_serializer=lambda x:
                                 dumps(x).encode('utf-8'))

        return consumer, producer

    def start_processing(self):
        logging.info("Initializing processing")

        for message in self.consumer:
            logging.info("Got message from topic {}".format(self.input_topic))
            response = self.process_message(message.value)
            logging.info("Message processed, sending to topic {}".format(self.output_topic))
            self.producer.send(self.output_topic, value=response)
            self.producer.flush()
            logging.info("Message sent")

    def process_message(self, message):
        import wrapped.wrapped_script
        return wrapped.wrapped_script.process(message)

def main(wrapped_path, input_topic, output_topic):
    sys.path.insert(0, wrapped_path)
    w = Wrapper(input_topic, output_topic)
    w.start_processing()

if __name__ == '__main__':
    # TODO CHECK ARGUMENT COUNT
    wrapped_path = sys.argv[0]
    input_topic = sys.argv[1]
    output_topic = sys.argv[2]
    main(wrapped_path, input_topic, output_topic)
