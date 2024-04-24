#FUNÇÃO PARA CADASTRAR USUARIOS
def usuario_cadastro():
    cadastro_usuario = {}
    # CADASTRAR NOME
    nome = input("INSIRA SEU NOME: ").upper().strip()

    # CADASTRAR TELEFONE
    telefone = str(input("INSIRA SEU TELEFONE: "))

    # CADASTRAR O E-MAIL
    email = input("INSIRA SEU EMAIL: ").lower().strip()
    senha = ""
    # CADASTRAR SENHA
    while True:
        senha = input("INSIRA A SENHA: ")
        if len(senha) < 6:
            print("SENHA PRECISA TER NO MÍNIMO 6 DIGITOS!")
            continue
        else:
            break
    cadastro_usuario["Nome"] = nome
    cadastro_usuario["Telefone"] = telefone
    cadastro_usuario[email] = senha
    return cadastro_usuario

# Função para verificar as credenciais
def verificar_credenciais(email, senha, cadastro):
    # Verificar se o email está no dicionário
    if email in cadastro:
        # Verificar se a senha corresponde ao email fornecido
        if cadastro[email] == senha:
            print("Login bem-sucedido!")
            return True
        else:
            print("Senha incorreta.")
            return False
    else:
        print("Email não encontrado.")
        return False