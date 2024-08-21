'''
1. Criação das Tabelas:
- Utilizando SQL, crie as tabelas necessárias para armazenar as
informações do sistema. Certifique-se de definir as chaves primárias e
estrangeiras conforme apropriado.

(talvez mudar os nomes das tabelas para terem inicial minuscula)
'''

import conexao as conn

#Tabela livros
conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id_livro INTEGER PRIMARY KEY,
        titulo VARCHAR(255) NOT NULL,
        editora VARCHAR(255) NOT NULL,
        num_max_renovacoes INTEGER
    );
''') 

#Tabela generos
conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS generos (
        id_genero INTEGER PRIMARY KEY,
        nome VARCHAR(255) NOT NULL
    );
''') 

#Tabela livros_generos - relacao muitos para muitos
conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros_autores (
        id_livro INTEGER NOT NULL,
        id_genero INTEGER NOT NULL,
        PRIMARY KEY (id_livro, id_genero),
        FOREIGN KEY (id_livro) REFERENCES livros(id_livro) ON DELETE NO ACTION ON UPDATE NO ACTION
        FOREIGN KEY (id_genero) REFERENCES generos(id_genero) ON DELETE NO ACTION ON UPDATE NO ACTION
    );
''')

#Tabela exemplares
conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS exemplares (
        id_exemplar INTEGER PRIMARY KEY,
        id_livro INTEGER,
        FOREIGN KEY (id_livro) REFERENCES livros(id_livro)
    );
''') 

#Tabela pessoas
conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id_pessoa INTEGER PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    );
''')

#Tabela usuarios - herda de pessoa
conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER NOT NULL,
        id_pessoa INTEGER NOT NULL,
        telefone INTEGER NOT NULL,
        nacionalidade VARCHAR(200) NOT NULL
        PRIMARY KEY (id_usuario, id_pessoa),
        FOREIGN KEY (id_pessoa) REFERENCES pessoas(id_pessoa) ON DELETE NO ACTION ON UPDATE NO ACTION
    );
''')

#Tabela autores - herda de pessoa
conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS autores (
        id_autor INTEGER NOT NULL,
        id_pessoa INTEGER NOT NULL,
        PRIMARY KEY (id_autor, id_pessoa),
        FOREIGN KEY (id_pessoa) REFERENCES pessoas(id_pessoa) ON DELETE NO ACTION ON UPDATE NO ACTION
    );
''')

#Tabela autores_livros (pela relação muitos para muitos)
conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS autores_livros (
        id_autor INTEGER NOT NULL,
        id_livro INTEGER NOT NULL,
        id_pessoa INTEGER NOT NULL,
        PRIMARY KEY (id_autor, id_livro, id_pessoa),
        FOREIGN KEY (id_livro) REFERENCES livros(id_livro) ON DELETE NO ACTION ON UPDATE NO ACTION
        FOREIGN KEY (id_autor, id_pessoa) REFERENCES autores(id_autor, id_pessoa) ON DELETE NO ACTION ON UPDATE NO ACTION
    );
''')

conn.conexao.commit()
conn.conexao.close()