from mensagens import *
from database.run_sql import run_sql
from verifacoes import *
from blocos import *


def menu():
    boasvindas()
    bl = [criar_bloco_de_tarefa,modificar_nome_bloco_de_tarefa,apaga_bloco_de_tarefa,selecao_do_bloco]
    entrada = input('1-Criar Novo Bloco de Tarefas\n2-Renomear Bloco de Tarefas\n3-Excluir Bloco de Tarefas\n4-Entrar no bloco de tarefa\n---->')
    entrada = e_num(entrada)
    if entrada >= 1 and entrada <= len(bl):
        bl[entrada - 1]()
    elif not entrada:
        opcao_invalida()
    
  
menu()