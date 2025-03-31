# Lab Integração do SQS com Python

Olá! Nesse lab iremos utilizar o SQS, para integrar 2 scripts em Python. Um script irá receber as mensagens da fila e outro irá enviar as mensagens.

Usaremos o CloudShell para executar os comandos.

**Atenção:** sempre confira qual conta você efetuou login. O uso da conta na AWS é de sua inteira responsabilidade!

## Passo 1 - Criar a fila do SQS

1 - Abra o console de gerenciamento da AWS e depois abra o CloudShell.

![aws-cloudshell1](/img/aws-cloudshell1.png)

2 - Copie o comando abaixo para um editor de texto, mude a parte de fila-nomesobrenome para colocar o seu nome e sobrenome. Este comando irá salvar esse nome para usarmos em seguida.

    Exemplo: fila-rafaelteste

```
export SQS_NAME='fila-nomesobrenome'
```

3 - Execute o comando abaixo. Este comando irá criar uma fila do SQS, com o nome salvo anteriormente e irá armazenar a URL da fila, que iremos utilizar nos scripts seguintes.
```
echo 'export SQS_QUEUE_URL='$(aws sqs create-queue \
    --queue-name $SQS_NAME \
    --attributes VisibilityTimeout=30,MessageRetentionPeriod=1800 \
    --query 'QueueUrl' --output text) >> ~/.bashrc && source ~/.bashrc
```

4 -  Execute os comandos abaixo no CloudShell, para baixarmos os arquivos do lab e carregarmos a pasta baixada.
```
git clone https://github.com/RafaelWillians/LabIntegracaoSQS.git
cd LabIntegracaoSQS/
```

5 -  Antes de executarmos os scripts Python, precisamos editá-los, para apontarmos para a fila correta.

Primeiro, edite o arquivo receber.py com o comando abaixo.


6 - Execute o comando abaixo no CloudShell e o script receber.py irá checar constantemente se chega alguma mensagem no SQS.
```
python3 receber.py
```

7 - Agora abra uma nova aba no CloudShell, no sinal de + azul, conforme imagem abaixo. Ao clicar no sinal de +, irá perguntar o ambiente. Clique no nome da região como no exemplo abaixo.

![cloudshell-aba](/img/cloudshell-aba.PNG)

8. Na aba nova, execute o comando abaixo, para executar o script enviar.py.
Este script irá enviar mensagens.


```

```


