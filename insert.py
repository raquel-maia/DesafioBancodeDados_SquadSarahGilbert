'''
2. Inserção de Dados:
- Insira dados de exemplo nas tabelas para simular um ambiente de
biblioteca. Certifique-se de incluir uma variedade de livros, autores e
editoras.
'''

import conexao as conn

# Tabela livros
conn.cursor.execute('''
    INSERT INTO livros (id_livro, titulo, editora, num_max_renovacoes) VALUES 
        (1, "The StatQuest Illustrated Guide to Machine Learning!!!", "Packt Publishing", 3),
        (2, "Código Limpo: Habilidades Práticas do Agile", "Alta Books", 4),
        (3, "Introdução à Programação com Python", "Novatec", 3),
        (4, "Python para Data Science", "Alta Books", 2),
        (5, "Algoritmos e Programação de Computadores", "GEN LTC", 4);       
''')

"""# Tabela generos
conn.cursor.execute('''
    INSERT INTO generos (id_genero, nome) VALUES 
        ( , ""),
        ( , "");       
''')

# Tabela livro_generos
conn.cursor.execute('''
    INSERT INTO livros_generos (id_livro, id_genero) VALUES 
        ( , ),
        ( , );       
''')

# Tabela exemplares
conn.cursor.execute('''
    INSERT INTO exemplares (id_exemplar, id_livro) VALUES 
        ( , ),
        ( , );       
''')
"""
# Tabela pessoas
conn.cursor.execute('''
    INSERT INTO pessoas (id_pessoa, nome, email) VALUES 
        (1, "Jéssica Lizar", "jessicalizar@gmail.com"),
        (2, "Letícia Almeida", "leticiaalmeida@gmail.com"),
        (3, "Lívia Boscolo", "liviaboscolo@gmail.com"),
        (4, "Michelle Martins", "michellemartins@gmail.com"),
        (5, "Nadiveth Duno", "nadivethduno@gmail.com"),
        (6, "Raquel Maia", "raquelmaaia@gmail.com"),
        (7, "Rosana Francisco", "rosanafrancisco@gmail.com"),
        (8, "Josh Starmer", "joshstamer@gmail.com"),
        (9, "Robert C. Martin", "robertmartin@gmail.com"),
        (10, "Nilo Ney Coutinho", "neycoutinho@gmail.com"),
        (11, "Henrique Bastos", "henriquebastos@gmail.com"),
        (12, "An Engelbrecht", "anengelbrecht@gmail.com"),
        (13, "Gilberto Nakamiti", "gilbertonakamiti@gmail.com"),
        (14, "Dilermando Junior", "dilermandojr@gmail.com");     
''')

# Tabela usuarios
conn.cursor.execute('''
    INSERT INTO usuarios (id_usuario, id_pessoa, telefone, nacionalidade) VALUES 
        (1, 1, "12345678910", "Brasileira"),
        (2, 2, "10987654321", "Brasileira"),
        (3, 3, "12345109876", "Brasileira"),
        (4, 4, "10987612345", "Brasileira"),
        (5, 5, "678910123456", "Venezuelana"),
        (6, 6, "54321109876", "Brasileira"),
        (7, 7, "54321678923", "Brasileira");     
''')

# Tabela autores
conn.cursor.execute('''
    INSERT INTO autores (id_autor, id_pessoa) VALUES 
        (1, 8),
        (2, 9),
        (3, 10),
        (4, 11),
        (5, 12),
        (6, 13),
        (7, 14);
''')


# Tabela autores_livros
conn.cursor.execute('''
    INSERT INTO autores_livros (id_autor, id_livro, id_pessoa) VALUES 
        (1, 1, 8),
        (2, 2, 9),
        (3, 3, 10),
        (4, 4, 11),
        (5, 5, 12),
        (6, 5, 13),
        (7, 5, 14);
''')

#Tabela emprestimo
conn.cursor.execute('''
    INSERT INTO emprestimos(id_exemplar, id_usuario, DataEmprestimo, DataDevolucao, DataDevolvido) VALUES
        (1, 1, '20/08/2024', '27/08/2024', NULL)
''')
   


conn.conexao.commit()
conn.conexao.close