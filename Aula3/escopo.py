#!/usr/bin/python3

#################
# Escopo de variaveis locais e globais
#################

# variavel no escopo global
variavel = 3

def muda_variavel():
    #variavel = 2 # escopo local
    global variavel
    variavel = 2 # escopo local
    print(variavel)

muda_variavel()