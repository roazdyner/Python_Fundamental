#!/usr/bin/python3

import MySQLdb

from orm import Banco

try:
    # Conexao MySQL
    con_mysql = MySQLdb.connect(host='localhost',db='scripts',user='developer',passwd='4linux')
    cur_mysql = con_mysql.cursor()
       
    banco_mysql = Banco(con_mysql,cur_mysql)

except Exception as e:
    print(e)
    exit()

try:
    #banco_mysql.inserir('Daniel','Proramador Python')
    print(banco_mysql.seleciona('scripts'))
    #print(banco_mysql.seleciona_primeiro('scripts'))
    #banco_mysql.delete('scripts','nome','John')
    #pass
except Exception as e:
    con_mysql.rollback()
    print(e)