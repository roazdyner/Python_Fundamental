#!/usr/bin/python3

import psycopg2

from orm import Banco


try:
    #conexao postgres
    con_psql = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')
    cur_psql = con_psql.cursor()
       
    banco_psql = Banco(con_psql,cur_psql)
  
except Exception as e:
    print(e)
    exit()

try:
    #banco_psql.inserir('Daniel','Proramador Python')
    #print(banco_psql.seleciona('scripts'))
    #print(banco_psql.seleciona_primeiro('scripts'))
    banco_psql.delete('scripts','nome','Daniel')
except Exception as e:
    con_psql.rollback()
    print(e)