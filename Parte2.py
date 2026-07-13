from collections import deque


# =============================================================================
# BFS - Sistema de Navegacao de Ambulancias (30 vertices)
# =============================================================================

def bfs_ambulancias(grafo, inicio, destino):
    """
    Executa BFS a partir do vertice 'inicio'.
    Retorna: niveis (distancias), caminho minimo ate 'destino',
             arvore BFS, e vertices a distancia <= 4.
    """
    fila = deque([(inicio, [inicio])])
    visitados = set([inicio])
    niveis = {inicio: 0}
    arvore_bfs = {inicio: None}  # pai de cada vertice na arvore BFS
    caminho_final = None

    while fila:
        vertice, caminho = fila.popleft()

        for vizinho in sorted(grafo.get(vertice, []), key=lambda x: int(x[1:])):
            if vizinho not in visitados:
                visitados.add(vizinho)
                niveis[vizinho] = niveis[vertice] + 1
                arvore_bfs[vizinho] = vertice
                fila.append((vizinho, caminho + [vizinho]))

                if vizinho == destino and caminho_final is None:
                    caminho_final = caminho + [vizinho]

    # Filtrar os vertices a uma distancia <= 4
    distancia_4 = sorted(
        [v for v, dist in niveis.items() if dist <= 4],
        key=lambda x: int(x[1:])
    )

    return niveis, caminho_final, distancia_4, arvore_bfs


# =============================================================================
# Dados: Todas as ruas (arestas) do enunciado
# =============================================================================

ruas = [
    ("A1", "A5"), ("A1", "A8"), ("A1", "A12"),
    ("A2", "A5"), ("A2", "A6"),
    ("A3", "A6"), ("A3", "A7"), ("A3", "A10"),
    ("A4", "A8"), ("A4", "A9"),
    ("A5", "A10"),
    ("A6", "A11"),
    ("A7", "A12"), ("A7", "A14"),
    ("A8", "A13"),
    ("A9", "A14"),
    ("A10", "A15"), ("A10", "A16"),
    ("A11", "A16"),
    ("A12", "A17"), ("A12", "A18"),
    ("A13", "A18"),
    ("A14", "A19"), ("A14", "A20"),
    ("A15", "A20"),
    ("A16", "A21"),
    ("A17", "A22"), ("A17", "A23"),
    ("A18", "A23"),
    ("A19", "A24"), ("A19", "A25"),
    ("A20", "A25"),
    ("A21", "A26"),
    ("A22", "A27"), ("A22", "A28"),
    ("A23", "A28"),
    ("A24", "A29"), ("A24", "A30"),
    ("A25", "A30"),
]

# Construir grafo (lista de adjacencia)
grafo_bfs = {}
for u, v in ruas:
    grafo_bfs.setdefault(u, []).append(v)
    grafo_bfs.setdefault(v, []).append(u)


# =============================================================================
# Programa Principal
# =============================================================================

if __name__ == "__main__":

    niveis, caminho, dist_4, arvore = bfs_ambulancias(grafo_bfs, "A1", "A30")

    # --- Tarefa 1: Distancia minima entre A1 e A30 ---
    print("=" * 60)
    print("  TAREFA 1: Distancia minima (numero de ruas) A1 -> A30")
    print("=" * 60)
    if "A30" in niveis:
        print(f"  Distancia minima: {niveis['A30']} ruas")
    else:
        print("  A30 nao e alcancavel a partir de A1!")
    print("=" * 60)

    # --- Tarefa 2: Arvore BFS por niveis ---
    print("\n" + "=" * 60)
    print("  TAREFA 2: Arvore BFS por niveis (a partir de A1)")
    print("=" * 60)

    nivel_max = max(niveis.values()) if niveis else 0
    for nivel in range(nivel_max + 1):
        vertices_nivel = sorted(
            [v for v, d in niveis.items() if d == nivel],
            key=lambda x: int(x[1:])
        )
        print(f"  Nivel {nivel}: {', '.join(vertices_nivel)}")

    print("=" * 60)

    # --- Tarefa 3: Caminho minimo entre A1 e A30 ---
    print("\n" + "=" * 60)
    print("  TAREFA 3: Caminho minimo em numero de ruas (A1 -> A30)")
    print("=" * 60)
    if caminho:
        print(f"  Caminho: {' -> '.join(caminho)}")
        print(f"  Numero de ruas: {len(caminho) - 1}")
    else:
        print("  Nao foi encontrado caminho!")
    print("=" * 60)

    # --- Tarefa 4: Vertices a distancia <= 4 de A1 ---
    print("\n" + "=" * 60)
    print("  TAREFA 4: Vertices a distancia <= 4 de A1")
    print("=" * 60)
    print(f"  Total: {len(dist_4)} vertices")
    print(f"  Vertices: {', '.join(dist_4)}")
    print("=" * 60)