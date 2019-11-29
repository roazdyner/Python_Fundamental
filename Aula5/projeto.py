#!/usr/bin/python3

#Trabalhar com mongo
import pymongo
import threading

from chat import *

try:
    client = pymongo.MongoClient()
    db = client['chat']

except Exception as e:
    print(e)

if __name__ == '__main__':
    usuario = input('Digite um apelido: ')
    try:
        paralelo = threading.Thread(target=chat.lerMensagens) ## Metodo a definir
        paralelo.start
    except Exception as e:
        print(e)

    while paralelo.isAlive:
        chat.cadastrar(usuario.mensagem)