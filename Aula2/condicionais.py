#!/usr/bin/python3

##################
# Estrutura de condicional simples
##################

# Estrutura simples

# nome = input('Digite o seu nome: ').strip().title()
# sobrenome = input('Digite seu sobrenome: ').strip().title()

# if nome == 'Rodnei':
#     print(f'Olá {nome}')
# print('Seja Bem vindo')

# Estrutura condicional composta
# if nome == 'Rodnei':
#     print(f'Oi {nome}')
# else:
#     print(f'Seja Bem vindo {nome}')
# print(f'{nome} pode utilizar a plataforma')

## Estrutura condicional duas condicoes
# if nome == 'Daniel' and sobrenome == 'Silva':
#     print(f'Bem vindo professor {nome} {sobrenome}')
# else:
#     print(f'Seja Bem vindo Aluno {nome} {sobrenome}')
# print(f'{nome} {sobrenome} pode utilizar a plataforma')


# if nome == 'Daniel':
#     if sobrenome =='Silva':
#         print('Olá Professor')
#     else:
#         print('Olá você é Daniel, mas não é professor')
# else:
#     print(f'Olá Aluno {nome}')

#########
# Condicional Aninhadas
#########

nome = input('Digite seu nome:').title().strip()

if nome == 'Daniel':
    print(f'Seu nome é bonito, {nome}')
elif nome == 'Juliana':
    print(f'Seu nome é bonito, {nome}')
elif nome == 'Jorge':
    print(f'Seu nome é muito feio, {nome}')
else:
    print(f'Seu nome é normal, {nome}')