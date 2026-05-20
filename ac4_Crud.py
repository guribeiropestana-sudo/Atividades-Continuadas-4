# Avaliação Continuada 4 - 1 ponto
# PROJETO DE VENDAS - parte 2
# Exercicios de CRUD completo (Produtos, Vendedores e Vendas)
# Entrega - dia 24/05/2026

from mysql.connector import Error
from conexao import conectar,fechar_conexao
# PRODUTOS

def criar_produto():
    # Exercicio 1: cadastrar um novo produto na tabela produtos (descricao, preco).
    
    conexao = conectar()

    if not conexao:
        return
    
    cursor = None
    try:
        cursor = conexao.cursor()

        descricao = input('Digite a descrição do produto: ').strip()
        preco = float(input('Digite o preço do produto: R$'))

        sql = """INSERT INTO produtos (descricao,preco)
        VALUES (%s, %s)"""
        
        valores = (descricao,preco)
        
        cursor.execute(sql,valores)
        
        conexao.commit()
        
        print('\nProduto cadastrados com sucesso! ')
    
    except Error as erro:
        print(f'Erro ao cadastrar produto: {erro}')
    
    finally:
        if cursor:
            cursor.close()
        fechar_conexao(conexao)


def listar_produtos():
    conexao = conectar()
    if not conexao:
        return
    cursor = None
    try:
        cursor = conexao.cursor()
        
        sql = " SELECT id, descricao, preco FROM produtos"
        
        cursor.execute(sql)

        produtos = cursor.fetchall()

        if not produtos:
            print('\nNenhum produto cadastrado no momento.')
            return
        print('\n===LISTA DE PRODUTOS===')
        
        for produto in produtos:
            print(f""" 
ID: {produto[0]}
Descrição: {produto[1]}
Preço: R${produto[2]:.2f}
--------------------------
""")
    
    except Error as erro:
        print(f'\nErro ao listar os produtos: {erro}')
     
    finally:
        if cursor:
            cursor.close()
        fechar_conexao(conexao)


def atualizar_produto():
    # Exercicio 3: atualizar descricao e/ou preco de um produto existente por id.
    conexao = conectar()
    if not conexao:
        return
    cursor = None
    try: 
        cursor = conexao.cursor()
        while True:
            id_produto = int(input('Digite o id do produto que deseja atualizar: '))
            
            sql_verificar = "SELECT * FROM produtos WHERE id=%s"

            cursor.execute(sql_verificar,(id_produto,))

            produto = cursor.fetchone()
            
            if not produto:
                print('\nProduto não encontrado.')
                continue
            
            print('\n===PRODUTO SELECIONADO===')
            print(f"""
            ID: {produto[0]}
            Descrição atual: {produto[1]}
            Preço atual: R${produto[2]:.2f}""")
            
            confirmacao = input('Esse é o produto certo? s/n ').strip().lower()
            
            if not confirmacao:
                print('Digite uma resposta válida.')
            
            confirmacao = confirmacao[0]

            if confirmacao == 's':
                break
            
            elif confirmacao == 'n':
                print('\nSelecione outro produto.')
                continue
            
            else:
                print('Opção inválida.')

        nova_descricao = input('Nova descrição do produto: ').strip()
        novo_preco = float(input('Novo preço do produto: R$'))

        sql = """
        UPDATE produtos
        SET descricao = %s, preco = %s
        WHERE id = %s"""
            
        valores = (nova_descricao, novo_preco, id_produto)
            
        cursor.execute(sql, valores)
        
        conexao.commit()
        
        print('\nProduto atualizado com sucesso! ')
    
    except Error as erro:
        print(f'Erro ao atualizar o produto: {erro}')
    
    except ValueError:
        print('\nDigite valores válidos. ')
    
    finally:
        if cursor:
            cursor.close()
        fechar_conexao(conexao)

                                
