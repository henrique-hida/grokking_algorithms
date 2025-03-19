## programa para encontrar índice de números em uma lista desordenada

## qsort
def qsort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if pivo >= i]
        maiores = [i for i in array[1:] if pivo < i]
        return qsort(menores) + [pivo] + qsort(maiores)
    

## binary search
def bsearch(array, procura):
    arrayOrdem = qsort(array)
    indiceInicial = 0
    indiceFinal = len(arrayOrdem) - 1

    while indiceInicial <= indiceFinal:
        metade = (indiceInicial + indiceFinal) // 2
        teste = arrayOrdem[metade]
        if teste == procura:
            print (arrayOrdem)
            return metade
        elif teste <= procura:
            indiceInicial = metade + 1
        elif teste > procura:
            indiceFinal = metade - 1
    return None

print(bsearch([1, 3, 2, 10, 7, 21, 9, 30], 7))