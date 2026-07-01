from smtplib import SMTP #Bilioteca para envio de email
from email.message import EmailMessage #Biblioteca para as informações que contém no email, utilizamos o import para puxar uma parte especifica da biblioteca

email = "email_do_remetente@provedor.com"
receber = "email_do_recebedor@provedor.com"
senha = "senha_do_remetente" #senha de 16 digitos gerada pelo google sem espaços!


comunicado = EmailMessage() #nesse momento o meu programa sabe que a minha "mensagem" faz parte dessa biblioteca em especifico
comunicado['Subject'] = "Teste Do meu Projeto de Email" #o assunto do email
comunicado['From'] = email #aqui especificamos que quem vai enviar o email e o email que criamos de teste
comunicado['To'] = receber #aqui especificamos o email que vai receber a mensagem e que foi criado inicialmente 
comunicado.set_content("Essa e uma mensagem enviada diretamente pelo python!")
#essa parte de envio de mensagem em especifico nao pode ser entre [], por isso utilizamos o set content que define o texto em si

#Agora a parte do envio de carta/parte do servidor

#tente enviar 
try:
    with SMTP("smtp.gmail.com", 587) as servidor: #se usa ponto pois é o servidor do google
        servidor.starttls() #aqui inicialmente a conexão vai ser aberta e rapidamente se transformará em algo seguro enviando para uma pessoa especifica.
        servidor.login(email, senha) #faz o login com o email e senha teste
        servidor.send_message(comunicado) #Quando passamos a variavel comunicado, a biblioteca extrai os 3 topicos (subject, from e to)
        print("E-mail Enviado Corretamente! Tudo okay")

except Exception as erro:
    #se encontrar qualquer erro!
    print("Ops deu algum erro no programa e o email nao foi enviado!")
