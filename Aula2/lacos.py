#!/usr/bin/python3

############
# Laço While
############

# Este laço executa enquanto uma condição for verdadeira

#i = 0
# while(i < 10):
#     print(i)
#     i +=1

# Controlando laço
# while(True):
#     i += 1
#     if i == 10:
#         break
#     if i == 5:
#         continue
#     print('teoricamente um looping infinito')

# continue retoma do começo a execução de um loop
#break encerra o programa

# i = 100  # Iterador regressivo
# while i > 0:
#     i -= 1
#     if i % 2 == 1:
#         continue
#     print(i)

###############
# Laço for
###############
# Percorre itens em determinado alcance de valores

# lista = []
# #for i in range(1,100,2): percorrer do 1 ao 100 de 2 em 2
# #for i in range(100): percorrer do 0 ao 100, foi indicado apenas o valor final
# for i in range(1,100):
#     lista.append(i)
#     print(lista)
# # Percorer uma lista colorindo o resultado cor \033[91m
# for i in lista:
#     if i % 2 == 0:
#         print(f'\033[91m{i}\033[0m','par')   # cor \033[91m
#     if i % 2 == 1:
#         print(f'\033[1;32m{i}\033[0m','impar')

# Percorrer um dicionario

# dicionario = {'nome':'Daniel',
#             'sobrenome':'Silva'
#              }

# for i in dicionario:
#     print(dicionario[i])

# for chave,valor in dicionario.items():
#     print(chave, valor)

# Enumerando itens de uma lista
lista = ['item1','item2','item3','item4','item5','item6','item7']

#print(list(enumerate(lista)))

# for indice,valor in enumerate(lista):
#     print(indice)
#     print(valor)

#list compreenhension (compreensão de listas)
lista = [x*2 for x in range(100)]
print(lista)