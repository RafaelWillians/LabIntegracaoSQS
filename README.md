# Lab Integração do SQS com Python

Olá! Nesse lab iremos utilizar o SQS, para integrar 2 scripts em Python. Um script irá receber as mensagens da fila e outro irá enviar as mensagens.

Usaremos o CloudShell para executar os comandos.

**Atenção:** sempre confira qual conta você efetuou login. O uso da conta na AWS é de sua inteira responsabilidade! Sempre que puder durante as etapas, faça prints da tela, para indicar que as concluiu com êxito.

## Passo 1 - Criar a fila do SQS

1 - Abra o console de gerenciamento da AWS e depois abra o CloudShell.

![aws-cloudshell1](/img/aws-cloudshell1.png)

2 - Copie o comando abaixo para um editor de texto, mude a parte de fila-nomesobrenome para colocar o seu nome e sobrenome. Depois, copie o comando que editou digitando CTRL+C e cole no CloudShell digitando CTRL+V ou clicando com o botão direito do mouse no meio do CloudShell e clicando em Colar. Este comando irá salvar esse nome para usarmos em seguida.

Exemplo: fila-rafaelteste

```
export SQS_NAME='fila-nomesobrenome'
```

**Dica:** sempre confira se os comandos estão sendo executados. Pode ocorrer de, ao colar o comando, precisar pressionar Enter em seguida para executar.

3 - Execute o comando abaixo, copiando e colando direto no CloudShell. Este comando irá criar uma fila do SQS, com o nome salvo anteriormente e irá armazenar a URL da fila no CloudShell mesmo em abas adicionais, que iremos utilizar nos scripts seguintes.

```
echo 'export SQS_QUEUE_URL='$(aws sqs create-queue \
    --queue-name $SQS_NAME \
    --attributes VisibilityTimeout=30,MessageRetentionPeriod=1800 \
    --query 'QueueUrl' --output text) >> ~/.bashrc && source ~/.bashrc
```

## Passo 2 - Baixar e executar os scripts Python

4 -  Execute também os comandos abaixo no CloudShell, para baixarmos os arquivos do lab e carregarmos a pasta baixada.
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

## Passo 3 - Excluir os recursos

12 - Para parar a execução do script, mantenha na primeira aba do CloudShell, onde foram mostradas as mensagens. Clique no meio onde aparecem os textos do CloudShell e pressione CTRL+C no teclado. Como alternativa, você pode clicar para fechar no X azul que aparece mais acima (ao lado de onde aparece o nome da região).

Após isso, exclua a fila do SQS executando o comando abaixo no CloudShell.
```
aws sqs delete-queue --queue-url $SQS_QUEUE_URL
```

13 - No CloudShell ainda, clique no botão azul Ações, clique para Excluir e, na mensagem que aparecer, confirme a exclusão.
Isso irá excluir apenas o ambiente do CloudShell que usamos, ou seja, tanto as variáveis de ambiente que configuramos quanto os arquivos baixados serão apagados.

![cloudshell-excluir-ambiente](/img/cloudshell-excluir-ambiente.PNG)

14 - Depois, feche o CloudShell.
Abra o serviço SQS na barra de pesquisa, clique no ícone de menu na parte de cima da tela e verifique se a fila que você criou foi excluída.

![sqs-tela](/img/sqs-tela.PNG)

15 - Se a sua fila foi excluída com sucesso, basta deslogar do console de gerenciamento da AWS, clicando no nome da sua conta no canto superior direito e no botão laranja Sair.

![aws-console2](/img/aws-console2.png)

Lab finalizado com sucesso!