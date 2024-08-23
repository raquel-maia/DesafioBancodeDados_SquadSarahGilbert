'''
4. Atualizações e Exclusões:
- Escreva consultas SQL para atualizar e excluir registros do banco de
dados, por exemplo, para marcar um livro como devolvido ou remover
um autor.
'''

import conexao as conn

# Atualizar | Jessica+

# Excluir | Nadi
#Excluir tabelas
'''
conn.cursor.execute('DROP TABLE livros')
conn.cursor.execute('DROP TABLE generos')
conn.cursor.execute('DROP TABLE livros_generos')
conn.cursor.execute('DROP TABLE exemplares')
conn.cursor.execute('DROP TABLE pessoas')
conn.cursor.execute('DROP TABLE usuarios')
conn.cursor.execute('DROP TABLE autores')
conn.cursor.execute('DROP TABLE autores_livros')
'''

#Excluir um autor
id_autor = 7
conn.cursor.execute('DELETE FROM autores WHERE id = id_autor')

conn.conexao.commit()
conn.conexao.close()