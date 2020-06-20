import pika, os, time

def generate_pdf(message):
    print("PDF processing")
    print("Received " + str(message))

    time.sleep(5)
    print("PDF processing finished")
    return

def callback(ch, method, properties, body):
    generate_pdf(body)

url = os.environ.get('CLOUDAMQP_URL')

rabbitmq_params = pika.URLParameters(url)

connection = pika.BlockingConnection(rabbitmq_params)

channel = connection.channel()
channel.queue_declare(queue='pdfprocess')

channel.basic_consume('pdfprocess', callback, auto_ack=True)

channel.start_consuming()

connection.close()