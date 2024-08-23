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

loan_cursor = conn.cursor.execute('''
                                SELECT livros.titulo, emprestimos.DataEmprestimo, emprestimos.DataDevolucao
                                FROM emprestimos
                                JOIN livros ON emprestimos.id_livro = livros.id_livro
                                JOIN usuarios ON emprestimos.id_usuario = usuarios.id_usuario
                                WHERE emprestimos.DataDevolvido IS NULL
                           ''')
loan_results = loan_cursor.fetchall()

if loan_results:
    for row in loan_results:
        print(row)

# Verificar o número de cópias disponíveis de um determinado livro. | Jéssica

# Mostrar os empréstimos em atraso. | Rosana

conn.conexao.commit()
conn.conexao.close()