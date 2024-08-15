import random
import time

def f_intercalar(l, l1, l2, cont_comp):
    i = 0
    j = 0
    k = 0
    while(i < len(l1)) and (j < len(l2)): #mescla as duas sublistas l1 e l2 em uma única lista l, enquanto conta as comparações
        cont_comp[0] += 1 #contador para cada comparação feita
        if l1[i] < l2[j]:
            l[k] = l1[i] #adiciona o elemento de l1 na lista resultante
            i += 1
        else:
            l[k] = l2[j] #adiciona o elemento de l2 na lista resultante
            j += 1
        k += 1
    
    while(i < len(l1)): #adiciona os elementos restantes de l1, se houver
        l[k] = l1[i]
        i += 1
        k += 1
    
    while(j < len(l2)): #adiciona os elementos restantes de l2, se houver
        l[k] = l2[j]
        j += 1
        k += 1

def f_mergeSort(l, cont_comp):
    if(len(l) <= 1):
        return l #se a lista tem 1 ou nenhum elemento, já está ordenada, seria o caso base
    else:
        meio = len(l) // 2  #calcula o ponto médio da lista
        l1 = l[:meio]  #divide a lista em duas partes
        l2 = l[meio:]  #divide a lista em duas partes
        f_mergeSort(l1, cont_comp) #ordena recursivamente as duas metades
        f_mergeSort(l2, cont_comp) #ordena recursivamente as duas metades
        f_intercalar(l, l1, l2, cont_comp) #mescla as duas metades ordenadas
        return l

def testar_merge_sort(lista): #função para testar o Merge Sort com uma lista e contar comparações
    cont_comp = [0] #contador de comparações
    inicio = time.time() #inicia o timer
    f_mergeSort(lista, cont_comp) #ordena a lista e conta as comparações
    fim = time.time() #paraliza o timer
    return cont_comp[0], fim - inicio #retorna o número de comparações e o tempo total

#criação de listas para os casos de teste
lista = [random.randint(1, 10000) for _ in range(50000)] #lista com 50.000 números aleatórios
listaDecrescente = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] #lista em ordem decrescente
listaCrescente = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #lista em ordem crescente

#testar o Merge Sort com a lista de 50.000 elementos
lista_50mil = lista.copy() #faz uma cópia da lista para manter a original inalterada
comparacoes50mil, tempo_total_50mil = testar_merge_sort(lista_50mil)  #ordena a lista e conta comparações

#testar o Merge Sort com a lista decrescente
lista_decrescente = listaDecrescente.copy() #faz uma cópia da lista para manter a original inalterada
comparacoesDecrescente, tempo_total_decrescente = testar_merge_sort(lista_decrescente) #ordena a lista e conta comparações

#testar o Merge Sort com a lista crescente
lista_crescente = listaCrescente.copy() #faz uma cópia da lista para manter a original inalterada
comparacoesCrescente, tempo_total_crescente = testar_merge_sort(lista_crescente) #ordena a lista e conta comparações

#exibir os resultados dos casos de teste
print(f"Lista ordenada: {lista_crescente[:10]}... (mostrando apenas os primeiros 10 números ordenados)")  #mostra apenas os primeiros 10 números da lista ordenada para não ocupar muito espaço da tela e para confirmar se a ordenação foi feita
print(f"Número de comparações com 50 mil elementos: {comparacoes50mil}  Tempo total para ordenar: {tempo_total_50mil:.4f} segundos") #mostra o número total de comparações e o tempo gasto para ordenar a lista de 50.000 elementos
print(f"Número de comparações com lista decrescente: {comparacoesDecrescente}  Tempo total para ordenar: {tempo_total_decrescente:.4f} segundos") #mostra o número total de comparações e o tempo gasto para ordenar a lista decrescente
print(f"Número de comparações com lista crescente: {comparacoesCrescente}  Tempo total para ordenar: {tempo_total_crescente:.4f} segundos") #mostra o número total de comparações e o tempo gasto para ordenar a lista crescente