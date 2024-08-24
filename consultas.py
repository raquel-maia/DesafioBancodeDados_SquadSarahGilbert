'''
3. Consultas SQL:
Escreva consultas SQL para realizar as seguintes operações:
'''
import conexao as conn

def print_consulta(consulta):
    for row in consulta:
        print(row)

# Listar todos os livros disponíveis. | raquel
print('Listar todos os livros disponíveis: ')
list_books = conn.cursor.execute('SELECT titulo FROM livros')
print_consulta(list_books)
      
# Encontrar todos os livros emprestados no momento. | Livia
print('\nEncontrar todos os livros emprestados no momento: ')
loan_cursor = conn.cursor.execute('''
                                SELECT livros.titulo,emprestimos.DataEmprestimo, emprestimos.DataDevolucao
                                FROM emprestimos
                                LEFT JOIN exemplares ON emprestimos.id_exemplar = exemplares.id_exemplar
                                LEFT JOIN Livros on exemplares.id_livro = livros.id_livro
                                LEFT JOIN usuarios ON emprestimos.id_usuario = usuarios.id_usuario
                                WHERE emprestimos.DataDevolvido IS NULL
                          ''')
loan_results = loan_cursor.fetchall()

if loan_results:
    print_consulta(loan_results)

# Verificar o número de cópias disponíveis de um determinado livro. | Jéssica
print('\nVerificar o número de cópias disponíveis de um determinado livro: ')

# Mostrar os empréstimos em atraso. | Rosana
print('\nMostrar os empréstimos em atraso: ')
c = conn.cursor.execute("SELECT titulo FROM livros as lv INNER JOIN generos as gn ON lv.id_livro = gn.id_genero")
print_consulta(c)
    
conn.conexao.commit()
conn.conexao.close