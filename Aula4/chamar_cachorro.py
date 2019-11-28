#!/usr/bin/python3
#from Cachorro import Cachorro

import Cachorro

rex1 = {'nome' : 'Rex',
        'idade' : 2,
        'raca' : 'Chow Chow',
        'porte' : 'Medio',
        'cor'   : 'preto',
        'lingua' : False,
        }

#variavel = Arquivo.Classe(atributos).metodo()

dog = Cachorro.Cachorro(**rex1).latir()