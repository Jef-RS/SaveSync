from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import bd

# Cria a conexão com o banco de dados
Session = sessionmaker(bind=bd.engine)

# Cria a instância do Base
Base = declarative_base()

# Define a classe do modelo
class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    directory = Column(String)

# Cria o banco de dados
Base.metadata.create_all(bd.engine)

# Cria uma nova instância do Game
game = Game(name='Skyrin', directory='/caminho/do/jogo')

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
