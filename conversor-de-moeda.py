opcao = int(input("""
SISTEMA DE CONVERSÃO DE MOEDAS
---Escolha uma opção---
[1] Dolar para real
[2] Real para dolar
"""))

if opcao == 1:
    valor = float(input("\nVocê selecionou a opção número 1 (Dolar para Real).\n" \
    "Digite o valor que deseja converter:\n"))
    valorDollar = valor * 5.37
    print(f"Conversão de valor em dolar para real é: R${valorDollar}.")
elif opcao == 2:
    valor = float(input("Você selecionou a opção número 2 (Real para Dolar).\n" \
    "Digite o valor que deseja converter:\n"))
    valorReal = valor * 0.19
    print(f"Conversão de valor em real para dolar é: ${valorReal}.")
else:
    print("Valor inválido, porfavor tente novamente.")
