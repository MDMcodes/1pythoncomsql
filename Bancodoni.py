import mysql.connector

conexao_banco = mysql.connector.connect(
    host ='127.0.0.1',
    user = 'root',
    password = '',
    database = 'mercado'
)

cursor = conexao_banco.cursor()

#CREATE

# nome = input('Digite o nome do produto: ')
# valor = float(input('Digite o valor do produto '))

# comando_sql = f'INSERT INTO produtos (nome_produto, valor_produto) VALUES ("{nome}", {valor})'

# cursor.execute(comando_sql)
# conexao_banco.commit()

#UPDATE

# input_id = int(input('Digite o id do produto que você deseja alterar: '))
# nome = input("Digite o novo nome do produto: ")

# comando_sql = f'UPDATE produtos SET nome_produto = "{nome}" WHERE id_produtos = {input_id}'


# cursor.execute(comando_sql)
# conexao_banco.commit()

#DELETE

# input_id = int(input('Digite o id do produto que você deseja deletar: '))

# comando_sql = f'DELETE FROM produtos WHERE id_produtos = {input_id}'
# cursor.execute(comando_sql)
# conexao_banco.commit()

#READ

comando_sql = 'SELECT * FROM produtos'
cursor.execute(comando_sql)
dados_tabela = cursor.fetchall()
print(dados_tabela[0][0])
print(dados_tabela[1][1])
print(dados_tabela[2][2])