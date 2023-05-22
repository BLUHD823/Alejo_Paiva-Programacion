import re

def reemplazar_caracteres(cadena,letra_1,letra_2):
    reemplazo = re.sub(letra_1,letra_2,cadena,2)
    return reemplazo

print(reemplazar_caracteres("Hola Mundo","o","a"))

