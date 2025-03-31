import boto3
import os

# Obtem a URL da fila SQS por uma variavel de ambiente.
sqs_queue_url = os.getenv("SQS_QUEUE_URL")

sqs = boto3.client("sqs")

response = sqs.send_message(
    QueueUrl=sqs_queue_url
    MessageBody='Ola, mundo! Sou uma mensagem do SQS!'
)