## algoritmo de quick sort 
## tempo médio de execução de O(n log n)

def qsort(array):
    if len(array) < 2: 
        return array ## retorna a array, pois não há o que ordenar se a lista tiver somente um ou nenhum elemento
    else: 
        pivo = array[0] ## torna o primeiro número do array o pivô
        menores = [i for i in array[1:] if i <= pivo] ## cria uma lista com os "i" da array se eles forem menores ou iguais ao pivô e adicionam a uma lista chamada menores ([1:] significa que ele vai selecionar a lista interia a partir do índice 1, já que o 0 é o pivô)
        maiores = [i for i in array[1:] if i > pivo] ## cria uma lista com os "i" da array se eles forem maiores ao pivô e adicionam a uma lista chamada maiores
        return qsort(menores) + [pivo] + qsort(maiores)
    
print (qsort([10, 5, 2, 3, 100, 1, 35]))