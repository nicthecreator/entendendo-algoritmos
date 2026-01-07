def caixa_eletronico():
    saldo = 500.0  #Saldo Inicial

    while True:
        print("""---- CAIXA ELETRÔNICO ----
[1] Ver Saldo
[2] Depositar
[3] Sacar
[4] Sair
            """)
        
        opcao = input("Escolha uma das opções:\n")

        if opcao == "1":
            print(f"Seu saldo atual é: {saldo:.2f}\n")

        elif opcao == "2":
            valor = float(input("Quanto deseja depositar?\n"))
            if valor > 0:
                saldo += valor
                print("Deposito realizado com sucesso.\n")
            else:
                print("Valor Inválido.\n")

        elif opcao == "3":
            valor = float(input("Quanto deseja sacar?\n"))
            if 0 < valor <= saldo:
                saldo -= valor
                print("Saque realizado com sucesso.\n")
            elif valor > saldo:
                print("Saldo insuficiente.\n")
            else:
                print("Valor inválido.\n")

        elif opcao == "4":
            print("Encerrando... Volte sempre!\n")
            break
        else:
            print("Opção inválida.\n")

caixa_eletronico()