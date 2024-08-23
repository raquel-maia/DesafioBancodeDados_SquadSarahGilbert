import sqlite3

conexao = sqlite3.connect('banco.db')
#conexao = sqlite3.connect('DesafioBancodeDados_SquadSarahGilbert/banco.db')
cursor = conexao.cursor()