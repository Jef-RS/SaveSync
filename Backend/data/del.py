from sqlalchemy import create_engine
import bd


try:
    with bd.engine.connect() as conn:
        conn.execute(f'DELETE FROM Games')
except:
    print("Não existe essa tabela {}")