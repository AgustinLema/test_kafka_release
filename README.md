#Kafka Wrapper
Kafka wrapper will subscribe to a Kafka topic. Once a message is received, it will execute a function and send the output to another Kafka queue.

##wrapped folder
For kafka Wrapper to work, there should be a "wrapped" folder created in the root of the project with the following content:
- wrapped_config.json
- wrapped.py

###Kafka used
docker run -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=localhost --env ADVERTISED_PORT=9092 spotify/kafka