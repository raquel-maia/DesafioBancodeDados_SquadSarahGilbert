import conexao as conn

#Listaroslivrosdisponíveis

list_books = conn.cursor.execute('SELECT titulo FROM livros')
for livros in list_books:
    print(livros)
    
conn.conexao.commit()
conn.conexao.close