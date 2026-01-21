import math
co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
hi = math.hypot(co, ca)
print(f"A hipotenusa vai medir: {hi:.2f}")