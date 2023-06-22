from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import os

diretorio_atual = os.getcwd()
caminho_banco_dados = os.path.join(diretorio_atual, 'data/banco_de_dados.db')
engine = create_engine(f'sqlite:///{caminho_banco_dados}')

Base = declarative_base()

class Game(Base):
    __tablename__ = 'Games'
    id = Column(Integer, primary_key=True)
    nome_do_game = Column(String)
    diretorio_do_game_save = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
Game1 = Game(nome_do_game={'teste'} , diretorio_do_game_save={'teste'})
Game2 = Game(nome_do_game= {'teste'}, diretorio_do_game_save={'teste'})

session.add(Game1)
#session.add(Game2)

session.commit()

pessoas = session.query(Game).all()

for Game in pessoas:
    print(Game.nome_do_game, Game.diretorio_do_game_save)
