num = int(input("Você deseja ver a tabuada de qual número? \n"))

print(f"\n --- Tabuada do {num} ---")
for a in range(1, 11):
    resultado = num * a
    print(f"{num} x {a} = {resultado}")