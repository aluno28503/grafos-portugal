# Trabalho Final (Parte I) — Algoritmos em Grafos

Este repositório contém as implementações em Python para a Parte I do Trabalho Final, focada na aplicação de algoritmos em grafos a contextos reais.

## Autores

- **Rodrigo Andrade** — aluno28503
- **Eric Cardoso** — aluno20518

## Ficheiros e Algoritmos

O projeto está dividido em quatro partes, cada uma abordando um cenário prático diferente:

### [Parte 1: Kruskal e Prim](Parte1.py)
**Contexto:** Planeamento da expansão de uma rede metropolitana de elétricos (20 estações).
**Objetivo:** Determinar a Árvore Geradora Mínima (AGM) para minimizar o custo das ligações.
**Implementação:** Ambos os algoritmos (Kruskal com Union-Find e Prim com Min-Heap) encontram a AGM ótima com custo total de 134 unidades.

### [Parte 2: BFS (Pesquisa em Largura)](Parte2.py)
**Contexto:** Sistema de navegação de ambulâncias numa rede de ruas (30 cruzamentos).
**Objetivo:** Determinar a distância mínima (em número de ruas) e o caminho mais curto entre a base (A1) e o destino (A30).
**Implementação:** O algoritmo BFS encontra o caminho mais curto de 6 ruas e identifica todos os vértices a uma distância máxima de 4 ruas da base.

### [Parte 3: DFS (Pesquisa em Profundidade)](Parte3.py)
**Contexto:** Inspeção de uma rede de trilhos florestais com 25 pontos de vigilância.
**Objetivo:** Percorrer os trilhos a partir do ponto P1 e verificar se a rede (grafo) é conexa.
**Implementação:** O DFS explora o grafo em profundidade (visitando vizinhos por ordem crescente), confirmando que todos os 25 pontos são alcançáveis (grafo conexo).

### [Parte 4: Algoritmo de Huffman](Parte4.py)
**Contexto:** Compressão de logs de servidores da empresa, onde mensagens como INFO, OK, WARN, etc., se repetem com frequências variadas.
**Objetivo:** Criar códigos binários prefixos ótimos para reduzir o tamanho dos ficheiros de log.
**Implementação:** Constrói a árvore de Huffman usando uma *min-heap*. Consegue reduzir o tamanho da codificação em cerca de 26,7% (de 150 000 bits para 110 000 bits) comparado com uma codificação de tamanho fixo.

## Como Executar

Cada ficheiro pode ser executado de forma independente:

```bash
python Parte1.py
python Parte2.py
python Parte3.py
python Parte4.py
```
