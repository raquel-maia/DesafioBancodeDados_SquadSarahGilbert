import conexao as conn

conn.cursor.execute('''
    INSERT INTO livros (
        id_livro,
        titulo,
        editora
    ) VALUES 
        (
            1,
            "The StatQuest Illustrated Guide to Machine Learning!!!",
            "Packt Publishing"
        ),
        (
            2,
            "Código Limpo: Habilidades Práticas do Agile",
            "Alta Books"
        ),
        (
            3,
            "Introdução à Programação com Python",
            "Novatec"
        ),
        (
            4,
            "Python para Data Science",
            "Alta Books"
        );       
''')

conn.conexao.commit()
conn.conexao.close