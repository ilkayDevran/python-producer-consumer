# Kafka Produce & Consumer in Python

This repo is created for a demonstration of Kafka data streaming on Docker container. Also sample producer and consumer scripts are inluded.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install **Kafka-Python**.

```bash
pip install kafka-python
```

## Usage

To start Kafka run.
```bash
docker-compose up
```

After the creation of containers is completed, we need to create a Kafka topic to write and read on it. With the command below **test** topic is created.
```bash
docker exec -it kafka /opt/bitnami/kafka/bin/kafka-topics.sh \
    --create \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1 \
    --topic test 
```

Now let's start with the Python part. First we need to run the producer script. The script sends numbers one by one every 5 seconds to Kafka.
```bash
python ./producer/producer.py
```

Open a new tab on the terminal and run the consumer script as well.
```bash
python ./consumer/consumer.py
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.