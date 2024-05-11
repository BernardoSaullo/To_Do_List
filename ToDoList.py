from database.run_sql import run_sql
# Função para imprimir uma mensagem de encerramento


# Função para adicionar uma nova tarefa à lista


boasvindas()


while True:
# 
# após selecionar o BLOCO DE NOTAS vc pode add,exc,ver,modificar
    lista_tarefa = input('1-')
    entrada = input('''1 - Adicionar elemento\n2 - Excluir elemento\n3 - Ver lista\n4 - Encerrar programa\n---->''')
    
    if entrada.isdigit(): # Verifica se a entrada é um dígito
        entrada = int(entrada)
        if entrada == 1:
            adicionar() # Chama a função adicionar
        elif entrada == 2:
            excluir() # Chama a função excluir
        elif entrada == 3:
            selecionar() # Chama a função selecionar
        elif entrada == 4:
            EncerraAçao()  # Chama a função de encerramento
            break  # Sai do loop principal
        else:
            opcao_invalida()
    else:
        opcao_invalida()