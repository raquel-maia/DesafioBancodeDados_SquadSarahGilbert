'''
4. Atualizações e Exclusões:
- Escreva consultas SQL para atualizar e excluir registros do banco de
dados, por exemplo, para marcar um livro como devolvido ou remover
um autor.
'''

import conexao as conn
from datetime import datetime

##############################################################################
# Atualizar | Jessica
##############################################################################

var_date = str(datetime.now().strftime("%d/%m/%Y"))
conn.cursor.execute(f'''UPDATE emprestimos
                        SET DataDevolvido = '{var_date}'
                        WHERE id_emprestimo = 1''')


##############################################################################
# Excluir | Nadi
##############################################################################

# Excluir tabelas
'''conn.cursor.execute('DROP TABLE IF EXISTS livros')
conn.cursor.execute('DROP TABLE IF EXISTS generos')
conn.cursor.execute('DROP TABLE IF EXISTS livros_generos')
conn.cursor.execute('DROP TABLE IF EXISTS exemplares')
conn.cursor.execute('DROP TABLE IF EXISTS pessoas')
conn.cursor.execute('DROP TABLE IF EXISTS usuarios')
conn.cursor.execute('DROP TABLE IF EXISTS autores')
conn.cursor.execute('DROP TABLE IF EXISTS autores_livros')
conn.cursor.execute('DROP TABLE IF EXISTS emprestimos')'''

#Excluir um autor
var_id_autor = 8
conn.cursor.execute(f'DELETE FROM autores WHERE id_autor = {var_id_autor}')

var_id_livro = 5
conn.cursor.execute(f'DELETE FROM livros WHERE id_livro = {var_id_livro}')

conn.conexao.commit()
conn.conexao.close()