import requests
from chaves import  TOKEN_ZAPI ,ID_ZAPI

def send_mensagem(phone_number, name):
    instance = ID_ZAPI
    token = TOKEN_ZAPI
    url = f"https://api.z-api.io/{instance}/3E59DCAA06CBF06B9EE9C200745B43DD/{token}/4D7BBDCFE51B42D8AE1065DA/send-text"
    payload = {
        "phone": phone_number,
        "message": f"Olá {name}, tudo bem com você?"        
        }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print(f"Mensagem enviada para {name} ({phone_number})")
    except requests.RequestException as e:
        print(f"Erro ao enviar mensagem para {name} ({phone_number}): {e}")