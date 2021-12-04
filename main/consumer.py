#amqps://soxcuwue:DJSrY-NBP1T1ik7GZk1PZE4wxP5TXGSi@puffin.rmq2.cloudamqp.com/soxcuwue

import pika
import json
import main

params = pika.URLParameters("amqps://soxcuwue:DJSrY-NBP1T1ik7GZk1PZE4wxP5TXGSi@puffin.rmq2.cloudamqp.com/soxcuwue")
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == "product_created":    #why does this come proprty come through content type
        product = main.Product(id=data['id'], title=data['title'], image=data['image'])
        main.db.session.add(product)
        main.db.session.commit()
        print("Product Created")

    elif properties.content_type == "product_updated":
        product = main.Product.query.get(data['id'])
        product.title=data['title']
        product.image=data['image']
        main.db.session.commit()
        print("Product updated")

    elif properties.content_type == "product_deleted":
        product = main.Product.query.get(data)
        main.db.session.delete(product)
        main.db.session.commit()
        print("Product deleted")

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print("started consuming in main")
channel.start_consuming()

channel.close()
