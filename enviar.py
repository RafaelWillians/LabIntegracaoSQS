import boto3

sqs = boto3.client("sqs")

### ATENÇÃO!
# Mude o send_message, para escrever uma mensagem 'ola mundo' na fila que você criou
###


response = sqs.send_message(
    QueueUrl='????'
    MessageBody='????'
)