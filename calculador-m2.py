print("Calcule quantos litros de tinta são necessários para pintar sua parede.")
largura = float(input("Insira a largura da parede em metros: "))
altura = float(input("Insira a altura da parede em metros: "))
area = altura * largura

quantidadeTinta = area / 2

print(f"Para pintar essa parede, você precisará de {quantidadeTinta}l de tinta.")
