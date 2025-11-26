def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
        else:
            resultado += c
    return resultado
