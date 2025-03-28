import boto3

sqs = boto3.client("sqs")
queue_url = 'fila-nomesobrenome'

while True:
    print("Recebendo mensagens")
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=2,
        WaitTimeSeconds=5,
    )

    if "Mensagens" in response:
        for message in response["Mensagens"]:
            print(f"Corpo mensagem: {message['Body']}")
            print(f"Removendo mensagem: {message['MessageId']}")
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )