from sqlalchemy import create_engine
import bd
engine = create_engine(f'sqlite:///{bd.caminho_banco_dados}')

with engine.connect() as conn:
    conn.execute('DELETE FROM pessoas')
