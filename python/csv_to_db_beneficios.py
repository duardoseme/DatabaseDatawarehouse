import pandas as pd
from sqlalchemy import create_engine

def import_csv_to_mysql(csv_file, table_name):
    df = pd.read_csv(csv_file, sep=';', encoding='utf-8')
    df.fillna('', inplace=True)

    engine = create_engine('mysql+pymysql://root:root@localhost:3306/db_beneficios')

    try:
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
        print(f"Dados inseridos na tabela {table_name} com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir dados na tabela {table_name}: {e}")


import_csv_to_mysql('../db-beneficios/tb_empresa.csv', 'tb_empresa')
import_csv_to_mysql('../db-beneficios/tb_beneficio.csv', 'tb_beneficio')
