from funcs import SearchNewsletterEmail
import smtplib
from email.message import EmailMessage
import ssl

senderemail = "melhoramigonaoresponda@gmail.com"
password = "melhoramigonaoresponda1234"
message = EmailMessage()
message["From"] = senderemail
emails = SearchNewsletterEmail()
context = ssl.create_default_context()


def EnviarNewsletter():
    message = EmailMessage()
    message["From"] = senderemail
    for usuario in emails:
        email = usuario[0]
        nome = usuario[1]
        message["To"] = email
        html = f"""
<body>
  <div>
    <h1>Estamos com uma promocao inedita imperdivel pra voce {nome}</h1>
    <p>
      Apenas hoje!!!!! <br />
      Na compra de duas racoes premium para qualquer animal voce leva uma a mais
      totalmente de graca, isso mesmo totalmente de graca. <br />
      garanta a comida preparada com nosso carinho para seu pet hoje mesmo
      apenas no Melhor Amigo.
    </p>
  </div>
</body>

"""
        message["Subject"] = "Promocao imperdivel Melhor Amigo"
        message.add_alternative(html, subtype="html")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(senderemail, password)
            server.sendmail(senderemail, email, message.as_string())


EnviarNewsletter()
