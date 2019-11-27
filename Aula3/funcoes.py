#!/usr/bin/python3

#################
# Funções
#################

# # Blocos de códigos pré-definidos para execução
# def mostrar_hello_world():
#     print('hello world')

# # mostrar_hello_world()
# #Criando uma estrutura de função
# def menu():
#     print('Escolha a opção: ')
#     print('1 - Registrar produto')
#     print('2 - Consultar saldo do caixa')
#     print('3 - Abrir caixa registradora')
#     print('4 - Fechamento')
#     return input('Digite a opção desejada: ')

# def registrar_produto():
#     print('Produto registrado')

# def consultar_saldo():
#     print('Saldo é R$ x')

# def abrir_caixa():
#     print('Abrindo caixa')

# def fechamento():
#     print('fechando')
# # pass # Utilizado para manter codigo funcional durante implementação
# # estrutura principal
# while True:
#     print('Caixa Registradora')
#     opcao = menu()
#     if opcao == '1':
#         registrar_produto()
#     elif opcao == '2':
#         consultar_saldo()
#     elif opcao == '3':
#         abrir_caixa()
#     elif opcao == '4':
#         fechamento()
#     else:
#         break
#     input('Digite enter para continuar!')

##############################
# Funcoes anonimas
# var = lambda x : x*2
# print(var(2))

numeros = list(range(1,100))
#print(numeros)

# def dobro(x):
#     return x * 2

print(list(map(lambda x : x + 3 ,numeros)))