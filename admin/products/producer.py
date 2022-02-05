#amqps://soxcuwue:DJSrY-NBP1T1ik7GZk1PZE4wxP5TXGSi@puffin.rmq2.cloudamqp.com/soxcuwue

import pika
import json

params = pika.URLParameters("amqps://ywifnmau:Olc-tMjfC-mZXiNQCBeHA56Jv2u5xdsZ@puffin.rmq2.cloudamqp.com/ywifnmau")
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)