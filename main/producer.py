#amqps://soxcuwue:DJSrY-NBP1T1ik7GZk1PZE4wxP5TXGSi@puffin.rmq2.cloudamqp.com/soxcuwue

import pika
import json

params = pika.URLParameters("amqps://soxcuwue:DJSrY-NBP1T1ik7GZk1PZE4wxP5TXGSi@puffin.rmq2.cloudamqp.com/soxcuwue")
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', properties=properties, body=json.dumps(body))