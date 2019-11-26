#!/usr/bin/python3
#########
# Manipulacao de arquivos com Python
#########
## Abrir um arquivo para manipulação
########### Metodo não recomendado #########

#ponteiro = open('nomedoarquivo.txt','r+')

# Escrita de arquivo, o modo utilizado é o read plus (r+) que serve para
# leitura e escrita. Possuimos varios modos de acesso, por exemplo:
# w = sobrescrita
# r = somente leitura
# + = abre um arquivo para atualização (acrescenta e modifica)
# a = complemento
# x = criação
# este metodo não é recomendado porque o ponteiro sempre necessita
# ser encerrado com o close, isso foi substituido com a adição
# do comando with (mostraremos em breve)

# ponteiro.write('Olá mundo\n')
# ponteiro.close()

########################
# Metodo Usual
#######################

with open('nomedoarquivo2.txt','w') as arquivo:
    arquivo.write('Olá Mundo\n')
    arquivo.writelines(['banana\n','maça\n'])
with open('nomedoarquivo2.txt','r') as arquivo:
    file = arquivo.readlines()

print(file)