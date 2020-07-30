import face_recognition

import pika

credentials = pika.PlainCredentials('dusk', 'dusk')
parameters = pika.ConnectionParameters(host='localhost',
                                       port=5678,
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#  ----- SHOULD BE INIT IN DUSK ALREADY -----
# channel.exchange_declare(exchange='logs', exchange_type='fanout')

# result = channel.queue_declare(queue='', exclusive=True)
# queue_name = result.method.queue

# channel.queue_bind(exchange='logs', queue=queue_name)
#  ----- SHOULD BE INIT IN DUSK ALREADY -----

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue="to-dusk-python", on_message_callback=callback, auto_ack=True)

channel.start_consuming()