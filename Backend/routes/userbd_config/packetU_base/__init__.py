from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

import os

diretório = os.path.dirname(__file__)
name_arq = os.path.basename(diretório)
dir_backend = diretório[:-33]
dir_frontend = f'{dir_backend[:-8]}Frontend/static/images/profile_image/*'
print(f'Diretório para banco de dados USERBASE {f"{dir_backend}data/database.db"}')
print('Diretório para o banco de dados APP:', dir_frontend)

# Cria a conexão com o banco de dados

engine = create_engine(f'sqlite:///{dir_backend}data/database.db')
Session = sessionmaker(bind=engine)


Base = declarative_base()


# Define a classe do modelo
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    image = Column(String)


def adicionar_users_bd(user, password):
    # Cria a conexão com o banco de dados
    Session = sessionmaker(bind=engine)

    # Cria o banco de dados
    Base.metadata.create_all(engine)

    # Cria uma nova instância do Game
    users = User(username=user, password=password, image=dir_frontend)

    # Inicia uma nova sessão
    session = Session()

    try:
        # Adiciona o jogo à sessão
        session.add(users)
        
        # Salva as mudanças no banco de dados
        session.commit()

        print('Usuario criado e salvo com sucesso!')
    except Exception as e:
        # Em caso de erro, faz rollback na transação
        session.rollback()

        print('Erro ao criar e salvar o usuario:', str(e))
    finally:
        # Fecha a sessão
        session.close()

#adicionar_users_bd('admin', '123')
