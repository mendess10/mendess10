from usuarios.usuario import usuario_cadastro, verificar_credenciais
from produtos.produto import pagina_produto
# INICIO DE CADASTRO/LOGIN

while True: 
    print("""BEM-VINDO AO ALPHA.COM
            1-CADASTRAR
            2-LOGIN
            X-SAIR""")
    try:
    #ESCOLHA DE AÇÃO INICIAL
        opcao= int(input("DIGITE A OPÇÃO DESEJADA: "))
        if opcao == 1:
            cadastro = usuario_cadastro()
            print("CADASTRO FEITO COM SUCESSO!")
        elif opcao == 2:
    # Solicitar email e senha ao usuário
            valido = False
    # Verificar credenciais
            while(not valido):
                login_email = input("DIGITE SEU EMAIL DE CADASTRO: ").lower()
                login_senha = input("DIGITE SUA SENHA DE CADASTRO: ")
                valido = verificar_credenciais(login_email, login_senha, cadastro)
                if valido:
                    pagina_produto()
        elif opcao == "X":
            break
        else:
            print("OPÇÃO ESCOLHIDA É INVALIDA, POR FAVOR ESCOLHER UMA OPÇÃO VALIDA!")
            continue
    except ValueError:
        print("SAINDO...")
        break
        