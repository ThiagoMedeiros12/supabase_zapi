# Aplicação de Automação Utilizando Supabase e Z-API

Este projeto é composto por 3 etapas principais:

- **Banco de dados** utilizando Supabase  
- **Z-API** para envio das mensagens  
- **Python** para integração e execução  

---

## Supabase

Para criar o banco de dados no Supabase, é necessário registrar uma conta e criar uma tabela.  
No meu caso, utilizei uma tabela com 3 campos:

- **id** — tipo: `uuid`, chave aleatória  
- **nome** — tipo: `text`, não permite `null` e valor padrão  
- **numero** — tipo: `text`, não permite `null`e valor padrão  

Após criar a tabela, foi necessário **desabilitar o RLS** (*Row Level Security*).  

Para localizar as chaves da API necessárias para o projeto:  
1. No painel, clique em **API Docs** no menu **Tables and Views**.  
2. Localize o nome da tabela criada.  
3. Na aba, procure por **Read rows**.  
4. Selecione a opção **bash** no canto superior direito e clique em **Hide keys**.  
5. Escolha **service_role** — assim você terá acesso à sua **API Key**.  

No meu projeto, salvei essa chave em um arquivo chamado `chaves.py` (não incluído neste repositório).  

Crie um arquivo `chaves.py` e defina as seguintes variáveis:

```python
SUPABASE_URL = "https://dkoawgndschrvbqojibl.supabase.co"
KEY = "sua_apikey_aqui"
```

# Z-API

1. Crie uma conta em [Z-API](https://www.z-api.io/).  
2. Após o cadastro, acesse **Instâncias Web** e clique em **+ Adicionar** para criar uma nova instância — atribua um nome a ela.  
3. Quando a instância for criada, selecione-a para visualizar o **ID da instância** e o **token**.

No projeto, essas duas chaves são definidas no arquivo `chaves.py`:

```python
TOKEN_ZAPI = "seu_token_aqui"
ID_ZAPI = "id_da_instancia_aqui"
``` 
> **Observação:** vale ressaltar que a versão *trial* possui validade de pouco mais de dois dias.

## Utilização

Para executar o projeto, siga os passos abaixo:

1. Faça login no Z-API e acesse **Instâncias Web**.  
2. Selecione a instância desejada e registre o WhatsApp que será usado para o envio automático das mensagens.  
3. No projeto está configurada uma mensagem no formato:

```python
"Olá {nome}, tudo bem com você?"
```

Essa mensagem será enviada automaticamente para os 3 primeiros contatos armazenados no Supabase.




