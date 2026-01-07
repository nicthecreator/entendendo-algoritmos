import random

def adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    print("Tente adivinhar o número entre 1 e 100!")

    while True:
        palpite = int(input("Qual seu palpite? "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Mais alto...")
        elif palpite > numero_secreto:
            print("Mais baixo...")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break

adivinhacao()