def excluir_produto():
    # Exercicio 4: excluir um produto por id, tratando dependencias em vendas_produtos.
    conexao = conectar()
    if not conexao:
        return
    cursor = None
    try: 
        cursor = conexao.cursor()

        while True: 
    
            id_produto = int(input('Digite o id do produto que deseja deletar: '))
            
            sql_verificar = 'SELECT * FROM produtos WHERE id=%s'
            
            cursor.execute(sql_verificar,(id_produto,))
            
            produto = cursor.fetchone()
            
            if not produto:
                print('\nNenhum produto encontrado.')
                continue
            
            print('\n===PRODUTO SELECIONADO===')
            print(f"""
            ID: {produto[0]}
            Descrição: {produto[1]}
            Preço: R${produto[2]:.2f}
            --------------------
            """)

            confirmacao = input('Deseja excluir esse produto? s/n ').strip().lower()
            
            if not confirmacao:
                print('\nDigite uma opção válida')
                continue
            
            confirmacao = confirmacao[0]
            
            if confirmacao == 's':
                break

            elif confirmacao == 'n':
                print('\nSelecione outro produto.')
                continue
            
            else:
                print('\nOpção inválida.')
        sql = "DELETE FROM produtos WHERE id = %s"
        cursor.execute(sql,(id_produto,))
        conexao.commit()
        print('\nProduto excluído com sucesso! ')
    
    except Error as erro:
        print(f'\nErro ao excluir produto: {erro}')
    
    except ValueError:
        print('\nDigite um id válido.')
    
    finally:
        if cursor:
            cursor.close()    
        fechar_conexao(conexao)

# VENDEDORES

def criar_vendedor():
    # Exercicio 5: cadastrar um novo vendedor na tabela vendedores.
    conexao = conectar()
    if not conexao:
        return
    
    cursor = None
    try:
        cursor = conexao.cursor()
        
        nome = input('Digite o nome do vendedor: ').strip()
        
        sql = 'INSERT INTO vendedores(nome) VALUES (%s)'
        
        valores = (nome,)
        
        cursor.execute(sql,valores)

        conexao.commit()

        print('\nVendedor cadastrado com sucesso!')
    
    except Error as erro:
        print(f'\nErro ao cadastrar um vendedor: {erro}')
    
    except ValueError:
        print('\nDigite um nome válido.')
    
    finally:
        if cursor:
            cursor.close()
        fechar_conexao(conexao)

def listar_vendedores():
    # Exercicio 6: listar todos os vendedores cadastrados.
    conexao = conectar()
    if not conexao:
        return
    
    cursor = None
    try:
        cursor = conexao.cursor()
        
        sql = 'SELECT id, nome FROM vendedores'
        
        cursor.execute(sql)
        
        vendedores = cursor.fetchall()
        
        if not vendedores:
            print('\nNão há vendedores cadastrados no momento.')
        
        print('\n===LISTA DE VENDEDORES===')
        
        print(f"""
            ID: {vendedores[0]}
            Nome: {vendedores[1]}
            ---------------------
            """)

    except Error as erro:
        print(f'\nErro ao listar os vendedores: {erro}')

    finally:
        if cursor:
            cursor.close()
        
        fechar_conexao(conexao)

def atualizar_vendedor():
    # Exercicio 7: atualizar o nome de um vendedor existente por id.
    conexao = conectar()
    if not conexao:
        return
    
    cursor = None
    try:
        cursor = conexao.cursor()
        while True:
            id_vendedor = int(input('Digite o id do vendedor que deseja atualizar: '))
            
            sql_verificar = 'SELECT * FROM vendedores WHERE id = %s'
            
            cursor.execute(sql_verificar,(id_vendedor,))
            
            vendedor = cursor.fetchone()
            
            if not vendedor:
                print('\nNenhum vendedor encontrado.')
                continue
            
            print('\n===VENDEDOR SELECIONADO===')
            
            print(f"""
            ID: {vendedor[0]}
            Nome: {vendedor[1]}
            -------------------
            """)
            
            confirmacao = input('Esse é o vendedor certo? s/n').strip().lower()
            
            if not confirmacao:
                print('Digite uma resposta válida.')
                continue
            
            confirmacao = confirmacao[0]
            
            if confirmacao == 's':
                break
            
            elif confirmacao == 'n':
                print('\nSelecione outro vendedor.')
                continue
            
            else:
                print('Opção inválida.')
        novo_nome = input('Novo nome do vendedor: ').strip()
        sql = """
        UPDATE vendedores
        SET nome = %s 
        WHERE id = %s"""
        valores = (novo_nome, id_vendedor)
        cursor.execute(sql,valores)
        conexao.commit()
        print('\nVendedor atualizado com sucesso! ')

    except Error as erro:
        print(f'\nErro ao atualizar o vendedor: {erro}')
    
    except ValueError:
        print('\nDigite valores válidos. ')

    finally:
        if cursor:
            cursor.close()
        
        fechar_conexao(conexao)


