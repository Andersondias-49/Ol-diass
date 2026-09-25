import mysql.connector
conexao = mysql.connector.connect(
host = '127.0.0.1',
port = '3306',
user = 'root',
password = '020508',
database = 'estoque',
use_pure = True)
cursor = conexao.cursor()
def listar_produtos():
    cursor.execute("""select *
                      from produtos""")
    p = cursor.fetchall()
    for c in p:
        print(f'ID: {c[0]} ')
        print(f'Nome: {c[1]}')
        print(f'Categoria: {c[2]}')
        print(f'Preço: {c[3]}')
        print(f'Quantidade: {c[4]}')
        print()


def cadastrar_produto():
    nome = input('Qual nome do produto que você deseja cadastrar? ')
    categoria = input('Qual a categoria do produto? ')
    preco = float(input('Qual será preço do produto '))
    quantidade = int(input('Qual a quantidade? '))
    sql = """ insert into produtos (nome, categoria, preco, quantidade) values (%s, %s, %s, %s)"""
    cursor.execute(sql,(nome,categoria,preco,quantidade))
    conexao.commit()
    print(f'{nome} CADASTRADO COM SUCESSO!')


def buscar_produto():
    busca = int(input('Qual o id do produto em que você deseja buscar? '))
    sql = """select * from produtos where id = %s """
    cursor.execute(sql,(busca,))
    p = cursor.fetchone()
    if p is None:
        print('ID não encontrado!')
    else:
        print(f'ID: {p[0]}')
        print(f'Categoria: {p[1]}')
        print(f'Preço: {p[2]}')
        print(f'Quantidade: {p[3]}')


def alterar_preco():
    idp = int(input('Qual o id do produto na qual você deseja alterar o preço? '))
    novopreco = float(input('Qual será o novo preço? '))
    sql = """ update produtos set preco = (%s) where id = (%s)"""
    cursor.execute(sql,(novopreco,idp))
    if cursor.rowcount == 0:
        print('O ID inserido não foi encontrado!')
    else:
        print('Preço alterado com sucesso!')
    conexao.commit()


def deletar_linha():
    delete = int(input('Qual id do produto que você deseja Excluir? '))
    sql = """delete from produtos where id = %s"""
    cursor.execute(sql,(delete,))
    conexao.commit()
    print('OK')


listar_produtos()