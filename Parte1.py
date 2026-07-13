import heapq
import networkx as nx
import matplotlib.pyplot as plt
import os

# =============================================================================
# Estrutura Union-Find (para Kruskal)
# =============================================================================

class UnionFind:
    def __init__(self, vertices):
        self.pai = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def encontrar(self, item):
        if self.pai[item] == item:
            return item
        self.pai[item] = self.encontrar(self.pai[item])
        return self.pai[item]

    def unir(self, x, y):
        raiz_x = self.encontrar(x)
        raiz_y = self.encontrar(y)

        if raiz_x != raiz_y:
            if self.rank[raiz_x] < self.rank[raiz_y]:
                self.pai[raiz_x] = raiz_y
            elif self.rank[raiz_x] > self.rank[raiz_y]:
                self.pai[raiz_y] = raiz_x
            else:
                self.pai[raiz_y] = raiz_x
                self.rank[raiz_x] += 1


# =============================================================================
# Algoritmo de Kruskal
# =============================================================================

def kruskal(vertices, arestas):
    agm = []
    custo_total = 0
    uf = UnionFind(vertices)

    arestas_ordenadas = sorted(arestas, key=lambda a: a[2])

    for origem, destino, custo in arestas_ordenadas:
        if uf.encontrar(origem) != uf.encontrar(destino):
            uf.unir(origem, destino)
            agm.append((origem, destino, custo))
            custo_total += custo

    return agm, custo_total


# =============================================================================
# Algoritmo de Prim
# =============================================================================

def prim(vertices, arestas, inicio="S1"):
    # Construir lista de adjacencia
    adj = {v: [] for v in vertices}
    for u, v, custo in arestas:
        adj[u].append((custo, v))
        adj[v].append((custo, u))

    visitados = set()
    agm = []
    custo_total = 0

    # Min-heap: (custo, vertice_destino, vertice_origem)
    heap = [(0, inicio, None)]

    while heap and len(visitados) < len(vertices):
        custo, vertice, origem = heapq.heappop(heap)

        if vertice in visitados:
            continue

        visitados.add(vertice)

        if origem is not None:
            agm.append((origem, vertice, custo))
            custo_total += custo

        for peso, vizinho in adj[vertice]:
            if vizinho not in visitados:
                heapq.heappush(heap, (peso, vizinho, vertice))

    return agm, custo_total


# =============================================================================
# Visualizacao do Grafo
# =============================================================================

def desenhar_grafo_agm(estacoes, ligacoes, agm_arestas, titulo, nome_ficheiro):
    G = nx.Graph()
    G.add_nodes_from(estacoes)
    for u, v, c in ligacoes:
        G.add_edge(u, v, weight=c)
    
    # Layout circular e bom para grafos abstratos pequenos
    pos = nx.circular_layout(G)
    plt.figure(figsize=(10, 8))
    
    # Desenhar arestas normais a cinzento
    nx.draw_networkx_edges(G, pos, alpha=0.3, edge_color='gray')
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=600, edgecolors='black')
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
    
    # Desenhar arestas da AGM a vermelho
    agm_edges = [(u, v) for u, v, c in agm_arestas]
    nx.draw_networkx_edges(G, pos, edgelist=agm_edges, width=3.0, edge_color='red')
    
    # Adicionar custos nas arestas
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    
    plt.title(titulo, fontsize=14, pad=20)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(nome_ficheiro, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  Imagem gravada: {nome_ficheiro}")


# =============================================================================
# Dados: Estacoes e Ligacoes
# =============================================================================

estacoes = [f"S{i}" for i in range(1, 21)]

ligacoes = [
    ("S1", "S2", 8), ("S1", "S3", 12), ("S1", "S4", 15),
    ("S2", "S5", 7), ("S2", "S8", 10),
    ("S3", "S6", 9), ("S3", "S7", 14), ("S3", "S9", 16),
    ("S4", "S11", 6), ("S4", "S10", 11), ("S4", "S8", 10),
    ("S5", "S9", 13), ("S5", "S11", 9),
    ("S6", "S10", 14), ("S6", "S12", 10),
    ("S7", "S12", 8), ("S7", "S15", 11),
    ("S8", "S9", 5), ("S8", "S14", 12),
    ("S9", "S13", 9),
    ("S10", "S13", 7), ("S10", "S20", 18),
    ("S11", "S14", 4),
    ("S12", "S15", 6),
    ("S13", "S16", 5),
    ("S14", "S17", 8),
    ("S15", "S18", 7),
    ("S16", "S18", 6),
    ("S17", "S19", 10),
    ("S18", "S19", 4),
    ("S19", "S20", 6)
]


# =============================================================================
# Programa Principal
# =============================================================================

if __name__ == "__main__":

    # --- Mostrar a rede inicial ---
    print("=" * 60)
    print("  REDE INICIAL - Ligacoes possiveis")
    print("=" * 60)
    for u, v, c in ligacoes:
        print(f"  {u} <-> {v} | Custo: {c}")
    print(f"\n  Total de estacoes: {len(estacoes)}")
    print(f"  Total de ligacoes: {len(ligacoes)}")
    print("=" * 60)

    # --- Kruskal ---
    print("\n" + "=" * 60)
    print("  ALGORITMO DE KRUSKAL - Arvore Geradora Minima (AGM)")
    print("=" * 60)

    agm_kruskal, custo_kruskal = kruskal(estacoes, ligacoes)

    for ligacao in agm_kruskal:
        print(f"  {ligacao[0]} <-> {ligacao[1]} | Custo: {ligacao[2]}")

    print(f"\n  Numero de arestas na AGM: {len(agm_kruskal)}")
    print(f"  Custo Total Minimo (Kruskal): {custo_kruskal} unidades")
    
    # Gerar imagem da AGM do Kruskal
    desenhar_grafo_agm(estacoes, ligacoes, agm_kruskal, 
                       "Árvore Geradora Mínima - Kruskal\n(A vermelho)", 
                       "parte1_kruskal.png")
    print("=" * 60)

    # --- Prim ---
    print("\n" + "=" * 60)
    print("  ALGORITMO DE PRIM - Arvore Geradora Minima (AGM)")
    print("  (a partir de S1 - Estacao Central)")
    print("=" * 60)

    agm_prim, custo_prim = prim(estacoes, ligacoes, inicio="S1")

    for ligacao in agm_prim:
        print(f"  {ligacao[0]} <-> {ligacao[1]} | Custo: {ligacao[2]}")

    print(f"\n  Numero de arestas na AGM: {len(agm_prim)}")
    print(f"  Custo Total Minimo (Prim): {custo_prim} unidades")
    
    # Gerar imagem da AGM do Prim
    desenhar_grafo_agm(estacoes, ligacoes, agm_prim, 
                       "Árvore Geradora Mínima - Prim\n(A vermelho)", 
                       "parte1_prim.png")
    print("=" * 60)

    # --- Comparacao ---
    print("\n" + "=" * 60)
    print("  COMPARACAO")
    print("=" * 60)
    print(f"  Custo Kruskal: {custo_kruskal} unidades")
    print(f"  Custo Prim:    {custo_prim} unidades")
    if custo_kruskal == custo_prim:
        print("  Os dois algoritmos obtiveram o mesmo custo minimo.")
    print("=" * 60)