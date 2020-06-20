import pika, os

url = os.environ.get('CLOUDAMQP_URL')

rabbitmq_params = pika.URLParameters(url)
rabbitmq_params.socket_timeout = 6

connection = pika.BlockingConnection(rabbitmq_params)

channel = connection.channel()

channel.queue_declare(queue='pdfprocess')

# empty exchange means the default exchange which is a
# direct exchange
channel.basic_publish(exchange='', routing_key='pdfprocess', body='User information')

print("Message sent!")
connection.close()
