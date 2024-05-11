from database.run_sql import run_sql
from mensagens import *

def quantidade_tarefas(nome_bloco):
    sql = f'''SELECT COUNT(*) FROM {nome_bloco}; '''
    con = run_sql(sql)[0]
    con = con[0]
    con = int(con)
    return con

def verifica_se_bloco_existe(nome_bloco):
    try:
        sql = f'''SHOW TABLES'''
        con = run_sql(sql)
        blocos_tarefas = [bloco[0] for bloco in con]

        if nome_bloco.lower() in blocos_tarefas:

            print(f"O bloco de tarefas '{nome_bloco}' existe.")

            return nome_bloco
        else:
            print(f"O bloco de tarefas '{nome_bloco}' não existe.")
            return None
        
    except Exception as e:
        print("Erro ao executar a consulta SQL:", e)
        return None
# verifica_se_bloco_existe('clientes')
# para inserção no banco  
def trata_nome_bloco(nome_bloco):
    nome_bloco = nome_bloco.split()
    nome_bloco = '_'.join(palavra.lower() for palavra in nome_bloco)
    return nome_bloco


# Função para visualizar sem ifem 
#Usada para mostra ao usuario 
def tira_ifem(nome_bloco):
    lista = []
    for bloco in nome_bloco:
        if '_' in bloco:
            nome_bloco = nome_bloco.split('-')
            nome_bloco = ' '.join(palavra.capitalize() for palavra in nome_bloco)
            lista.append(nome_bloco)
        else:
            lista.append(nome_bloco)
            print('nome sem ifem')
    
    return lista


def e_num(numero):

    if numero.isdigit():
        numero = int(numero)
        return numero
    else:
        return False
    

def id_task(nome_bloco):
    try:
        dic = {}
        sql = f"select id from {nome_bloco}"
        resultados = run_sql(sql)
        i = 0
        for resultado in resultados:
            i += 1
            dic[i] = resultado[0]
        return dic
    except Exception as e:
        print("Erro ao executar a consulta SQL:", e)

# Exemplo de uso
# idd = id_task('bernardinho')
# print(idd[3])
    


        
# sql_delete = f"delete FROM bernardinho WHERE id = %s"
# values = (4,)  # Parâmetro de id que queremos deletar
# run_sql(sql_delete, values)
