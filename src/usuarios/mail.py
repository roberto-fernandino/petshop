from pathlib import Path
from typing import List
from usuarios.funcs import SearchNewsletterEmail
import smtplib
from email.message import EmailMessage
import os
import ttkbootstrap as ttk
import tkinter as tk

# declara BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# informacoes do smtp, apikeys
api_key = "93756b68ede318c14f2b66e96dae6d15"
api_secret_key = "ddf300ee85d972be1c77816c593ee096"
email_sender = "melhoramigonaoresponda@gmail.com"


def procura_email_template() -> str:
    emails = os.listdir(f"{BASE_DIR}/usuarios/emailstemplate")
    return emails


def EnviarNewsletter() -> None:
    """Acha emails validos com is_newsletter em todo o banco de dados e envia o newsletter selecionado em ->
    with open(
    "diretorio do template",
    "r"
    ) as htmlmodel:"""
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
                BASE_DIR / "usuarios/emailstemplate/newsletter1.html",
                "r",
            ) as htmlmodel:
                html = htmlmodel.read()
            message.add_alternative(html, subtype="html")
            try:
                server.send_message(message)
                print(f"Email enviado com sucesso para {email}! (200 OK)")
            except Exception as e:
                print(f"Erroa o enviar email, ERRO: {e}")


class Selector:
    """Objeto tela -> feito com ttkbootstrap, um selector que retorna o valor selecionado"""

    def __init__(
        self,
        templates: List[str],
        height: str = "300",
        width: str = "300",
        title: str = "Selector",
    ) -> None:
        self.root = tk.Tk()
        self.root.geometry(f"{height}x{width}")
        self.root.resizable(False, False)
        self.root.title(title)
        self.template_selecionado = tk.StringVar()

        texto_informativo = ttk.Label(self.root, text="Selecione o template")
        combobox = ttk.Combobox(
            self.root,
            bootstyle="dark",
            state="readonly",
            textvariable=self.template_selecionado,
        )
        combobox["values"] = templates
        botao_enviar = ttk.Button(self.root, text="Enviar", command=self.salva_e_fecha)
        texto_informativo.place(x=40, y=40)
        combobox.place(x=40, y=70)
        botao_enviar.place(x=40, y=120)

    def salva_e_fecha(self):
        template = self.template_selecionado.get()
        self.root.destroy()
        self.template_selecionado.set(template)

    def start_tk(self):
        self.root.mainloop()
        return self.template_selecionado.get()


"""def on_enviar_click(self):
    template = template_selecionado.get()
    root.destroy()
    template_selecionado.set(template)


def start_tk():
    global template_selecionado, root

    root = tk.Tk()
    root.geometry("300x300")
    root.resizable(False, False)
    root.title("Selecione template")
    template_selecionado = tk.StringVar()

    combobox = ttk.Combobox(
        root, bootstyle="dark", state="readonly", textvariable=template_selecionado
    )

    templates_arquivo = procura_email_template()
    combobox["values"] = templates_arquivo
    combobox.place(x=50, y=50)

    botao_enviar = ttk.Button(
        root, text="Enviar", bootstyle="sucess", command=on_enviar_click
    )
    botao_enviar.place(x=50, y=80)

    root.mainloop()
    return template_selecionado.get()"""


def EnviaNewsLetterFromDataBase(inquerylist: list) -> None:
    """Envia emails de newsletter para emails selecionados no admin panel"""

    with smtplib.SMTP("in-v3.mailjet.com", 587) as server:
        server.starttls()
        server.login(api_key, api_secret_key)

        selector = Selector(procura_email_template())
        template = selector.start_tk()
        print(template)
        for tuplas in inquerylist:
            email = tuplas[0]
            message = EmailMessage()
            message["Subject"] = "Promocao imperdivel Melhor Amigo"
            message["From"] = "melhoramigonaoresponda@gmail.com"
            message["To"] = email
            with open(
                BASE_DIR / f"usuarios/emailstemplate/{template}",
                "r",
            ) as htmlmodel:
                html = htmlmodel.read()
            message.add_alternative(html, subtype="html")
            try:
                server.send_message(message)
            except Exception as e:
                print(f"erro: {e}")


def EnviaSigunupEmail(email, username) -> str:
    """Envia emails para usuarios novos cadastrados"""
    with smtplib.SMTP("in-v3.mailjet.com", 587) as server:
        server.starttls()
        server.login(api_key, api_secret_key)
        message = EmailMessage()
        message["Subject"] = f"Bem vindo ao Melhor Amigo Petshop {username}"
        message["From"] = email_sender
        message["To"] = email
        with open(
            BASE_DIR / "usuarios/emailstemplate/SIGNUPPETSHOP.html", "r"
        ) as htmlmodel:
            html = htmlmodel.read()
        message.add_alternative(html, subtype="html")
        try:
            server.send_message(message)
        except Exception as e:
            return f"EMAIL ERROR LOG : {e}"
