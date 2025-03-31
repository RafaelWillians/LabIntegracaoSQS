import time
import sys
import boto3
import os

# Obtem a URL da fila SQS por uma variavel de ambiente.
sqs_queue_url = os.getenv("SQS_QUEUE_URL")

sqs = boto3.client("sqs")


# Irá enviar mensagem indicando que o job nao foi iniciado
response = sqs.send_message(
    QueueUrl=sqs_queue_url
    MessageBody='Processamento nao iniciado'
)

# Tera atraso de 10 segundos, apenas para simular um processamento assincrono entre as mudancas de status
time.sleep(10)

# Irá enviar mensagem indicando que o job foi iniciado
response = sqs.send_message(
    QueueUrl=sqs_queue_url
    MessageBody='Processamento iniciado'
)

# Tera atraso de 10 segundos, apenas para simular um processamento assincrono entre as mudancas de status
time.sleep(10)

# Irá enviar mensagem indicando que o job nao foi iniciado
response = sqs.send_message(
    QueueUrl=sqs_queue_url
    MessageBody='Processamento concluido'
)