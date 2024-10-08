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

# comando_sql = 'SELECT * FROM produtos'
# cursor.execute(comando_sql)
# dados_tabela = cursor.fetchall()
# print(dados_tabela[0][0])
# print(dados_tabela[1][1])
# print(dados_tabela[2][2])

# for i in dados_tabela:
#     print(f'ID: {i[0]}  PRODUTO {i[1]}   VALOR: {i[2]}')


#-----------------------------------------------------------------------
#Verificar se o id esta cadastrado no update

input_id = int(input('Digite o ID do produto que será alterado: '))
comando_sql = 'SELECT * FROM produtos'
cursor.execute(comando_sql)
dados_tabela = cursor.fetchall()
for dados in dados_tabela:
    if dados[0] == input_id:
        esc = int(input(f'Deseja alterar o (1)nome ou o (2)valor?: '))
        if esc == 1:
            nome = input("Digite o novo nome do produto: ")
            comando_sql = f'UPDATE produtos SET nome_produto = "{nome}" WHERE id_produtos  = {input_id}'
            cursor.execute(comando_sql)
            conexao_banco.commit()
        elif esc == 2:
            valor = float(input("Digite o novo valor do produto: "))
            comando_sql = f'UPDATE produtos SET valor_produto = "{valor}" WHERE id_produtos  = {input_id}'
            cursor.execute(comando_sql)
            conexao_banco.commit()
    else:
        print('ID não encontrado')
        break



