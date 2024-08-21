'''
1. Criação das Tabelas:
- Utilizando SQL, crie as tabelas necessárias para armazenar as
informações do sistema. Certifique-se de definir as chaves primárias e
estrangeiras conforme apropriado.
'''

import conexao as conn

# Tabela livros
conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id_livro INTEGER PRIMARY KEY,
        titulo VARCHAR(255) NOT NULL,
        editora VARCHAR(255) NOT NULL
    );
''') 


# Tabela exemplares
conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS exemplares (
        ExemplarID INT PRIMARY KEY
        ,id_livro INT
        ,FOREIGN KEY (id_livro) REFERENCES livros(id_livro)
    );
''') 

conn.conexao.commit()
conn.conexao.close()