# Análise de Desempenho de Algoritmos de Ordenação

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8-green?logo=matplotlib&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)

Um projeto desenvolvido em Python que realiza uma análise prática do desempenho de quatro algoritmos de ordenação fundamentais. A aplicação compara algoritmos de complexidade quadrática ($O(n^2)$) com um de complexidade log-linear ($O(n \log n)$), demonstrando visualmente o impacto da **Notação Big O** no tempo de execução real.

Este projeto foi criado para o Checkpoint de "Computational Thinking using Python" da FIAP, servindo como uma peça de portfólio que demonstra habilidades em análise de algoritmos, manipulação de dados e visualização de resultados com `matplotlib`.

---

## ✨ Funcionalidades Principais

* **Implementação de Algoritmos**: Código claro e comentado para **Bubble Sort**, **Selection Sort**, **Insertion Sort** e **Merge Sort**.
* **Simulação de Desempenho**: Executa testes cronometrados para cada algoritmo com diferentes volumes de dados (N = 1.000 a 50.000).
* **Análise Estatística**: Calcula a média de tempo de 3 amostras para cada teste, garantindo maior confiabilidade nos resultados.
* **Geração de Gráficos**: Cria e salva um gráfico de linha comparativo, plotando o **Tempo de Execução vs. Tamanho da Lista (N)**.
* **Manipulação de Arquivos**: Capaz de ler uma lista de números de um arquivo de entrada e salvar a lista ordenada em um arquivo de saída.
* **Interface de Linha de Comando (CLI)**: Um menu interativo guia o usuário para executar uma ordenação simples ou a simulação completa.

## 📸 Demonstração

O script principal opera através de um menu no terminal:

1.  O usuário pode escolher **ordenar um arquivo específico** ou **rodar a simulação completa**.
2.  Ao rodar a simulação, o progresso é exibido no console, mostrando os tempos de cada amostra e a média para cada algoritmo e tamanho de lista.
3.  Ao final, um arquivo de imagem `grafico_desempenho.png` é gerado no diretório do projeto, contendo o gráfico comparativo.

![Exemplo de Gráfico Gerado](https://i.imgur.com/link_para_seu_grafico.png) 
*(Dica: Após rodar o projeto, tire um print do gráfico, suba para um site como o [Imgur](https://imgur.com/) e substitua este link!)*

## 🛠️ Tecnologias e Ferramentas

* **Linguagem**: Python 3
* **Bibliotecas Principais**:
    * [Matplotlib](https://matplotlib.org/): A única dependência externa, utilizada para a criação de gráficos e visualizações de dados.
* **Módulos Nativos do Python**:
    * `time`: Para cronometrar o tempo de execução.
    * `random`: Para gerar listas de números aleatórios.
    * `sys`: Para interações básicas com o sistema.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o projeto em sua máquina local.

### **Pré-requisitos**

* **Python 3.6** ou superior.
* **PIP** (gerenciador de pacotes do Python) instalado.

### **Passos para Configuração**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/hrqmartins/python-sort-analysis.git](https://github.com/hrqmartins/python-sort-analysis.git)
    cd python-sort-analysis
    ```

2.  **Crie um ambiente virtual (Recomendado):**
    ```bash
    python -m venv venv
    # Ative o ambiente virtual
    # No Windows:
    venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    O projeto tem apenas uma dependência externa. Instale-a com o pip:
    ```bash
    pip install matplotlib
    ```

4.  **Execute a aplicação:**
    ```bash
    python analise_ordenacao.py
    ```

5.  **Siga as instruções do menu:**
    * Escolha a **opção 2** para rodar a simulação completa e gerar o gráfico.
    * Escolha a **opção 1** se quiser testar a ordenação de um arquivo de texto específico.

## 🏗️ Estrutura do Projeto

Por ser um script de análise focado, todo o código está contido em um único arquivo, `analise_ordenacao.py`, organizado em seções lógicas para clareza e manutenibilidade.

* **Funções Auxiliares**: Contém as funções `gerar_lista_aleatoria`, `ler_lista_de_arquivo` e `salvar_lista_em_arquivo`, responsáveis pela manipulação de dados e arquivos.
* **Implementação dos Algoritmos de Ordenação**: Cada algoritmo (`bubble_sort`, `selection_sort`, etc.) é implementado como uma função pura e independente.
* **Funções de Simulação e Gráficos**: A lógica para rodar os testes (`rodar_simulacao`) e para gerar o gráfico (`gerar_grafico`) está encapsulada aqui.
* **Função Principal (`main`)**: Controla o fluxo da aplicação, exibindo o menu e orquestrando as chamadas para as outras funções com base na entrada do usuário.

Essa estrutura, mesmo em um único arquivo, promove a separação de responsabilidades e facilita o entendimento do código.

---

_Este projeto foi desenvolvido com dedicação como parte do aprendizado contínuo em Análise e Desenvolvimento de Sistemas._