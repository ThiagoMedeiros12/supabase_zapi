from chaves import SUPABASE_URL,KEY
from supabase import create_client, Client



def get_contatos():
    url = SUPABASE_URL
    key = KEY
        
    
    supabase: Client = create_client(url, key)

    data = supabase.table('contatos').select('*').execute()

    return data.data

print(get_contatos())
