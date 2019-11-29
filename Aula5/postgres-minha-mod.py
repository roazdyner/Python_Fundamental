#!/usr/bin/env python3

import psycopg2

# Criando a função de inserção de dados
def inserir(cursor,conexao,nome,conteudo):
    cur.execute(f"INSERT into scripts(nome,conteudo) values('{nome}','{conteudo}')")
    con.commit()
    print('Inserido com sucesso')


############################
def pesquisar(tabela): #Select no banco
#     #select
    cur.execute(f"SELECT * from {tabela}")
    retorno = cur.fetchall()
    #for retorno in r_sql:
    #print(retorno)
###

try:
    con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")
except Exception as e:
    print(e)
    exit()

cur = con.cursor()
try:
    
    inserir(cur,con,'John','Testador')

    pesquisar('scripts')
#################################
    for r_sql in retorno:
    print(r_sql)
######################################
except Exception as e:
    print(e)
    con.rollback()
finally:
    cur.close()
    con.close()