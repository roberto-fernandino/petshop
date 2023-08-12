from usuarios.funcs import SearchNewsletterEmail
import smtplib
from email.message import EmailMessage

# informacoes do smtp, apikeys
api_key = "93756b68ede318c14f2b66e96dae6d15"
api_secret_key = "ddf300ee85d972be1c77816c593ee096"
email_sender = "melhoramigonaoresponda@gmail.com"


def EnviarNewsletter() -> None:
    '''Acha emails validos com is_newsletter em todo o banco de dados e envia o newsletter selecionado em ->
    with open(
    "diretorio do template",
    "r"
    ) as htmlmodel: '''
    emails = SearchNewsletterEmail()

    with smtplib.SMTP("in-v3.mailjet.com", 587) as server:
        server.starttls()
        server.login(api_key, api_secret_key)
        for usuario in emails:
            email = usuario[0]
            nome = usuario[1]
            message = EmailMessage()
            message["Subject"] = "Promocao imperdivel Melhor Amigo"
            message["From"] = "melhoramigonaoresponda@gmail.com"
            message["To"] = email
            with open(
                "/home/roberto/projects/petshop/src/usuarios/emailstemplate/newsletter1.html",
                "r",
            ) as htmlmodel:
                html = htmlmodel.read()
            message.add_alternative(html, subtype="html")
            try:
                server.send_message(message)
                print(f"Email enviado com sucesso para {email}! (200 OK)")
            except Exception as e:
                print(f"Erroa o enviar email, ERRO: {e}")


def EnviaNewsLetterFromDataBase(inquerylist: list) -> None:
    '''Envia emails de newsletter para emails selecionados no admin panel'''
    with smtplib.SMTP("in-v3.mailjet.com", 587) as server:
        server.starttls()
        server.login(api_key, api_secret_key)
        for tuplas in inquerylist:
            email = tuplas[0]
            nome = tuplas[1]
            message = EmailMessage()
            message["Subject"] = "Promocao imperdivel Melhor Amigo"
            message["From"] = "melhoramigonaoresponda@gmail.com"
            message["To"] = email
            with open(
                "/home/roberto/projects/petshop/src/usuarios/emailstemplate/newsletter1.html",
                "r",
            ) as htmlmodel:
                html = htmlmodel.read()
            message.add_alternative(html, subtype="html")
            try:
                server.send_message(message)
            except Exception as e:
                print(f"erro: {e}")

def EnviaSigunupEmail(email, username) -> str:
    '''Envia emails para usuarios novos cadastrados'''
    with smtplib.SMTP("in-v3.mailjet.com", 587) as server:
        server.starttls()
        server.login(api_key, api_secret_key)
        message = EmailMessage()
        message["Subject"] = f"Bem vindo ao Melhor Amigo Petshop {username}"
        message["From"] = email_sender
        message['To'] = email
        with open('/home/roberto/projects/petshop/src/usuarios/emailstemplate/SIGNUPPETSHOP.html', 'r') as htmlmodel:
            html = htmlmodel.read()
        message.add_alternative(html, subtype="html")
        try:
            server.send_message(message)
        except Exception as e:
            return f"EMAIL ERROR LOG : {e}"