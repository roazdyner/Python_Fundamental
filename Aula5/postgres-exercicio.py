#!/usr/bin/env python3

import psycopg2

#Criando a função de inserção de dados
def inserir(cursor,conexao,nome,conteudo,tabela ,*colunas : str):
    todas_as_colunas = ''
    for coluna in colunas:
        todas_as_colunas += ' ' + coluna
    cursor.execute(f"INSERT into {tabela}({todas_as_colunas}) values('{valor}')")
    conexao.commit()
    print('Inserido com sucesso')


try:
    con = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')
except Exception as e:
    print(e)
    exit()

cur = con.cursor()
try:
    inserir(cur,con,'Luiz','Programador java')
except Exception as e:
    con.rollback()
    print(e)
finally:
    cur.close()
    con.close()