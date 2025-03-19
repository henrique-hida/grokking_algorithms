## ordenação por seleção
## caso médio de execução de O(n^2)

def buscaMenor(arr):
    menor = arr[0]  ## define menor como o primeiro item do array
    menor_indice = 0    ## define o índice do número menor como 0
    for i in range(1, len(arr)):    ## para cada i entre o segundo item e o último...
        if arr[i] < menor:  ## se o item for menor que o menor
            menor = arr[i]  ## o item se torna o menor
            menor_indice = i    ## o índice do menor será o índice
    return menor_indice

def ordenacaoPorSelecao(arr):
    novoArr = []    ## inicializa um novo array vazio
    for i in range(len(arr)):   ## para i entre o primeiro item e o último...
        menor = buscaMenor(arr) ## atribui o menor_indice a menor
        novoArr.append(arr.pop(menor))  ## remove o elemento que está no índice menor e adiciona ao novoArr
    return novoArr

print (ordenacaoPorSelecao([5, 3, 6, 2, 10]))