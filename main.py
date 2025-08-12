from api.supabase_client import get_contatos
from api.zapi_client import send_mensagem

def main():
    contatos = get_contatos()
    if not contatos:
        print("Nenhum contato encontrado no Supabase.")
        return 
    
    for contato in contatos[:1]:
        send_mensagem(contato['numero'],contato['nome'])
      
if __name__ == "__main__":
    main()