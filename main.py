from operacoesbd import *

conn = abrirBancoDados("localhost", "root", 1234, "abella")

sql = "SELECT * FROM conta"
resultado = listarBancoDados(conn,sql)

for elemento in resultado:
    print(elemento)


conta = int(input('digite a conta')
agencia = int(input('agencia))
titular = input('titular')
saido = float(input('saldo'))

sql = "insert into conta (conta,agencia,titular,saldo) VALUES (%s , %s , %s, %s)"
dados = (conta, agencia, titular, saldo)
insertNoBancoDados(conn,sql,dados)



"""
nome = input('digite o nome do produto ') descricao = input('digite a descricao ') areco = float(input('digite o preco '))
scl = "INSERT INTO rodutos nome descricao reco VALUES Is Is
• 1111 1.01.1" \A I .1. 10 • 1001
6 (nn,6 d06rriran 1,6n) v
"""






'''
import mysql.connector

connection = mysql.connector.connect(
host."localhost",
user = "root",
password = "1234",
database = "abella"
)

cursor = connection.cursor()

sql = 'INSERT INTO usuarios (conta,agencia, titular, varchar(100) saldo float,) VALUES (%s, %s, %s, %s)'
data = ('Daniel Abella', 'dabella', '12345')

cursor.execute(sql, data)
connection.commit()

userid = cursor.lastrowid

cursor.close()
connection.close()

print("ID do novo usuario:", userid)
'''