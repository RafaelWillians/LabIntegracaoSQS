# Lab Integração do SQS com Python

Olá! Nesse lab iremos utilizar o SQS, para integrar 2 scripts em Python. Um script irá receber as mensagens da fila e outro irá enviar as mensagens.

Usaremos o CloudShell para executar os comandos.

**Atenção:** sempre confira qual conta você efetuou login. O uso da conta na AWS é de sua inteira responsabilidade!

## Passo 1 - Criar a fila do SQS

1. Abra o console de gerenciamento da AWS e depois abra o CloudShell.
![aws-cloudshell1](/img/aws-cloudshell1.png)

2. Copie o comando abaixo para um editor de texto, mude


```
aws sqs create-queue \
    --queue-name <fila-nomesobrenome> \
    --attributes VisibilityTimeout=30,MessageRetentionPeriod=1800
```





