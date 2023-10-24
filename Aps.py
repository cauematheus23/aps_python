import requests
import matplotlib.pyplot as plt
def gerar_datas_aleatorias(qtd_datas):
    url = "https://www.random.org/calendar-dates/"
    datas_aleatorias = []
    
    for _ in range(qtd_datas):
        response = requests.get(url)
        data = response.text.strip()
        datas_aleatorias.append(data)
    
    return datas_aleatorias

# Exemplo de uso para gerar 10 datas aleatórias
datas_aleatorias = gerar_datas_aleatorias(1000)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergesort(left_half)
        mergesort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def selectionsort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Exemplo de uso para ordenar as datas aleatórias com QuickSort
datas_ordenadas = quicksort(datas_aleatorias)


import time

def medir_tempo_ordenacao(algoritmo, dados):
    inicio = time.time()
    algoritmo(dados)
    fim = time.time()
    return fim - inicio

# Lista de quantidades de dados para testar
quantidades = [10, 20, 30, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Lista para armazenar os tempos de ordenação
tempos_quick = []

# Medir o tempo de ordenação para cada quantidade de dados
for qtd in quantidades:
    dados = datas_aleatorias[:qtd]  # Usar um subconjunto dos dados
    tempo = medir_tempo_ordenacao(quicksort, dados)
    tempos_quick.append(tempo)

# Criar o gráfico
plt.plot(quantidades, tempos_quick, label="QuickSort")
plt.xlabel("Quantidade de Datas")
plt.ylabel("Tempo de Ordenação (s)")
plt.legend()
plt.show()
