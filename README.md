# DIO SISTEMA BANCARIO
## Esse projeto é referente ao desafio do Bootcamp SUZANO - PYTHON DEVELOPER

menu = """ ======== Banco Brasileiro - Menu ======= 
    Bem-vindo (a)! Para prosseguir com o autoatendimento, informe uma das opções abaixo:

    [d] Depósito
    [s] Saque 
    [e] Extrato
    [q] Sair
    
=============>> """
saldo = 0
limite = 500
extrato = ""
numero_saques= 0
LIMITE_SAQUES = 3

while True:
    opcao = input (menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: \n"))
        if valor > 0:
            saldo += valor
            extrato = f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Falha na operação! VALOR INVÁLIDO.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
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
    
    elif opcao == "e":
        print("\n=============== EXTRATO =================")
        print("Sem movimentações no momento." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("===========================================")
   
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida. Favor digite novamente a opção.")
menu = """ ======== Banco Brasileiro - Menu ======= 
    Bem-vindo (a)! Para prosseguir com o autoatendimento, informe uma das opções abaixo:

    [d] Depósito
    [s] Saque 
    [e] Extrato
    [q] Sair
    
=============>> """
saldo = 0
limite = 500
extrato = ""
numero_saques= 0
LIMITE_SAQUES = 3

while True:
    opcao = input (menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: \n"))
        if valor > 0:
            saldo += valor
            extrato = f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Falha na operação! VALOR INVÁLIDO.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
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
    
    elif opcao == "e":
        print("\n=============== EXTRATO =================")
        print("Sem movimentações no momento." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("===========================================")
   
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida. Favor digite novamente a opção.")

