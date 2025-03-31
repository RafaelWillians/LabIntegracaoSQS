import boto3

sqs = boto3.client("sqs")
sqs_queue_url = os.getenv("SQS_QUEUE_URL")

while True:
    print("Recebendo mensagens")
    response = sqs.receive_message(
        QueueUrl=sqs_queue_url,
        MaxNumberOfMessages=2,
        WaitTimeSeconds=5,
    )

    if "Mensagens" in response:
        for message in response["Mensagens"]:
            print(f"Corpo mensagem: {message['Body']}")
            print(f"Removendo mensagem: {message['MessageId']}")
            sqs.delete_message(
                QueueUrl=sqs_queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )