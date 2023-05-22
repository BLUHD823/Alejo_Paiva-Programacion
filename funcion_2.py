import re

def reemplazar_caracteres(cadena,letra_1,letra_2):
    contador = cadena.count("o")
    reemplazo = re.sub(letra_1,letra_2,cadena,2)
    return reemplazo,contador

print(reemplazar_caracteres("Hola Mundo","o","a"))

