import requests
from api.chaves import  TOKEN_ZAPI ,ID_ZAPI,CLIENT_TOKEN

def send_mensagem(phone_number, name):
    instance = ID_ZAPI
    client_token = CLIENT_TOKEN
    token = TOKEN_ZAPI
    url = f"https://api.z-api.io/instances/{instance}/token/{token}/send-text"
   
    headers = {
        "Content-Type": "application/json",
        "client-token": client_token
        }
    payload = {    
        "phone": phone_number,
        "message": f"Olá {name}, tudo bem com você?"        
        }
    
    try:
        response = requests.post(url,headers=headers,json=payload)
        response.raise_for_status()
        print(f"Mensagem enviada para {name} ({phone_number})")
    except requests.RequestException as e:
        print(f"Erro ao enviar mensagem para {name} ({phone_number}): {e}")