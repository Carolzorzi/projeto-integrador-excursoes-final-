import sqlite3

# ATENÇÃO: Se o nome da variável no seu app.py não for 'banco.db',
# mude o nome aqui embaixo para o nome do seu arquivo de banco.
DB_NAME = "banco.db"

try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Executa o comando para adicionar a nova coluna
    cursor.execute("ALTER TABLE viagens ADD COLUMN mensagem_whatsapp TEXT;")

    conn.commit()
    print("Sucesso! A coluna 'mensagem_whatsapp' foi adicionada com sucesso.")
except sqlite3.OperationalError:
    print("Aviso: A coluna já existe ou o nome do arquivo de banco (.db) está incorreto.")
finally:
    conn.close()