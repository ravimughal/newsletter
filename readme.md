<img src="./img/nws.png" width='150px' style='margin: 0 auto; display: flex' />

# NWS letter

## Descrição do Projeto
<p> O script em Python de Envio Automatizado de Newsletters por E-mail oferece uma maneira eficaz e automatizada de enviar boletins informativos para uma lista de assinantes. </p>

<div style="display: flex; align-items: center;">
  <img src='https://simpleicons.org/icons/python.svg' width='50px' style='display: flex; margin-right: 15px'>
  <h1 style='margin-right:15px'>.</h1>
  <img src="https://img.shields.io/static/v1?label=license&message=MIT&color=7159c1&style=flat-square">
  <img src="https://img.shields.io/static/v1?label=py&message=3.9.13&color=7159c1&style=flat-square" style='margin-left:10px'>
</div>

<br>

Tabela de conteúdos
=================
<!--ts-->


- [NWS letter](#nws-letter)
  - [Descrição do Projeto](#descrição-do-projeto)
- [Tabela de conteúdos](#tabela-de-conteúdos)
- [Sobre](#sobre)
- [Instalação](#instalação)
- [Como usar](#como-usar)
  - [Pre Requisitos](#pre-requisitos)
- [Tecnologias](#tecnologias)
<!--te-->

<br>

<a id='sobre'></a>

# Sobre

O script Python automatiza o envio de newsletters por e-mail para uma lista de assinantes. Ele usa a API do Gmail para criar e enviar e-mails personalizados a partir de um remetente definido, para destinatários em um arquivo CSV. Com uma interface gráfica, os usuários inserem assunto e conteúdo, que são enviados a todos os assinantes. O script lida com erros e simplifica a comunicação com os assinantes, tornando o compartilhamento de informações eficiente e personalizado.


# Instalação

1. instale o <a href='https://www.python.org/downloads'>python</a> 

2. verifique a instalção no ***Prompt de Comando**** digitando:
    ```
    python3
    ```

3. Clone o repositório
    ```console
    # clone the repo
    $ git clone https://github.com/ravimughal/newsletter.git
    ```

4. Acessar o Console de Desenvolvedor do Google:
Acesse https://console.developers.google.com/ e faça login na sua conta do Google.

5. Criar um Novo Projeto:
No Console de Desenvolvedor, clique no botão "Selecione um projeto" no canto superior esquerdo e, em seguida, clique em "Novo Projeto". Dê um nome ao projeto e selecione as opções apropriadas. Clique em "Criar".

6. Ativar a API do Gmail:
No painel do projeto, clique em "Ativar APIs e serviços". Procure por "Gmail" e clique em "Gmail API". Em seguida, clique no botão "Ativar".

7. Criar Credenciais:
No menu lateral, clique em "Credenciais". Depois, clique em "Criar credenciais" e escolha "ID do Cliente OAuth". Selecione "Aplicativo da Área de Trabalho" como o tipo de aplicativo.

8. Configurar as Credenciais:
Preencha os detalhes do aplicativo, como nome e ícone. Nas URLs de redirecionamento autorizadas, você pode adicionar "http://localhost" para fins de teste. Clique em "Criar" para criar as credenciais.

9. Fazer o Download das Credenciais:
Na lista de credenciais, você verá a nova credencial que foi criada. Clique no ícone de download ao lado dela para baixar o arquivo JSON contendo as informações de autenticação.

10. Utilizar as Credenciais:
No seu código, você pode utilizar o arquivo JSON de credenciais para autenticar sua aplicação e acessar a API do Gmail. Pegue o arquivo 'path_to_credentials.json' e passe para a pasta da NEWSLETTER

1.  No Código substitua em ***main.py*** o _testedasilvafilho@gmail.com_ pelo seu email
    ```
    sender_email = 'testedasilvafilho@gmail.com' 
    ```

    Substitua em ***email_utils.py*** pelo seu email também
    ```
    if sender == 'testedasilvafilho@gmail.com':
    ```
    

# Como usar

1. Procure o diretorio newsletter no seu Prompt de Comando e execute o ***main.py*** (<a href='https://medium.com/@adsonrocha/como-abrir-e-navegar-entre-pastas-com-o-prompt-de-comandos-do-windows-10-68750eae8f47'>como navegar pelo Prompt de Comando</a>)
    ```
    C:\Users\Ravim\Desktop>cd newsletter
    C:\Users\Ravim\Desktop\newsletter>python main.py
    ```

2. Escreva o *Assunto* e a *Mensagem* do email que serão enviados para os emails em ***lista_assinantes.csv***

    <img src='./img/envio do email.png'/>

3. Acesse a conta do email cadastrada na instalação.

## Pre Requisitos

1. Conta no <a href='https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AXo7B7VvjglutmmcYtQBTfc763EW8kgXTO2PBr_P3i5KaouLpyK_mngVXMjjPkB6hlSDJWb8eXUnaA&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1962252387%3A1693370731362858'>GMAIL</a>
2. Python instalado na sua maquina. <a href='https://www.python.org/downloads/'>(Clique aqui) </a>

# Tecnologias

<div style='display: flex;'>
    <img src='https://simpleicons.org/icons/gmail.svg' width='100px'/>
    <img src='https://simpleicons.org/icons/python.svg' width='100px' style='margin-left: 15px'/>
</div>

<br>
<br>

<h4 align='center'> EM DESENVOLVIMENTO 🚧 </h4>