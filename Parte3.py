# =============================================================================
# DFS - Inspecao de Rede Florestal (25 vertices)
# =============================================================================

def dfs_floresta(grafo, inicio):
    """
    Executa DFS recursivo a partir do vertice 'inicio',
    visitando vizinhos por ordem crescente.
    Retorna a lista com a ordem de visita.
    """
    visitados = []

    def dfs_recursivo(vertice):
        visitados.append(vertice)
        vizinhos = sorted(grafo.get(vertice, []), key=lambda x: int(x[1:]))
        for vizinho in vizinhos:
            if vizinho not in visitados:
                dfs_recursivo(vizinho)

    dfs_recursivo(inicio)
    return visitados


# =============================================================================
# Dados: Todos os trilhos (arestas) do enunciado
# =============================================================================

trilhos = [
    ("P1", "P2"), ("P1", "P3"),
    ("P2", "P4"), ("P2", "P5"),
    ("P3", "P6"), ("P3", "P7"),
    ("P4", "P8"),
    ("P5", "P9"), ("P5", "P10"),
    ("P6", "P10"),
    ("P7", "P11"), ("P7", "P12"),
    ("P8", "P12"),
    ("P9", "P13"), ("P9", "P14"),
    ("P10", "P14"),
    ("P11", "P15"), ("P11", "P16"),
    ("P12", "P16"),
    ("P13", "P17"), ("P13", "P18"),
    ("P14", "P18"),
    ("P15", "P19"), ("P15", "P20"),
    ("P16", "P20"),
    ("P17", "P21"), ("P17", "P22"),
    ("P18", "P22"),
    ("P19", "P23"), ("P19", "P24"),
    ("P20", "P24"),
    ("P21", "P25"), ("P21", "P23"),
]

# Construir grafo (lista de adjacencia)
grafo_dfs = {}
for u, v in trilhos:
    grafo_dfs.setdefault(u, []).append(v)
    grafo_dfs.setdefault(v, []).append(u)


# =============================================================================
# Programa Principal
# =============================================================================

if __name__ == "__main__":

    # --- Tarefa 1 e 2: Executar DFS e indicar ordem de visita ---
    print("=" * 60)
    print("  TAREFA 1 e 2: DFS a partir de P1 (ordem crescente)")
    print("=" * 60)

    ordem = dfs_floresta(grafo_dfs, "P1")

    print("  Ordem de visita:")
    for i, vertice in enumerate(ordem):
        print(f"    {i + 1:2d}. {vertice}")

    print(f"\n  Total de vertices visitados: {len(ordem)} de 25")
    print("=" * 60)

    # --- Tarefa 3: Verificar se o grafo e conexo ---
    print("\n" + "=" * 60)
    print("  TAREFA 3: Verificacao de conexidade")
    print("=" * 60)

    is_conexo = len(ordem) == 25

    if is_conexo:
        print("  O grafo E CONEXO.")
        print("  Todos os 25 pontos de vigilancia foram visitados.")
        print("  Existe caminho entre quaisquer dois pontos.")
    else:
        print(f"  O grafo NAO E CONEXO.")
        print(f"  Apenas {len(ordem)} de 25 pontos foram alcancados.")
        todos = set(f"P{i}" for i in range(1, 26))
        nao_visitados = sorted(todos - set(ordem), key=lambda x: int(x[1:]))
        print(f"  Pontos nao alcancados: {', '.join(nao_visitados)}")

    print("=" * 60)