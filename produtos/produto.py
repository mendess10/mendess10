produto_cadastrado = {}
lista_produto = []
# Função para cadastrar um produto
def cadastrar_produto():
    #ID DO PRODUTO
    produto_cadastrado["ID"] = int(input("ID do produto: "))
    #NOME DO PRODUTO
    produto_cadastrado["Nome"] = input("Nome do produto: ").upper().strip()
    #PREÇO DO PRODUTO
    produto_cadastrado["Preço"] = float(input("Preço do produto: R$"))
    #ARMAZENANDO PRODUTO
    lista_produto.append(produto_cadastrado.copy())
    return lista_produto
#FUNÇÃO PARA SELECIONAR O PRODUTO PARA EDITAR
def selecionar_produto(lista_produto):
    print("LISTA DE PRODUTO:")
    for produto in lista_produto:
        print(f"{produto}")
        id_produto = int(input("DIGITE O ID DO PRODUTO QUE DESEJAR EDITAR: "))
        for produto in lista_produto:
            if produto ["ID"] == id_produto:
                return produto
    print("ID INVÁLIDO.")
#EDITOR DE PRODUTO
def editar_produto(produto, chave, novo_valor):
    if chave in produto:
        produto[chave] = novo_valor
        return True
    else:
        print(f"A {chave} NÃO EXISTE NO PRODUTO")
        return False


#LISTAGEM DE PRODUTOS
def listagem_produto():
    print("LISTA DE PRODUTOS CADASTRADOS: ")
    for produto in lista_produto:
        print(f"{produto}")
    
#EXCLUIR PRODUTO
def excluir_produto(lista_produto, id_produto):
    for produto in lista_produto:
        if produto["ID"] == id_produto:
            lista_produto.remove(produto)
            print(f"PRODUTO COM O ID {id_produto} REMOVIDO!")
            return True
    print(f"PRODUTO COM O ID {id_produto} NÃO ESTÁ NO CADASTRO")
    return False
    
#PAGINA PRINCIPAL DO PRODUTO
def pagina_produto():
    while True:
            print("""
                1-CADASTRAR PRODUTO
                2-EDITAR PRODUTO
                3-EXIBIR PRODUTO
                4-EXCLUIR PRODUTO
                X-SAIR
                    """)
            try:
                opcao= int(input("DIGITE A OPÇÃO DESEJADA: "))
            #OPÇÃO DE CADASTRO
                if opcao == 1:
                    _ = cadastrar_produto()
                    print("CADASTRO FEITO COM SUCESSO!")
                    continue
            #OPÇÃO DE EDIÇÃO
                elif opcao == 2:
            #ESCOLHA DO PRODUTO QUE DESEJAR EDITAR
                    selecionando_produto = selecionar_produto(lista_produto)
                    chave_produto= str(input(f"DIGITE O QUE DESEJA EDITAR: ")).capitalize().strip()
            #NOVO VALOR
                    novo_valor= str(input((f"DIGITE O NOVO {chave_produto}: "))) 
                    if  editar_produto(selecionando_produto, chave_produto, novo_valor):
                        print("PRODUTO EDITADO.")
                    continue
            #OPÇÃO DE EXIBIÇÃO
                elif opcao == 3:
                    listagem = listagem_produto()
                    print(listagem)
            #OPÇÃO DE EXCLUSÃO
                elif opcao == 4:
                    id_produto= int(input("DIGITE O ID DO PRODUTO QUE DESEJA EXCLUIR: "))
                    excluir =  excluir_produto(lista_produto, id_produto)
                    continue
                elif opcao == "X":
                    break
                else:
                    print("ESCOLHA UMA OPÇÃO VÁLIDA!")
                    continue
            except ValueError:
                print("SAINDO...")
                break
