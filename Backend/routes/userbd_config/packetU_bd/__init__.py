from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Diretório do Bd
diretório = os.path.dirname(__file__)
name_arq = os.path.basename(diretório)
diretório_raiz = diretório[:-31]

# Cria a conexão com o banco de dados
print(f'Diretório do Banco de dados {diretório_raiz}data/database.db')
engine = create_engine(f'sqlite:///{diretório_raiz}data/database.db')


Base = declarative_base()
Session = sessionmaker(bind=engine)


# Define a classe do modelo do Game
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


def read_users():
    # Inicia uma nova sessão
    session = Session()
    usuarios_salvos = []
    
    try:
        # Consulta todos os usuarios
        users = session.query(User).all()

        # Imprime os usuarios encontrados
        for user in users:
            usuarios_salvos.append({'username': user.username, 'password': user.password})

    except Exception as e:
        print('Erro ao ler os usuários:', str(e))
    finally:
        # Fecha a sessão
        session.close()
    print(usuarios_salvos)
    return usuarios_salvos
    
read_users()


def delete_database():
    # Obtém uma nova sessão
    session = Session()

    try:
        # Deleta todas as tabelas do banco de dados
        Base.metadata.drop_all(bind=engine)

        print('Banco de dados apagado com sucesso!')
    except Exception as e:
        print('Erro ao apagar o banco de dados:', str(e))
    finally:
        # Fecha a sessão
        session.close()


#delete_database()
