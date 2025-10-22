'''
INTEGRANTES:
Henrique Martins - RM 563620
Henrique Teixeira - RM 563088

Titulo: Personalizado em ASCII ART no site FSymbols.
IMPORT TIME: Para saber o tempo de execução.
IMPORT RANDOM: Gerar lista aleatória de números.
IMPORT MATPLOTLIB: Para gerar gráficos.
IMPORT OS: Para limpar o terminal.
'''

# Importações
import random
import time
import matplotlib.pyplot as plt
import os 

# Funções para o estilizar o programa.
def titulo():
    print('-=≣ ------------------------------------------------------------------------ ≣=-')
    print('''

░█████╗░██╗░░░░░░██████╗░░█████╗░██████╗░██╗████████╗███╗░░░███╗░█████╗░░██████╗
██╔══██╗██║░░░░░██╔════╝░██╔══██╗██╔══██╗██║╚══██╔══╝████╗░████║██╔══██╗██╔════╝
███████║██║░░░░░██║░░██╗░██║░░██║██████╔╝██║░░░██║░░░██╔████╔██║██║░░██║╚█████╗░
██╔══██║██║░░░░░██║░░╚██╗██║░░██║██╔══██╗██║░░░██║░░░██║╚██╔╝██║██║░░██║░╚═══██╗
██║░░██║███████╗╚██████╔╝╚█████╔╝██║░░██║██║░░░██║░░░██║░╚═╝░██║╚█████╔╝██████╔╝
╚═╝░░╚═╝╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░╚════╝░╚═════╝░
''')
    print('-=≣ ------------------------------------------------------------------------ ≣=-')

def limpar_terminal():
    """Limpa o terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Funções para Manipulação de Listas e Arquivos
def gerar_lista(tam_lista):
    """
    Gera uma lista de números aleatórios de 0 até o tamanho da listq.
    """
    return [random.randint(0, tam_lista) for i in range(tam_lista)]

def ler_lista_arq(nome_arq):
    """
    Lê uma lista de números a partir de um arquivo de texto.
    """
    try:
        with open(nome_arq, 'r') as f:
            return [int(line.strip()) for line in f]
    except FileNotFoundError:
        print(f"[ERRO]: O arquivo '{nome_arq}' não foi encontrado.")
        return None
    except ValueError:
        print(f"[ERRO]: O arquivo '{nome_arq}' tem linhas que não são números.")
        return None

def salvar_lista_arq(lista, nome_arq):
    """
    Salva uma lista de números em um arquivo de texto.
    """
    with open(nome_arq, 'w') as f:
        for item in lista:
            f.write(f"{item}\n")

# Algoritmos de Ordenação
# Bubblee Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista

# Selection Sort
def selection_sort(lista):
    n = len(lista) 
    
    for i in range(n):
        indice_minimo = i 
        
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                    indice_minimo = j 
                    
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

# Insertion Sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

# Merge Sort
def merge_sort(lista):
    if len(lista) > 1:

        meio = len(lista) // 2  

        L = lista[:meio] 
        R = lista[meio:]  

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
    return lista


# Função para a Simulação
def simulacao():
    """
    Executa a simulação completa, com o tempo decada algoritmo.
    """
    algoritmos_ordenacao = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort
    }
    
    tamanhos_n = [1000, 5000, 10000, 25000, 50000]
    resultados = {}

    print("Começando a Simulação..")

    for nome_algoritmo in algoritmos_ordenacao:
        funcao_algoritmo = algoritmos_ordenacao[nome_algoritmo]
        resultados[nome_algoritmo] = {}
        print(f"\n-=≣ Testando o {nome_algoritmo} ≣=-")
        
        for n in tamanhos_n:
            tempos = []
            print(f"Testando com N = {n}...")

            for i in range(3): 
                lista_teste = gerar_lista(n)
                
                inicio_tempo = time.time()
                funcao_algoritmo(lista_teste) 
                fim_tempo = time.time()
                
                tempo_execucao = fim_tempo - inicio_tempo
                tempos.append(tempo_execucao)
                print(f"  Amostra {i+1}: {tempo_execucao:.3f} segundos")
            
            media_tempo = sum(tempos) / len(tempos)
            print(f"  Média de tempo: {media_tempo:.3f} segundos\n")
            
            resultados[nome_algoritmo][n] = {
                "amostras": tempos,
                "media": media_tempo
            }
            
    return resultados

# Função Para o Gráfico
def gerar_grafico(resultados):
    """
    Gera e salva um gráfico de linha comparando o tempo médio dos algoritmos.
    """
    print("Gerando gráfico...")
    
    for nome_algoritmo in resultados:
        dados_n = resultados[nome_algoritmo]
        
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
    
    # Salvar o gráfico em arquivo
    nome_arq_grafico = 'grafico.png'
    plt.savefig(nome_arq_grafico)
    print(f"\nGráfico salvo como '{nome_arq_grafico}'")
    plt.show() # Fazer o gráfico aparecer no terminal

# Programa Principal
def main():
    """
    Função principal que exibe o menu e controla o programa.
    """ 
    while True:
        limpar_terminal() 
        titulo()
        print("Menu de Opções:")
        print(f"\n1. Ordenar um Arquivo.")
        print("2. Simulação e Relatório.")
        print("3. Sair")
        
        escolha_usuario = input("Escolha uma opção: ")

        if escolha_usuario == '1':
            limpar_terminal()
            try:
                arquivo_entrada = input("Digite o nome do arquivo desordenado: ")
                arquivo_saida = input("Digite o nome do novo arquivo ordenado: ")
                
                print("\nAlgoritmos:")
                print("  1 - Bubble Sort")
                print("  2 - Selection Sort")
                print("  3 - Insertion Sort")
                print("  4 - Merge Sort")
                alg_escolha = input("Escolha o algoritmo (1-4): ")
                
                algoritmos_mapa = {
                    '1': ("Bubble Sort", bubble_sort),
                    '2': ("Selection Sort", selection_sort),
                    '3': ("Insertion Sort", insertion_sort),
                    '4': ("Merge Sort", merge_sort),
                }
                
                if alg_escolha not in algoritmos_mapa:
                    print("Opção de algoritmo inválida.")
                    continue
                
                nome_alg, func_alg = algoritmos_mapa[alg_escolha]
                
                lista_desordenada = ler_lista_arq(arquivo_entrada)
                if lista_desordenada is not None:
                    print(f"\nOrdenando {len(lista_desordenada)} itens com {nome_alg}...")
                    inicio_tempo = time.time()
                    lista_ordenada = func_alg(lista_desordenada) 
                    fim_tempo = time.time()
                    
                    salvar_lista_arq(lista_ordenada, arquivo_saida)
                    print(f"Lista ordenada salva em '{arquivo_saida}'.")
                    print(f"Tempo de execução: {fim_tempo - inicio_tempo:.3f} segundos.")

            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")

        elif escolha_usuario == '2':
            limpar_terminal()
            resultados_simulacao = simulacao()
            gerar_grafico(resultados_simulacao)
            print("\nSimulação concluída!")
            
        elif escolha_usuario == '3':
            limpar_terminal()
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

main()