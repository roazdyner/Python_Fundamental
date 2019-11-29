#!/usr/bin/python3

class Banco():
    def __init__(self,conexao,cursor):
        try:
            self.conexao = conexao
            self.cursor = cursor
        except Exception as e:
            raise Exception(e)

#Criando CRUD - Create, Read, Update, Delete
    def inserir(self, nome, conteudo):
        self.cursor.execute(f"INSERT INTO scripts(nome,conteudo) VALUES('{nome}','{conteudo}')")
        self.conexao.commit()
        print('Inserido com sucesso')

    # Criando funcao atualizar dados
    def atualizar(self, coluna, valor, coluna_antiga, valor_old):
        self.cursor.execute(f"UPDATE scripts SET {coluna} = {valor} WHERE {coluna_antiga} = {valor_old}")
        self.conexao.commit()
        print('Atualizado com sucesso')

    def delete(self, tabela, coluna, valor):
        self.cursor.execute(f"DELETE FROM {tabela} WHERE {coluna} = '{valor}'")
        self.conexao.commit()
        print(f'Deletando da tabela "{tabela}", o valor "{valor}"!\nDeletado com sucesso.')

    def seleciona(self, tabela):
        self.cursor.execute(f"SELECT * FROM {tabela}")
        return self.cursor.fetchall()

    def seleciona_primeiro(self, tabela):
        self.cursor.execute(f"SELECT * FROM {tabela}")
        return self.cursor.fetchone()

    def __del__(self):
        self.cursor.close()
        self.conexao.close()