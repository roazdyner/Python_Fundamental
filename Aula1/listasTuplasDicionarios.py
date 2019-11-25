#!/usr/bin/python3

#contagem de lista se inicia no zero
# lista = ['Arroz','Feijao','Oleo','Sal','Açucar','Temperos'] # Teste de lista

# print(lista[0])

# lista = ['Alfa','Beta','Cor','Delta','Echo','Faca','Gato'] # Teste de lista
# print(lista[-2])

#lista multidimensionais

# lista3d = [
#     [2 , 4 ,5 , 6],
#     [7 , 8 , 9, 10],
#     [11 , 12, 13, 14]
# ]


#lista = ['Echo','Alfa','Delta','Beta','Cor','Faca','Gato','Zebra']

#adiocionar no final da lista
#lista.append('Carne')

#adicionar na posicao selecionada
#lista.insert(5,'Café')

#remover item selecionado
#lista.pop(-1)

#Ordenar lista ordem alfabetica/numerica
#lista.sort()

#Ordernar reverso
#lista.reverse()

#exibe qtde de elementos
#print(len(lista))

#Procura o primeiro indice da ocorrencia
#print(lista.index('Delta'))

#exibe posicao do item pelo nome
#print(lista.count('Beta'))

#remove primeiro item encontrado com o valor informado
#lista.remove('Echo')

#Sobreescreve o elemento em determinado indice
# lista[2] = 'Bola'
# print(lista)

# tupla = ('Maça','Banana','Laranja','Abacaxi','Uva')
# tupla2 = 'valor1', 2, True, 2j

#Acessar indice de tupla
#print(tupla[1:4])
#print(tupla[3])
#print(tupla[-3])

#Converter tupla para lista
#lista_tupla = list(tupla)
#print(tupla)
#print(type(lista_tupla))

#print(tupla2[0:])

# tupla3 = (['Indice 1'], 'Nome')
# tupla3[0].insert(1,'Indice 2')
# print(tupla3)

##################################################
#   Dicionarios
#   Criando dicionarios
# apresentacoes = {
#     'Paulista' : 'Salve',
#     'Carioca' : 'Eae',
#     'Pirata' : 'Argh',
#     'Mineiro' : 'Pão de queijo',
#     'Acre' : 'Barulhos de Dinossauros',
# }

# Acessando indices de um dicionario
#print(apresentacoes['Paulista'])

#Criando um dicionario com multi-valores internos
# linguagem_favorita = {
#     'Daniel' : {
#         'linguagem' : 'Python',
#         'Tempo_de_experiencia' : 2
#     },
#     'Olympio' : {
#     'linguagem' : 'R',
#     'linguagem2' : 'VBA',
#     'Tempo_de_experiencia' : 10
#     },
# }

#print(linguagem_favorita.get('Daniel')['linguagem'])

#acesso a todas as chaves
#print(linguagem_favorita.keys())

#acesso aos valores
#print(linguagem_favorita.values())

#acesso aos itens
#print(linguagem_favorita.items())

###################################################
# Numeros

# somar = 2+2
# multiplicar = 23*20
# divisao = 455 / 2 
# potencia = 2**2
# raiz = 2 ** 0.5
# print(f'2+2 = {somar} - Retornando o somar')
# print(f'23x20 = {multiplicar} - Retornando o multiplicar')
# print(f'455 / 2 = {divisao} - Retornando o produto')
# print(f'2**2 = {potencia} - Retornando potencia')
# print(f'2 ** 0.5 = {raiz} - Retornando raiz')

#letras = 'abcdefghij' + 'lmnopqrstu'
#print(letras)


print(float(input('Digite um numero: ')) + float(input('Digite outro numero: ')))