#amqps://soxcuwue:DJSrY-NBP1T1ik7GZk1PZE4wxP5TXGSi@puffin.rmq2.cloudamqp.com/soxcuwue

import json
import pika, django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()
from products.models import Product


params = pika.URLParameters("amqps://ywifnmau:Olc-tMjfC-mZXiNQCBeHA56Jv2u5xdsZ@puffin.rmq2.cloudamqp.com/ywifnmau")
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    data = json.loads(body)
    print(data)

    if properties.content_type == "like_event":
        record  = Product.objects.get(id=data)
        print(record)
        record.likes += 1
        record.save()
        print("Likes updated")
    

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("started consuming in admin")
channel.start_consuming()

channel.close()
