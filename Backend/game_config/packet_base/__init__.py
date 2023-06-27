from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

import os

diretório = os.path.dirname(__file__)
name_arq = os.path.basename(diretório)
dir_absp = diretório[:-17]

dir_backend_utils = dir_absp

# Cria a conexão com o banco de dados
print(dir_backend_utils)
engine = create_engine(f'sqlite:///{dir_backend_utils}/data/database.db')
Session = sessionmaker(bind=engine)


Base = declarative_base()


# Define a classe do modelo
class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    directory = Column(String)

def adicionar_games_bd(game, diretório):
    # Cria a conexão com o banco de dados
    Session = sessionmaker(bind=engine)

    # Cria o banco de dados
    Base.metadata.create_all(engine)

    # Cria uma nova instância do Game
    game = Game(name=f'{Game}', directory=f'{diretório}')

    # Inicia uma nova sessão
    session = Session()

    try:
        # Adiciona o jogo à sessão
        session.add(game)

        # Salva as mudanças no banco de dados
        session.commit()

        print("Jogo criado e salvo com sucesso!")
    except Exception as e:
        # Em caso de erro, faz rollback na transação
        session.rollback()

        print("Erro ao criar e salvar o jogo:", str(e))
    finally:
        # Fecha a sessão
        session.close()

#adicionar_games_bd('teste', 'teste')