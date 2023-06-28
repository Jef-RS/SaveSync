from sqlalchemy import create_engine, MetaData
import os

diretório = os.path.dirname(__file__)
dir_absp = diretório[:-4]

print(dir_absp)
dir_backend_utils = dir_absp

def mostrar_todos_os_registros():
    # Criando a engine de conexão com o banco de dados
    engine = create_engine(f'sqlite:///{dir_backend_utils}data/database.db')

    # Criando um objeto MetaData
    metadata = MetaData()

    # Carregando as informações das tabelas
    metadata.reflect(bind=engine)

    # Obtendo a tabela desejada
    sua_tabela = metadata.tables['games']

    # Executando uma consulta para obter todos os registros da tabela
    conn = engine.connect()
    registros = conn.execute(sua_tabela.select()).fetchall()

    # Exibindo os registros
    for registro in registros:
        print(registro)

    # Fechando a conexão
    conn.close()
mostrar_todos_os_registros()