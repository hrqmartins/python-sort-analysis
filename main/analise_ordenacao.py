import random
import time
import sys
import matplotlib.pyplot as plt

def titulo():
    print('''

░█████╗░██╗░░░░░░██████╗░░█████╗░██████╗░██╗████████╗███╗░░░███╗░█████╗░░██████╗
██╔══██╗██║░░░░░██╔════╝░██╔══██╗██╔══██╗██║╚══██╔══╝████╗░████║██╔══██╗██╔════╝
███████║██║░░░░░██║░░██╗░██║░░██║██████╔╝██║░░░██║░░░██╔████╔██║██║░░██║╚█████╗░
██╔══██║██║░░░░░██║░░╚██╗██║░░██║██╔══██╗██║░░░██║░░░██║╚██╔╝██║██║░░██║░╚═══██╗
██║░░██║███████╗╚██████╔╝╚█████╔╝██║░░██║██║░░░██║░░░██║░╚═╝░██║╚█████╔╝██████╔╝
╚═╝░░╚═╝╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░╚════╝░╚═════╝░
''')
    print('--------------------------------------------------------------------------------')

# --- Funções Auxiliares (Manipulação de Listas e Arquivos) ---
def gerar_lista_aleatoria(tamanho):
    """
    Gera uma lista de números inteiros aleatórios.
    O intervalo dos números vai de 0 até o tamanho da lista.
    """
    return [random.randint(0, tamanho) for i in range(tamanho)]

def ler_lista_de_arquivo(nome_arquivo):
    """
    Lê uma lista de números a partir de um arquivo de texto,
    onde cada número está em uma linha.
    """
    try:
        with open(nome_arquivo, 'r') as f:
            return [int(line.strip()) for line in f]
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except ValueError:
        print(f"Erro: O arquivo '{nome_arquivo}' contém linhas que não são números inteiros.")
        return None

def salvar_lista_em_arquivo(lista, nome_arquivo):
    """
    Salva uma lista de números em um arquivo de texto,
    com cada número em uma nova linha.
    """
    with open(nome_arquivo, 'w') as f:
        for item in lista:
            f.write(f"{item}\n")

# --- Implementação dos Algoritmos de Ordenação ---

# 1. Bubble Sort - O(n^2)
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break # Otimização: se não houve trocas, a lista já está ordenada
    return lista

# 2. Selection Sort - O(n^2)
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# 3. Insertion Sort - O(n^2)
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

# 4. Merge Sort - O(n log n)
def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
    return lista

# --- Funções de Simulação e Geração de Gráficos ---
def rodar_simulacao():
    """
    Executa a simulação completa, cronometrando cada algoritmo
    com diferentes tamanhos de lista e salvando os resultados.
    """
    algoritmos = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort
    }
    
    tamanhos_n = [1000, 5000, 10000, 25000, 50000]
    resultados = {}

    print("Iniciando simulação de desempenho. Isso pode levar vários minutos...")

    for nome_algoritmo, funcao_algoritmo in algoritmos.items():
        resultados[nome_algoritmo] = {}
        print(f"\n--- Testando {nome_algoritmo} ---")
        
        for n in tamanhos_n:
            tempos = []
            print(f"Testando com N = {n}...")

            for i in range(3): 
                lista_teste = gerar_lista_aleatoria(n)
                
                start_time = time.time()
                funcao_algoritmo(lista_teste.copy())
                end_time = time.time()
                
                tempo_execucao = end_time - start_time
                tempos.append(tempo_execucao)
                print(f"  Amostra {i+1}: {tempo_execucao:.3f} segundos")
            
            media_tempo = sum(tempos) / len(tempos)
            print(f"  Média de tempo: {media_tempo:.3f} segundos\n")
            
            resultados[nome_algoritmo][n] = {
                "amostras": tempos,
                "media": media_tempo
            }
            
    return resultados

def gerar_grafico(resultados):
    """
    Gera e salva um gráfico de linha comparando o tempo médio dos algoritmos.
    """
    print("Gerando gráfico comparativo...")
    
    # Prepara os dados para o gráfico
    for nome_algoritmo, dados_n in resultados.items():
        x_valores = sorted(dados_n.keys())
        y_valores = [dados_n[n]['media'] for n in x_valores]
        plt.plot(x_valores, y_valores, marker='o', linestyle='-', label=nome_algoritmo)

    # Configurações do Gráfico
    plt.title('Comparação de Desempenho de Algoritmos de Ordenação')
    plt.xlabel('Tamanho da Lista (N)')
    plt.ylabel('Tempo Médio de Execução (segundos)')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.xscale('log')
    
    # Salva o gráfico em um arquivo
    nome_arquivo_grafico = 'grafico_desempenho.png'
    plt.savefig(nome_arquivo_grafico)
    print(f"\nGráfico comparativo salvo como '{nome_arquivo_grafico}'")
    plt.show() # Fazer o gráfico aparecer no terminal

# --- Função Principal (Menu) ---
def main():
    """
    Função principal que exibe o menu e controla o fluxo do programa.
    """   
    while True:
        titulo()
        print("Menu de Opções:")
        print(f"\n1. Ordenar lista de um arquivo")
        print("2. Rodar simulação completa e gerar relatório")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            try:
                arquivo_entrada = input("Digite o nome do arquivo de entrada (ex: entrada.txt): ")
                arquivo_saida = input("Digite o nome do arquivo de saída (ex: saida.txt): ")
                
                print("\nAlgoritmos:")
                print("  1 - Bubble Sort")
                print("  2 - Selection Sort")
                print("  3 - Insertion Sort")
                print("  4 - Merge Sort")
                alg_escolha = input("Escolha o algoritmo (1-4): ")
                
                algoritmos_map = {
                    '1': ("Bubble Sort", bubble_sort),
                    '2': ("Selection Sort", selection_sort),
                    '3': ("Insertion Sort", insertion_sort),
                    '4': ("Merge Sort", merge_sort),
                }
                
                if alg_escolha not in algoritmos_map:
                    print("Opção de algoritmo inválida.")
                    continue
                
                nome_alg, func_alg = algoritmos_map[alg_escolha]
                
                lista_desordenada = ler_lista_de_arquivo(arquivo_entrada)
                if lista_desordenada is not None:
                    print(f"\nOrdenando {len(lista_desordenada)} itens com {nome_alg}...")
                    start_time = time.time()
                    lista_ordenada = func_alg(lista_desordenada)
                    end_time = time.time()
                    
                    salvar_lista_em_arquivo(lista_ordenada, arquivo_saida)
                    print(f"Lista ordenada salva em '{arquivo_saida}'.")
                    print(f"Tempo de execução: {end_time - start_time:.4f} segundos.")

            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")

        elif escolha == '2':
            resultados_simulacao = rodar_simulacao()
            gerar_grafico(resultados_simulacao)
            print("\nSimulação concluída!")
            
        elif escolha == '3':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Programa Principal
if __name__ == "__main__":
    main()