'''
3. Consultas SQL:
Escreva consultas SQL para realizar as seguintes operações:
'''
import conexao as conn
from datetime import datetime

def print_consulta(consulta):
    for row in consulta:
        print(row)

############################################################################## 
# Listar todos os livros disponíveis. | raquel
############################################################################## 
print('Listar todos os livros disponíveis: ')
list_books = conn.cursor.execute('SELECT titulo FROM livros')
print_consulta(list_books)

##############################################################################     
# Encontrar todos os livros emprestados no momento. | Livia
##############################################################################
print('\nEncontrar todos os livros emprestados no momento: ')
loan_cursor = conn.cursor.execute('''
                                SELECT livros.titulo, emprestimos.data_emprestimo, emprestimos.data_devolucao
                                FROM emprestimos
                                LEFT JOIN exemplares ON emprestimos.id_exemplar = exemplares.id_exemplar
                                LEFT JOIN Livros on exemplares.id_livro = livros.id_livro
                                LEFT JOIN usuarios ON emprestimos.id_usuario = usuarios.id_usuario
                                WHERE emprestimos.data_devolvido IS NULL
                          ''')
loan_results = loan_cursor.fetchall()

if loan_results:
    print_consulta(loan_results)

##############################################################################
# Verificar o número de cópias disponíveis de um determinado livro. | Jéssica
##############################################################################
print('\nVerificar o número de cópias disponíveis de um determinado livro: ')
# var_id_livro = 1
var_id_livro = 3
check_livro_emprestimo = conn.cursor.execute(f'''
                                SELECT livros.titulo, emprestimos.data_emprestimo, emprestimos.data_devolucao
                                FROM emprestimos
                                LEFT JOIN exemplares ON emprestimos.id_exemplar = exemplares.id_exemplar
                                LEFT JOIN Livros on exemplares.id_livro = livros.id_livro
                                LEFT JOIN usuarios ON emprestimos.id_usuario = usuarios.id_usuario
                                WHERE livros.id_livro = {var_id_livro}
                                ''')
check_livro_emprestimo_r = check_livro_emprestimo.fetchall()

check_exemplares = conn.cursor.execute(f'''
                                SELECT id_livro, count(1) as qtd_livros
                                FROM exemplares
                                WHERE id_livro = {var_id_livro}
                                GROUP BY id_livro
                                ''')
for idlivro, qtdlivro in check_exemplares: 
    pass
    # print(f'- Livro id: {idlivro}\n- Cópias disponiveis: {qtdlivro}')

# Algum exemplar desse livro está emprestado
if check_livro_emprestimo_r:
    qtd_emprestimo = conn.cursor.execute(f'''
                                SELECT livros.id_livro, count(1)
                                FROM emprestimos
                                LEFT JOIN exemplares ON emprestimos.id_exemplar = exemplares.id_exemplar
                                LEFT JOIN Livros on exemplares.id_livro = livros.id_livro
                                LEFT JOIN usuarios ON emprestimos.id_usuario = usuarios.id_usuario
                                WHERE livros.id_livro = {var_id_livro}
                                GROUP by livros.id_livro
                                ''')
    for idlivroemprest, qtdlivroemprest in qtd_emprestimo: 
        resp = qtdlivro - qtdlivroemprest
        print(f'- Livro id: {idlivroemprest}\n- Cópias disponiveis: {resp}')

# Livro não possui nenhum exemplar em emprestimo
else: 
    print(f'- Livro id: {idlivro}\n- Cópias disponiveis: {qtdlivro}')

##############################################################################
# Mostrar os empréstimos em atraso. | Rosana
##############################################################################
print('\nMostrar os empréstimos em atraso: ')
data_atual = datetime.now().strftime('%Y-%m-%d')
c = conn.cursor.execute('''
    SELECT livros.titulo, usuarios.id_usuario, emprestimos.data_emprestimo, emprestimos.data_devolucao
    FROM emprestimos
    JOIN exemplares ON emprestimos.id_exemplar = exemplares.id_exemplar
    JOIN livros ON exemplares.id_livro = livros.id_livro
    JOIN usuarios ON emprestimos.id_usuario = usuarios.id_usuario
    WHERE emprestimos.data_devolucao > ? AND emprestimos.data_devolucao IS NULL
''', (data_atual,))
print_consulta(c)

conn.conexao.commit()
conn.conexao.close
