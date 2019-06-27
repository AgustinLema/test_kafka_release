# Kafka Wrapper
Kafka wrapper will subscribe to a Kafka topic. Once a message is received, it will execute a function and send the output to another Kafka queue.

## Deployer
Deployer is the default function run by wrapper. When started it will take the code received in code_input topic, create a new wrapper and use the function in code for the new wrapper as well as the input and output topics.

### Kafka used
docker run -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=localhost --env ADVERTISED_PORT=9092 spotify/kafka
