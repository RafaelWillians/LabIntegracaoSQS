# Lab Integração do SQS com Python

Olá! Nesse lab iremos utilizar o SQS, para integrar 2 scripts em Python. Um script irá receber as mensagens da fila e outro irá enviar as mensagens.

Usaremos o CloudShell para executar os comandos.

**Atenção:** sempre confira qual conta você efetuou login. O uso da conta na AWS é de sua inteira responsabilidade! Sempre que puder durante as etapas, faça prints da tela, para indicar que as concluiu com êxito.

## Passo 1 - Criar a fila do SQS

1 - Abra o console de gerenciamento da AWS e depois abra o CloudShell.

![aws-cloudshell1](/img/aws-cloudshell1.png)

2 - Copie o comando abaixo para um editor de texto, mude a parte de fila-nomesobrenome para colocar o seu nome e sobrenome. Este comando irá salvar esse nome para usarmos em seguida.

Exemplo: fila-rafaelteste

```
export SQS_NAME='fila-nomesobrenome'
```

3 - Execute o comando abaixo. Este comando irá criar uma fila do SQS, com o nome salvo anteriormente e irá armazenar a URL da fila no CloudShell mesmo em abas adicionais, que iremos utilizar nos scripts seguintes.

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

6 - Execute o comando abaixo no CloudShell e o script receber.py irá checar constantemente se chega alguma mensagem no SQS.
```
python3 receber.py
```

7 - Agora abra uma nova aba no CloudShell, no sinal de + azul, conforme imagem abaixo. Ao clicar no sinal de +, irá perguntar o ambiente. Clique no nome da região como no exemplo abaixo.

![cloudshell-aba](/img/cloudshell-aba.PNG)

8 - Na aba nova, execute os comandos abaixo, para abrir o diretorio LabIntegracaoSQS e executar o script enviar.py dentro dele.
Este script irá enviar uma mensagem.
```
cd LabIntegracaoSQS/
python3 enviar.py
```

9 - Clique na aba anterior do CloudShell e irá mostrar a mensagem sendo recebida pelo script.

![cloudshell-mensagem-recebida](/img/cloudshell-mensagem-recebida.PNG)

10 - Agora que tanto enviamos, quanto recebemos a mensagem com o SQS, iremos executar mais um script, para simularmos um processamento assíncrono de uma aplicação. Clique na segunda aba do CloudShell, execute o comando abaixo e depois volte na primeira aba do CloudShell.
```
python3 atualizar_status.py
``` 

11 - Pronto! Você pode olhar o código do arquivo atualizar_status.py aqui deste repositório e ver que, entre uma mensagem e outra, podemos implementar algum código para algum processamento e, para cada etapa de execução, podemos enviar uma mensagem no SQS para indicar o status.

![cloudshell-atualizar-status](/img/cloudshell-atualizar-status.PNG)

12 - Agora, iremos excluir os arquivos e a fila do SQS. Ainda na primeira aba, clique no meio dela com o mouse e aperte as teclas CTRL e C no teclado, para parar de executar o recebimento das mensagens.
Depois, execute os comandos abaixo.
```
cd ..
rm -rf LabIntegracaoSQS
```

13 - Agora, exclua a fila do SQS executando o comando abaixo.
```
aws sqs delete-queue --queue-url $SQS_QUEUE_URL
```

14 - Depois de executar o comando acima, feche o CloudShell.
Abra o serviço SQS na barra de pesquisa, clique no ícone de menu na parte de cima da tela e verifique se a fila que você criou foi excluída.

![sqs-tela](/img/sqs-tela.PNG)

15 - Se a sua fila foi excluída com sucesso, tudo pronto! Lab finalizado com sucesso!