#!/usr/bin/python3

###############
# Parametros de função
###############

# def retorna_pessoa(nome,idade=99):
#     print(f'Nome: {nome}\nIdade: {idade}')

#retorna_pessoa('Rodnei',idade=29)

### Especificar tipo de parametro e retorno

# def retorna_valor_int( inteiro : int, booleano : bool) -> int:
#     ''' Função com anotação de tipo

#     Se refere a função que possui tipo especificos e mostram a sua sintaxe de construção
#     o que é necessario, sempre tem que pular uma linha'''
#     inteiro = int(inteiro)
#     return int(inteiro)

#print(retorna_valor_int())

#print('olá','mundo',',','prazer','Rodnei')

## Criando funcao que recebe multplos valores - Args

def funcao_multi_valores(parametros_estaticos,*argumento_variavel):
    print(parametros_estaticos,'parametros_estaticos')
    print(argumento_variavel)
    #Fazendo acesso aos parâmetros
    # for argumento in argumento_variavel:
    #     print(argumento)

# funcao_multi_valores('valor_obrigatorio','Daniel',
#                      'Vanessa','Joao','ANA','Luiz',
#                     'Lucas','Maria','Cintia','Lara')

# funcao_multi_valores('valor_obrigatorio')

# Argumento com palavra chave - kwargs

# def parametros_chave_valor(**dados):
#     if dados['nome'] == 'Daniel':
#         print('Acesso Negado')
#         #print(dados)
#     else:
#         print('Permitido')

# print('Metodo 1')
# Execução - Metodo 1
# parametros_chave_valor(nome='Daniel',sobrenome='Silva',
#                               idade=20,sexo='Masculino')

# print('Metodo 2')
# Execução - Metodo 2
# dados_requisicao = {'nome':'John','Sobrenome':'Silva',
#                     'Profissão':'Operador de empilhadeira'}


# parametros_chave_valor(**dados_requisicao)


## Decoradores de função
# funcao que modifica valor de outra

# declara uma funcao com uma variavel funcao obrigatoria
def muda_cor(retorno_funcao):
    def modificaAzul(retorno_funcao):
        return f'\033[94m{retorno_funcao}\033[0m'
    return modificaAzul

@muda_cor
def log(texto):
    return texto

print(log('oi'))