# Módulo de conexão ao banco de dados

# Imports
import mysql.connector

# Função
def run_sql(sql, values=None):
    # Variáveis de controle
    connection = None
    results = []

    # Conexão ao banco de dados
    try:
        connection = mysql.connector.connect(
            host="localhost",    # Endereço do servidor MySQL
            port=3306,           # Porta do MySQL (por padrão é 3306)
            user="root",         # Nome de usuário do MySQL
            password="1234",# Senha do MySQL
            database="e_commerce" # Nome do banco de dados
        )

        if not values == None :
            cursor = connection.cursor()
            cursor.execute(sql, values)
            connection.commit()
            results = cursor.fetchall()
            cursor.close()
        else:
            cursor = connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
    except mysql.connector.Error as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

    return results