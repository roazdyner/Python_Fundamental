#!/usr/bin/python3

################
# Tratando Excessoes
################

# try: #Tente 
#     print('Divisao de dois valores')
#     numero1 = int(input('Digite um numero a ser dividido: '))
#     numero2 = int(input('Digite outro numero a ser dividido: '))
#     print(numero1 / numero2)
# #except ValueError: # Exceção
# #    print('Insira Somente Números!')
# #except ZeroDivisionError:
# #    print('Impossivel dividir por 0')
# except Exception as e:
#     print('Erro na execução do programa:', e)
# finally: # Saindo do script, utilizado para encerrar conexões
#     print('Saindo do script')

#Variavel Nula
nulo = None # variavel nula, zerar valor

#try:
opcao = int(input('Não digite 5: '))
if opcao == 5:
    raise ValueError('Eu falei pra você não digitar 5')
#except ValueError as e:
#    print('Deu erro: ', e)