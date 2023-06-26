from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Diretório do Bd
dir_atual = os.getcwd()
dir_backend = f'{dir_atual}/Backend'

# Cria a conexão com o banco de dados

engine = create_engine(f'sqlite:///{dir_backend}/data/database.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)


# Define a classe do modelo do Game
class Game(Base):
    __tablename__ = 'games'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    directory = Column(String)




def read_games():
    # Inicia uma nova sessão
    session = Session()
    
    try:
        # Consulta todos os jogos
        games = session.query(Game).all()
        
        # Imprime os jogos encontrados
        for game in games:
            print(f"ID: {game.id}, Nome: {game.name}, Diretório: {game.directory}")
        
    except Exception as e:
        print("Erro ao ler os jogos:", str(e))
    finally:
        # Fecha a sessão
        session.close()



read_games()

def delete_database():
    # Obtém uma nova sessão
    session = Session()

    try:
        # Deleta todas as tabelas do banco de dados
        Base.metadata.drop_all(bind=engine)

        print("Banco de dados apagado com sucesso!")
    except Exception as e:
        print("Erro ao apagar o banco de dados:", str(e))
    finally:
        # Fecha a sessão
        session.close()


#delete_database()