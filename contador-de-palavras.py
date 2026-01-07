def contar_palavras(texto):
    palavras = texto.lower().split()
    frequencia = {}

    for p in palavras:
        # Remove pontuação básica
        p = p.strip(",.!?")
        frequencia[p] = frequencia.get(p, 0) + 1
    
    return frequencia

frase = "Python é incrível, e aprender Python é muito divertido!"
resultado = contar_palavras(frase)
print(resultado)