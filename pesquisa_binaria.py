## pesquisa binária
## funciona somente para listas ordenadas
## O(log n)

def pesquisa_binaria(lista, item):
    baixo = 0   ## define baixo como 0 (ou seja, primeiro índice)
    alto = len(lista) - 1   ## define alto como o tamanho da lista - 1 (ou seja, último índice)

    while baixo <= alto:    ## enquanto o baixo for menor ou igual ao alto...
        meio = (baixo + alto) // 2  ## meio será (baixo + alto) / 2, sempre arredondando para baixo
        chute = lista[meio] ## o índice do meio é atribuído a chute
        if chute == item:   ## se chute for igual ao item procurado...
            return meio     ## retorna o valor em meio
        if chute > item:    ## se chute for maior que item...
            alto = meio - 1    ## alto será meio - 1, ou seja, irá eliminar as possibilidades iguais ou superiores a meio
        else:   ## senão
            baixo = meio + 1 ## baixo será meio + 1, ou seja, irá eliminar as possibilidades iguais ou inferiores a meio
    return None     ## caso não ache, retorna none

minha_lista = [1, 3, 5, 7, 9]

print (pesquisa_binaria(minha_lista, 3))
print (pesquisa_binaria(minha_lista, -1))