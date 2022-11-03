import requests
from pyfiglet import Figlet
from termcolor import colored

def titulo():
    Titulo = Figlet(font='slant')
    print(colored(Titulo.renderText("INSTAGRAM COPY"), ("blue")))

access_token = "EAARZCRrjye0MBALD4ep0ZCfbh9gZAhKBrlrH5ZAmmVZC3eexgwXD62LZBi2fPMwmqGHtZAc58jrV17KrqSrHkE8EbmXVlY9kCW87dMIilSnjZBWqOwyQ0RnZC22KTO4RtbG9N7Iok8KqWeBzpiJGOkqP8Q4D1ISvOGs2ZCc3ZBoZAxFNTNO0bDcqPKRsLrcBn7gJrZBscu2gwFv7lZAUmLOvc52Ak4"
pageID = "101926902693609"
link_foto = str("Digite a URL da foto:")
legenda = str("Digite a legenda: ")

request = requests.get(f"https://graph.facebook.com/v15.0/{pageID}?fields=instagram_business_account&access_token={access_token}")
instagramID = request.json()["instagram_business_account"]["id"]
request = requests.get(f"https://graph.facebook.com/v14.0/{instagramID}?fields=media%2Cfollowers_count%2Cfollows_count%2Cusername%2Cname&access_token={access_token}")
resposta = request.json()

if request.status_code == 200:
    nome = resposta["name"]
    nomeusuario = resposta["username"]
    seguidores = resposta["followers_count"]
    seguindo = resposta["follows_count"]

    print("\033[1m DADOS DO USUÁRIO \033[m")
    print(F"NOME DE USUÁRIO: \033[1m{nome}\033[m")
    print(F"NOME DA CONTA: \033[1m{nomeusuario}\033[m")
    print(F"SEGUIDORES: \033[1m{seguidores}\033[m")
    print(F"SEGUINDO: \033[1m{seguindo}\033[m")

else:
    print(f" ERRO - STATUS CODE: {request.status_code} " )


request = requests.post(f"https://graph.facebook.com/v14.0/{instagramID}/media?image_url={link_foto}&caption={legenda}&access_token={access_token}")
print(request)


imageID = request.json()["id"]
request2 = requests.post(f"https://graph.facebook.com/v14.0/{instagramID}/media_publish?creation_id={imageID}&access_token={access_token}")


