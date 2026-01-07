nota1 = float(input("Digite a sua primeira nota: \n"))
nota2 = float(input("Digite a sua segunda nota: \n"))
nota3 = float(input("Digite a sua terceira nota: \n"))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Parabéns, você foi aprovado!\nSua média = {media}. ")
else:
    print(f"Infelizmente você não conseguiu média suficiente.\nSua média = {media}.")