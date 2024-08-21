'''
3. Consultas SQL:
Escreva consultas SQL para realizar as seguintes operações:
'''
import conexao as conn

# Listar todos os livros disponíveis. | raquel

list_books = conn.cursor.execute('SELECT titulo FROM livros')
for livros in list_books:
    print(livros)

# Encontrar todos os livros emprestados no momento. | Livia

# Localizar os livros escritos por um autor específico. | Leticia

# Verificar o número de cópias disponíveis de um determinado livro. | Jéssica

# Mostrar os empréstimos em atraso. | Rosana

conn.conexao.commit()
conn.conexao.close()