from sqlalchemy import create_engine, MetaData, Table
import bd
# Criar uma instância do engine e conectar ao banco de dados
engine = create_engine(f'sqlite:///{bd.caminho_banco_dados}')

# Criar uma instância do objeto MetaData e vinculá-la ao engine
metadata = MetaData(bind=engine)

# Definir uma tabela existente no banco de dados
tabela = Table('nome_da_tabela', metadata, autoload=True)

# Criar uma conexão
with engine.connect() as connection:
    # Selecionar todos os registros da tabela
    select_statement = tabela.select()
    result_set = connection.execute(select_statement)

    # Iterar sobre os registros e imprimir os dados
    for row in result_set:
        print(row)
