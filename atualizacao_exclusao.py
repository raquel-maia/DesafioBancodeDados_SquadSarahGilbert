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
conn.cursor.execute('DROP TABLE IF EXISTS livros')
conn.cursor.execute('DROP TABLE IF EXISTS generos')
conn.cursor.execute('DROP TABLE IF EXISTS livros_generos')
conn.cursor.execute('DROP TABLE IF EXISTS exemplares')
conn.cursor.execute('DROP TABLE IF EXISTS pessoas')
conn.cursor.execute('DROP TABLE IF EXISTS usuarios')
conn.cursor.execute('DROP TABLE IF EXISTS autores')
conn.cursor.execute('DROP TABLE IF EXISTS autores_livros')
conn.cursor.execute('DROP TABLE IF EXISTS emprestimos')
'''

#Excluir um autor
id_autor = 7
conn.cursor.execute('DELETE FROM autores WHERE id = id_autor')

conn.conexao.commit()
conn.conexao.close()