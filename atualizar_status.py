import time
import sys
import boto3

sqs = boto3.client("sqs")


# Irá enviar mensagem indicando que o job nao foi iniciado
response = sqs.send_message(
    QueueUrl='fila-nomesobrenome'
    MessageBody='Processamento nao iniciado'
)

# Tera atraso de 10 segundos, apenas para simular um processamento assincrono entre as mudancas de status
time.sleep(10)

# Irá enviar mensagem indicando que o job foi iniciado
response = sqs.send_message(
    QueueUrl='fila-nomesobrenome'
    MessageBody='Processamento iniciado'
)

# Tera atraso de 10 segundos, apenas para simular um processamento assincrono entre as mudancas de status
time.sleep(10)

# Irá enviar mensagem indicando que o job nao foi iniciado
response = sqs.send_message(
    QueueUrl='fila-nomesobrenome'
    MessageBody='Processamento concluido'
)