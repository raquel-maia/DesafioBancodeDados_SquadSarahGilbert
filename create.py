import conexao as conn

conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id_livro INTEGER PRIMARY KEY,
        titulo VARCHAR(255) NOT NULL,
        editora VARCHAR(255) NOT NULL
    )
''') 

conn.conexao.commit()
conn.conexao.close()