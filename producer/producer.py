from time import sleep
from json import dumps
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number' : e}
    resp = producer.send('test', value=data)
    if resp:
        print('Message sendt successfully')
    else:
        print('Something wnt wrong')
    sleep(5)            