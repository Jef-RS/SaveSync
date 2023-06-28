import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os

diretório = os.path.dirname(__file__)
name_arq = os.path.basename(diretório)
diretório_raiz = diretório[:-8]

# Cria a conexão com o banco de dados
print(f'Diretório do Banco de dados {diretório_raiz}')

# Inicializar o SDK do Firebase
cred = credentials.Certificate(f"{diretório_raiz}firebase/firebase.json")
firebase_admin.initialize_app(cred)

# Obtenha a URL do banco de dados de uma variável de ambiente
database_url = os.environ.get('FIREBASE_DATABASE_URL')

if database_url:
    # Referência para o nó "dados" no banco de dados
    ref = db.reference(database_url)

    # Dados a serem salvos
    dados = {
        'username': 'admin',
    }

    # Salvar os dados no banco de dados
    ref.set(dados)
else:
    print("A variável de ambiente FIREBASE_DATABASE_URL não está definida.")


