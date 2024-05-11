from database.run_sql import run_sql
from mensagens import *
from verifacoes import *

# Função para mostrar a lista de tarefas
def mostra_tarefas(nome_bloco):
    print('           LISTA     ')
    print('-'*30)

    quantidade = quantidade_tarefas(nome_bloco)
    
    if quantidade == 0:
        print('        LISTA VAZIA       ')
        
    else:
        sql_1 = f'''SELECT task from {nome_bloco};'''
        con_1 = run_sql(sql_1)

        i = 0
        for tarefa in con_1:
            i += 1
            print(f'Tarefa {i} - {tarefa[0]}')
    print('-'*30)


def adicionar_tarefa(nome_bloco):
    # mostra_tarefas()  # Mostra a lista atual de tarefas
    print('Digite (ENCERRAR) a qualquer momento para encerrar a sessão\n')

    while True:
        adicionar = input('Adicionar Tarefa----> ')
        print(f'{adicionar} adicionado com sucesso')
        
        if adicionar == 'ENCERRAR':
            EncerraAçao()
            break
        sql = f"INSERT INTO {nome_bloco} (task) VALUES (%s)"
        run_sql(sql, (adicionar,))
    
        
# adicionar_tarefa('bernardinho')
# Função para excluir uma tarefa da lista
def excluir_tarefa(nome_bloco):


    print('Digite (ENCERRAR)) a qualquer momento para encerrar a ação\n')

    while True:
        mostra_tarefas(nome_bloco)  # Mostra a lista atual de tarefas 

        excluir = int(input('Digite o numero correspondente a tarefa\n-----> '))
        quantidade = quantidade_tarefas(nome_bloco)
        if excluir >=1 and excluir <= quantidade:
            id_tarefa = id_task(nome_bloco)

            sql = f"DELETE FROM {nome_bloco} WHERE id = %s"
            values = (id_tarefa[excluir],)  # Parâmetro de id que queremos deletar

    #            Chamando a função para executar 3a consulta SQL
            run_sql(sql, values)
        else:
            opcao_invalida()

        # if excluir ==  'ENCERRAR':
        #     EncerraAçao()

        # else:
        #     opcao_invalida()
    
# excluir_tarefa('clientes')


# mostra_tarefas('clientes')




def modificar_nome_tarefa(nome_bloco):
    print('Digite (ENCERRAR)) a qualquer momento para encerrar a ação\n')

    while True:
        mostra_tarefas(nome_bloco)  # Mostra a lista atual de tarefas 

        excluir = int(input('Digite o numero correspondente a tarefa\n-----> '))
        quantidade = quantidade_tarefas(nome_bloco)
        if excluir >=1 and excluir <= quantidade:
            id_tarefa = id_task(nome_bloco)
            renome = input('Renomei: ')

            sql = f"UPDATE {nome_bloco} SET Nome = %s WHERE id = %s"
            values = (renome,id_tarefa[excluir])  # Parâmetro de id que queremos deletar

    #            Chamando a função para executar 3a consulta SQL
            run_sql(sql, values)
        else:
            opcao_invalida()

        # if excluir ==  'ENCERRAR':
        #     EncerraAçao()

        # else:
        #     opcao_invalida()
# modificar_nome_tarefa('clientes')


def marca_desmarca_tarefa(nome_bloco):
    print('Digite (ENCERRAR)) a qualquer momento para encerrar a ação\n')

    while True:
        mostra_tarefas(nome_bloco)  # Mostra a lista atual de tarefas 

        excluir = int(input('Digite o numero correspondente a tarefa\n-----> '))
        quantidade = quantidade_tarefas(nome_bloco)
        if excluir >=1 and excluir <= quantidade:
            id_tarefa = id_task(nome_bloco)
            renome = input('Renomei: ')

            sql = f"UPDATE {nome_bloco} SET Nome = %s WHERE id = %s"
            values = (renome,id_tarefa[excluir])  # Parâmetro de id que queremos deletar

    #            Chamando a função para executar 3a consulta SQL
            run_sql(sql, values)
        else:
            opcao_invalida()

        # if excluir ==  'ENCERRAR':
        #     EncerraAçao()

        # else:
        #     opcao_invalida()