def excluir_vendedor():
    # Exercicio 8: excluir vendedor por id, validando se possui vendas vinculadas.
    conexao = conectar()
    if not conexao:
        return
    
    cursor = None
    try:
        cursor = conexao.cursor()
        while True:
            id_vendedor = int(input('Digite o id do vendedor que deseja excluir: '))
            sql_verificar = 'SELECT * FROM vendedores WHERE id = %s'
            cursor.execute(sql_verificar,(id_vendedor,))
            vendedor = cursor.fetchone()
            if not vendedor:
                print('\nNenhum vendedor encontrado.')
            print('\n===VENDEDOR SELECIONADO===')
            print(f"""
            ID: {vendedor[0]}
            Nome: {vendedor[1]}
            ------------------""")

            confirmacao = input('Deseja excluir este vendedor? (s/n): ').strip().lower()

            if not confirmacao:
                print('\nDigite uma resposta válida.')
                continue

            confirmacao = confirmacao[0]

            if confirmacao == 's':
                break

            elif confirmacao == 'n':
                print('\nSelecione outro vendedor.')
                continue

            else:
                print('\nOpção inválida.')
        
        sql = 'DELETE FROM vendedores WHERE id = %s'
        cursor.execute(sql,(id_vendedor,))
        conexao.commit()
        print('\nVendedor excluído com sucesso! ')


    except Error as erro:
        print(f'\nErro ao atualizar o vendedor: {erro}')
    
    except ValueError:
        print('\nDigite valores válidos. ')

    finally:
        if cursor:
            cursor.close()
        
        fechar_conexao(conexao)


# VENDAS

def criar_venda_com_itens():
    # Exercicio 9: criar uma venda e inserir itens na tabela vendas_produtos com quantidade e valores.
    return


def listar_vendas_completas():
    # Exercicio 10: listar vendas com vendedor e itens (produto, quantidade, valor_unitario, valor_total).
    return


def atualizar_venda_e_itens():
    # Exercicio 11: atualizar dados da venda (desconto/valor_final) e seus itens.
    return


def excluir_venda():
    # Exercicio 12: excluir uma venda por id removendo primeiro os itens de vendas_produtos.
    return


def menu():
    opcoes = {
        "1": ("Criar produto", criar_produto),
        "2": ("Listar produtos", listar_produtos),
        "3": ("Atualizar produto", atualizar_produto),
        "4": ("Excluir produto", excluir_produto),
        "5": ("Criar vendedor", criar_vendedor),
        "6": ("Listar vendedores", listar_vendedores),
        "7": ("Atualizar vendedor", atualizar_vendedor),
        "8": ("Excluir vendedor", excluir_vendedor),
        "9": ("Criar venda com itens", criar_venda_com_itens),
        "10": ("Listar vendas completas", listar_vendas_completas),
        "11": ("Atualizar venda e itens", atualizar_venda_e_itens),
        "12": ("Excluir venda", excluir_venda),
    }

    while True:
        print("\n=== MENU AC4 - CRUD COMPLETO ===")
        for codigo, (descricao, _) in opcoes.items():
            print(f"{codigo} - {descricao}")
        print("0 - Sair")

        escolha = input("Escolha uma opcao: ").strip()

        if escolha == "0":
            print("Voltando ao menu principal.")
            break

        if escolha in opcoes:
            descricao, funcao = opcoes[escolha]
            print(f"\nSelecionado: {descricao}")
            funcao()
            print("Exercicio em estrutura base (return vazio).")
        else:
            print("Opcao invalida. Tente novamente.")
