from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import re
import requests
import json
from pymongo import MongoClient

# PEGANDO O HTML DO SITE PARA PEGAR AS URLS
url = 'https://grupoutah.com.br/'
request = requests.get(url)
html = request.text


# REGEX PARA PEGAR AS URLS
sites = (re.findall(r'\bhref="https://\w+\.\w+\.\w+\.\w+/\w+', html))


# TRANSFORMANDO A LISTA EM JSON
urls = json.dumps(sites)


# TRANSFORMANDO A LISTA EM DICIONÁRIO
dicionario = {"url":[]}
dicionario["url"].append(urls)
print(dicionario)


# INPUT PARA EVIAR O E-MAIL JUNTO DA SENHA
email = 'luc.pedro.lea@outlook.com'
password = 'senha123'


def send_email(email, password):
    # CRIANDO UM CORPO PARA O E-MAIL (mime do json/mensagem, mime do assunto, destinatário e remetente)
    content_email = urls
    subject = 'Aqui esta as URLS do website scanneado.'
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = subject
    body = MIMEText(content_email, urls)
    msg.attach(body)

    # FAZENDO O ENVIO DO E-MAIL
    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls()
    server.login(email, password)
    server.send_message(msg, from_addr=email, to_addrs=[email])
    server.quit()
send_email(email, password)



connection = 'mongodb+srv://fiapuser:senha123@rm96036.ezuf3fx.mongodb.net/test'
client = MongoClient(connection)
db = client.cp4
collection = db.rm96036
collection.insert_one(dicionario)
