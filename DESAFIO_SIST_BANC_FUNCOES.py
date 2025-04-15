def menu():
    menu = """  ======== Banco Brasileiro - Menu ======= 
    Bem-vindo (a)! Para prosseguir, informe uma das opções abaixo:

    [d] Depósito
    [s] Saque 
    [e] Extrato
    [nc] Nova conta
    [nu] Novo usuário
    [lc] Listar contas
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
    excedeu_numero_saques = numero_saques >= limite_saques
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
    return saldo, extrato, numero_saques

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

    usuarios.append({"nome": nome, "data_nasc": data_nasc, "endereco": endereco, "cpf": cpf})
    print("Usuário cadastrado com sucesso!\n")

def filtro_usuario (cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta (agencia, numero_conta, usuarios):
    cpf = input("Informe o seu cpf: \n")
    usuario = filtro_usuario (cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado. Encerrando a sessão.")

def listar_contas (contas):
    for conta in contas:
        linha = f"Agência:\t{conta['agencia']} \n\tC/C:\t{conta['numero_conta']}\n\tTitular:\t{conta['usuario']['nome']}"
        print("=" * 100)
        print(linha)


def main():
    LIMITE_SAQUES = 3 
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques= 0
    usuarios = []
    contas = []

    while True:
        opcao = menu ()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = saque(
                saldo = saldo,
                valor = valor,
                extrato= extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques =LIMITE_SAQUES,
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            cria_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas)+ 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            break

main()

        









    
    