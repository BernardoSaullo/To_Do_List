from database.run_sql import run_sql
from mensagens import *
from verifacoes import *
from tarefas import *


def criar_bloco_de_tarefa():

    nome_bloco = input('Nome do Bloco\n----> ')
    nome_bloco = trata_nome_bloco(nome_bloco)

    sql = f'''CREATE TABLE IF NOT EXISTS {nome_bloco} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(30) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP NULL DEFAULT NULL,
    status ENUM('PENDENTE', 'COMPLETA') DEFAULT 'PENDENTE'
    
);'''
    run_sql(sql)

# criar_bloco_de_tarefa()

def modificar_nome_bloco_de_tarefa():
    mostra_todos_blocos_de_tarefa()
    while True:
        nome_bloco = input('Nome do Bloco\n----> ')
        nome_bloco_tratado = trata_nome_bloco(nome_bloco)
        verifica = verifica_se_bloco_existe(nome_bloco_tratado) # verifica se existe o banco de dados e depois renomea-lo
        if  verifica == False:
            opcao_invalida()
        else:
            nome_novo = input('Novo nome do Bloco\n---->')
            nome_novo_tratado = trata_nome_bloco(nome_novo)
            pass # Renome-lo
            sql = f"RENAME TABLE {nome_bloco_tratado} TO {nome_novo_tratado}"
            run_sql(sql)

# modificar_nome_bloco_de_tarefa()


def apaga_bloco_de_tarefa():
    mostra_todos_blocos_de_tarefa()
    while True:
        nome_bloco = input('Nome do bloco: ')
        nome_bloco_tratado = trata_nome_bloco(nome_bloco)
        verifica = verifica_se_bloco_existe(nome_bloco_tratado) # verifica se existe o banco de dados e depois renomea-lo
        if  not verifica:
            opcao_invalida()
        else:
            sql = f'''DROP TABLE {verifica};'''

            run_sql(sql)

#apaga_bloco_de_tarefa()

def mostra_todos_blocos_de_tarefa():

    print('='*30)
    print(' '*7,'BLOCOS')
    print('='*30)
    sql = 'show tables;'
    blocos = run_sql(sql)
    lista = []
    for i,bloco in enumerate(blocos):
        print(f'Bloco {i+1} -- {bloco[0]}')
        lista.append(bloco[0])

    return lista

    print('='*30)


# mostra_todos_blocos_de_tarefa()


def selecao_do_bloco():
    blocos = mostra_todos_blocos_de_tarefa()
    print('Selecione o bloco que vc quer entrar')
    entrada = int(input('----> '))

    nome_bloco = blocos[entrada-1]

    entrada = input('1-Adicionar Tarefa\n2-Renomear Tarefas\n3-Excluir Tarefas\n4-Marca tarefa\n---->')
    entrada = e_num(entrada)

    bl = [adicionar_tarefa,modificar_nome_tarefa,excluir_tarefa,marca_desmarca_tarefa]
    if entrada >= 1 and entrada <= len(bl):
        bl[entrada - 1](nome_bloco)
    elif not entrada:
        opcao_invalida()



