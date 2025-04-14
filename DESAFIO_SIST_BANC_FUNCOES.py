def menu():
    menu = """  ======== Banco Brasileiro - Menu ======= 
    Bem-vindo (a)! Para prosseguir, informe uma das opções abaixo:

    [d] Depósito
    [s] Saque 
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair 
    -->> """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato = f"Depósito: R$ {valor:.2f}\n"
        print("OPERAÇÃO REALIZADA COM SUCESSO.")
    else:
        print("Falha na operação! VALOR INVÁLIDO.")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_numero_saques = numero_saques >= LIMITE_SAQUES
    if excedeu_saldo:
        print("Falha na operação! Saldo insuficiente.")
    elif excedeu_limite:
        print("Falha na operação! O valor do saque excede o limite.")
    elif excedeu_numero_saques:
        print("Falha na operação! O número de saques excede o limite.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Falha na operação! VALOR INVÁLIDO.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO =================")
    print("Sem movimentações no momento." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("===========================================")

def cria_usuario (usuarios):
    cpf = input("Informe o seu cpf (somente números): \n")
    usuario = filtro_usuario (cpf, usuarios)

    if usuario:
        print("Já existe usuário com o cpf informado!")
        return
    nome = input("Informe o seu nome completo: \n")
    data_nasc = input("Informe a sua data de nascimento (d/m/a): \n")
    endereco = input("Informe o seu endereço (logradouro, nº, bairro, cidade, Estado): \n")

    usuarios.append({"nome": nome, "data_nasc": data_nasc, "endereco": endereco})
    print("Usuário cadastrado com sucesso!\n")

def filtro_usuario (cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] = cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta (agencia, numero_conta, usuarios):
    cpf = input("Informe o seu cpf: \n")
    usuario = filtro_usuario (cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado. Encerrando a sessão.")
