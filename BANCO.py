usuarios = []
saldo = []
session = []

login_sucesso = False
#add saldo
def add_saldo(s,cpf):
    print(f"O valor {s} foi depositado.")

def cadastrar():
    
    usuario = input("digite seu nome:")
    cpf = input("Digite seu cpf: ")
    senha = input("Senha:")
    usuarios.append({"cpf": cpf, "senha": senha, "usuario" : usuario})
    print(f"cpf cadastrado com sucesso!")

    saldo.append({"cpf":cpf,"saldo": 00})
    print("Seu saldo é 0,00")

def login():
    nome = input("cpf:")
    senha = input("Senha:")
    global login_sucesso
    login_sucesso = False
    for u in usuarios:
        if u["cpf"] == nome and u["senha"] == senha:
            login_sucesso = True
            global session
            session = {"cpf": u["cpf"], "usuario" :u["usuario"]}
           #1 print (session)
            print(f"Acesso liberado Seja bem vindo! {u['usuario']}")
            
            break
        print("falha no login")
   

def trocar_senha():
    nome = input("cpf: ")
    senha_atual = input("Senha atual: ")
    for user in usuarios:
        if user["cpf"] == nome and user["senha"] == senha_atual:
            user["senha"] = input("Nova senha: ")
            print("Senha atualizada!")
            return
    print("Dados invalidos.")

def sistema():
    while True:
        global login_sucesso
        if login_sucesso:
            print("\n1. Adicionar saldo | 2. Trocar Senha | 3. Sair")
            opcao = input("Escolha: ")

            match opcao:
                case "1":
                    if login_sucesso:
                        global session
                        cpf = session["cpf"] 
                        s = float(input("informe o valor do deposito:"))
                        add_saldo(s, cpf)
                case "2":
                    trocar_senha()
                case "3":
                    print("Saindo...")
                    login_sucesso = False
                    session = {}
                    print (session)
                case _:
                    print("opção invalida.")
        else:
            print("\n1. Cadastrar | 2. Login | 3. Trocar Senha | 4. Sair do programa")
            opcao = input("Escolha: ")

            match opcao:
                case "1":
                    cadastrar()
                case "2":
                    login()
                case "3":
                    trocar_senha()
                case "4":
                    print("Saindo...")
                    # global login_sucesso
                    login_sucesso = False
                    break
                case _:
                    print("opção invalida.")
sistema()
