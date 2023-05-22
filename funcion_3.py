def ordenar_caracteres(cadena, des):
    lista = []
    for caracter in cadena:
        lista.append(caracter)

    tam = len(lista)

    for i in range(0, tam-1):
        for j in range(i + 1, tam):
            if (des and lista[i] < lista[j]) or (not des and  lista[i] > lista[j]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    chain = ' '.join(lista)
    return chain

print(ordenar_caracteres("algoritmo", False))