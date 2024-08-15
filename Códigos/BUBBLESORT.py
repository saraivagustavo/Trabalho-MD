import random
import time

def f_troca(l, i, j):  #função de troca auxiliar para o Bubble Sort
    #troca os elementos nas posições i e j da lista l
    aux = l[i]
    l[i] = l[j]
    l[j] = aux 

def f_bubbleSort(l):
    verificar = True  #inicialização da variável para verificar se houve troca na última passagem
    reps = 0  #contador de repetições do loop externo
    comparacoes = 0  #contador de para registrar o número de comparações feitas ao longo da lista
    
    while(verificar):  #continua executando enquanto houver trocas (enquanto continuar True)
        verificar = False  #reseta a verificação de troca a cada nova passagem
        for i in range(len(l)-1-reps):  #loop interno para comparar elementos adjacentes
            comparacoes += 1  #incrementa +1 ao contador a cada comparação realizada
            if(l[i] > l[i+1]):  #verifica se o elemento atual é maior que o próximo
                f_troca(l, i, i+1)  #realiza a troca dos elementos através da função auxiliar mencionada acima
                verificar = True  #marca que houve uma troca, voltando a variável "verificar", que tinha sido alterada para False, para True
        reps += 1  #incrementa o número de repetições, movendo o maior elemento para o final
    return comparacoes  #retorna o número total de comparações feitas durante todo o loop

#criação de listas para os casos de testes
lista = [random.randint(1, 10000) for _ in range(50000)]  #lista com 50.000 números aleatórios
listaDecrescente = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  #lista em ordem decrescente
listaCrescente = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  #lista em ordem crescente

#testar o Bubble Sort com cada lista gerada
#teste para lista com 10.000 elementos aleatórios
inicio50mil = time.time()  #inicia o timer para o caso de 50.000 elementos
comparacoes50mil = f_bubbleSort(lista)  #irdena a lista e conta as comparações
fim50mil = time.time()  #paraliza o timer após a ordenação

#teste para lista decrescente
inicioDecrescente = time.time()  #inicia o timer para o caso da lista decrescente
comparacoesDecrescente = f_bubbleSort(listaDecrescente)  #ordena a lista e conta as comparações
fimDecrescente = time.time()  #paraliza o timer após a ordenação

#teste para lista crescente
inicioCrescente = time.time()  #inicia o timer para o caso da lista crescente
comparacoesCrescente = f_bubbleSort(listaCrescente)  #ordena a lista e conta as comparações
fimCrescente = time.time()  #paraliza o timer após a ordenação

#calcular o tempo total para cada caso
tempo_total_50mil = fim50mil - inicio50mil  #tempo total gasto para ordenar 10.000 elementos
tempo_total_decrescente = fimDecrescente - inicioDecrescente  #tempo total gasto para ordenar a lista decrescente
tempo_total_crescente = fimCrescente - inicioCrescente  #tempo total gasto para ordenar a lista crescente

#exibir os resultados dos casos de testes
print(f"Lista ordenada: {lista[:10]}... (mostrando apenas os primeiros 10 números ordenados)") #mostra apenas os primeiros 10 números da lista ordenada para não ocupar muito espaço da tela e para confirmar se a ordenação foi feita
print(f"Número de comparações com 50 mil elementos: {comparacoes50mil}  Tempo total para ordenar: {tempo_total_50mil:.4f} segundos") #mostra o número total de comparações e o tempo gasto para ordenar a lista de 10.000 elementos
print(f"Número de comparações Decrescente: {comparacoesDecrescente}  Tempo total para ordenar: {tempo_total_decrescente:.4f} segundos") #mostra o número total de comparações e o tempo gasto para ordenar a lista decrescente
print(f"Número de comparações Crescente: {comparacoesCrescente}  Tempo total para ordenar: {tempo_total_crescente:.4f} segundos") #mostra o número total de comparações e o tempo gasto para ordenar a lista crescente