#!/usr/bin/python3

# Importando modulos
##############
# Metodo 1 de importar
##############
#import modulos.calculadora as calculadora

# soma = calculadora.somar(1,2)
# print(soma)

# print(calculadora.subtrai(90,70))

####################
# Metodo 2 de importacao - para importar todos os modulos usar *
# ou chamar pelo nome do modulo
####################
# from modulos.calculadora import *

# from modulos.calculadora import somar,subtrai
# print(somar(1,2))
# print(subtrai(90,70))

import random # modulo que trata operações de aleatoriedade
import os # possibilita usar funcionalidades do s.o
import sys # acessar variaveis de sistema e alguns parametros especificos
import datetime # data e hora
import json # codificar e/ou decodificar um arquivo no formato JSON
import csv # trabalha com planilhas

#print(random.randint(1,90))

#os.system('ip -4 a') # rodar comando do sistema

#print(sys.builtin_module_names)
#print(sys.argv)

#print(datetime.datetime.now())

#exemplo prático
# acesso = datetime.datetime(2019,1,22,00,00,00)
# atual = datetime.datetime(2019,1,22,1,1,00)

# if (atual-acesso).total_seconds() > 3600:
#     print('Seu token expirou')
# else:
#     print('Acesso liberado')

############
# Modulo Json
############

print(json.dumps({"nome":"Daniel",
                  "sobrenome":"silva"
                 },indent=4))

# Json.loads retorna um dicionario
print(json.loads('{"nome":"Daniel","sobrenome":"silva"}'))