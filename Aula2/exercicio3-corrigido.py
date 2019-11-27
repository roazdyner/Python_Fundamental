#!/usr/bin/python3

#######
## Exercicio de excessões
#######

#Abro o arquivo de politicos para leitura
with open('politicos.txt','r') as arquivo:
    #pego a lista de todos os politicos com o readlines que retorna
    #uma lista
    figuras_publicas = arquivo.readlines()
# para testar o conteúdo de figuras públicas
# print(figuras_publicas)

try: #abro o bloco para tratamento de exceções
    while True: #código roda em um loop infinito

        #pego a lista de nomes cadastrados com o with open em modo
        #de leitura
        with open('nomes.txt','r') as nomes:
            lista_nomes = nomes.readlines() # pega a lista com todos os nomes
        
        # Pegando a entrada de nome
        nome = input('Digite um nome: ').lower().strip()
        nome += '\n' #acrescentar o \n para trabalhar no padrão de quebra de linha

        #Criando lógica para cadastro
        if nome in figuras_publicas: # se o nome for de politico
            #gero uma exceção
            raise ValueError('Você tentou inserir uma figura pública')
        # se o nome já estiver na lista de nomes
        elif nome in lista_nomes:
            #mostro que o nome já existe e não faço mais nada
            print('nome Já existe')
        # se eu digitar o nome como visualizar
        elif nome == 'visualizar\n':
            #faço um loop dentro da lista de nomes
            for nome_cadastrado in lista_nomes:
                #mostro o nome no indice do loop separado com ,
                print(nome_cadastrado.replace('\n','').title(),end=', ')
            #quando acaba a lista eu dou uma quebra de linha
            print('\n')
        # se não cair em nenhuma validação
        # significa que o nome pode ser cadastrado

        ### teste exit sair do looping
        elif nome == 'exit\n':
            break
        else:
            #abro o arquivo em modo de acrescentar (append)
            with open('nomes.txt','a') as nome_arquivo:
                #cadastro minha variável nome
                nome_arquivo.write(nome)
            #mostro uma mensagem falando que foi realizado com sucesso
            print('Cadastro Realizado')
#se ele der o erro definido para dar quando cadastramos um politico
except ValueError:
    # mandar uma mensagem de erro
    print('Você tentou cadastrar uma figura pública')
# Tratar qualquer outro erro
except Exception as e:
    #mostra a mensagem de erro de uma forma formatada
    print('Deu ruim: ', e)