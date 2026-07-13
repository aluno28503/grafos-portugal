import heapq
import networkx as nx
import matplotlib.pyplot as plt


# =============================================================================
# Algoritmo de Huffman - Compressao de Logs de Servidores
# =============================================================================

class NoHuffman:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.esq = None
        self.dir = None

    def __lt__(self, outro):
        return self.freq < outro.freq


def calcular_huffman(frequencias):
    # Criar min-heap com todos os simbolos
    heap = [NoHuffman(sym, freq) for sym, freq in frequencias.items()]
    heapq.heapify(heap)

    print("=" * 60)
    print("  CONSTRUCAO DA ARVORE DE HUFFMAN")
    print("=" * 60)
    passo = 0

    # Combinar os dois menores ate restar um
    while len(heap) > 1:
        no1 = heapq.heappop(heap)
        no2 = heapq.heappop(heap)

        combinado = NoHuffman(None, no1.freq + no2.freq)
        combinado.esq = no1
        combinado.dir = no2
        heapq.heappush(heap, combinado)

        passo += 1
        nome1 = no1.char if no1.char else f"No({no1.freq})"
        nome2 = no2.char if no2.char else f"No({no2.freq})"
        print(f"  Passo {passo}: Combinar {nome1}({no1.freq}) + {nome2}({no2.freq}) = No({combinado.freq})")

    print("=" * 60)

    # Gerar codigos percorrendo a arvore
    raiz = heap[0]
    codigos = {}

    def gerar_codigos(no, codigo_atual):
        if no is None:
            return
        if no.char is not None:
            codigos[no.char] = codigo_atual
        gerar_codigos(no.esq, codigo_atual + "0")
        gerar_codigos(no.dir, codigo_atual + "1")

    gerar_codigos(raiz, "")
    return codigos, raiz


def imprimir_arvore(no, prefixo="", is_esq=True, is_raiz=True):
    """Imprime a arvore de Huffman de forma visual."""
    if no is None:
        return

    if is_raiz:
        etiqueta = f"[RAIZ: {no.freq}]"
        print(f"  {etiqueta}")
    else:
        conector = "|-- 0: " if is_esq else "`-- 1: "
        if no.char:
            etiqueta = f"{no.char} ({no.freq})"
        else:
            etiqueta = f"No ({no.freq})"
        print(f"  {prefixo}{conector}{etiqueta}")

    novo_prefixo = prefixo + ("|   " if is_esq and not is_raiz else "    ")

    if no.esq or no.dir:
        imprimir_arvore(no.esq, novo_prefixo if not is_raiz else "  ", True, False)
        imprimir_arvore(no.dir, novo_prefixo if not is_raiz else "  ", False, False)


# =============================================================================
# Visualizacao da Arvore
# =============================================================================

def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parsed=None):
    if pos is None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    
    if parsed is None:
        parsed = set()
    parsed.add(root)
    
    neighbors = list(G.successors(root))
    
    if len(neighbors) != 0:
        dx = width / 2 
        nextx = xcenter - width/2 - dx/2
        for neighbor in neighbors:
            nextx += dx
            pos = _hierarchy_pos(G, neighbor, width=dx, vert_gap=vert_gap, 
                                vert_loc=vert_loc-vert_gap, xcenter=nextx,
                                pos=pos, parsed=parsed)
    return pos


def desenhar_huffman(raiz, nome_ficheiro):
    G = nx.DiGraph()
    labels = {}
    edge_labels = {}
    node_colors = []
    
    # Percorrer a arvore para construir o grafo do NetworkX
    def traverse(no, idx):
        node_id = f"{idx}_{no.char}_{no.freq}"
        if no.char:
            labels[node_id] = f"{no.char}\n{no.freq}"
        else:
            labels[node_id] = f"{no.freq}"
            
        if no.esq:
            esq_id = traverse(no.esq, idx*2)
            G.add_edge(node_id, esq_id)
            edge_labels[(node_id, esq_id)] = '0'
        if no.dir:
            dir_id = traverse(no.dir, idx*2+1)
            G.add_edge(node_id, dir_id)
            edge_labels[(node_id, dir_id)] = '1'
            
        return node_id

    root_id = traverse(raiz, 1)
    
    # Colorir as folhas de cor diferente dos nos internos
    for n in G.nodes():
        if n in labels and '\n' in labels[n]:  # e uma folha
            node_colors.append('lightgreen')
        else:
            node_colors.append('lightblue')
            
    pos = _hierarchy_pos(G, root=root_id, width=1.5, vert_gap=0.3)
    
    plt.figure(figsize=(12, 8))
    
    # Desenhar grafo
    nx.draw(G, pos, with_labels=False, node_color=node_colors, node_size=2000, 
            edgecolors='gray', arrows=False)
            
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_color='red')
    
    plt.title("Árvore de Huffman - Compressão de Logs", fontsize=16, pad=20)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(nome_ficheiro, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  Imagem gravada: {nome_ficheiro}")


# =============================================================================
# Dados: Frequencias dos simbolos
# =============================================================================

frequencias = {
    "INFO": 22000,
    "OK": 12000,
    "WARN": 6000,
    "ERROR": 4000,
    "RETRY": 3000,
    "FAILED": 3000
}


# =============================================================================
# Programa Principal
# =============================================================================

if __name__ == "__main__":

    # --- Tarefa 1: Construir arvore e mostra-la ---
    codigos_gerados, raiz = calcular_huffman(frequencias)

    print("\n" + "=" * 60)
    print("  ARVORE DE HUFFMAN")
    print("=" * 60)
    imprimir_arvore(raiz)
    
    # Gerar a imagem graficamente
    desenhar_huffman(raiz, "parte4_huffman.png")
    
    print("=" * 60)

    # --- Tarefa 2: Mostrar codigos ---
    print("\n" + "=" * 60)
    print("  CODIGOS DE HUFFMAN")
    print("=" * 60)
    print(f"  {'Simbolo':<10} {'Frequencia':>12} {'Codigo':<10} {'Bits':>5}")
    print(f"  {'-' * 42}")

    # Ordenar por comprimento do codigo (mais curto primeiro)
    for sym, cod in sorted(codigos_gerados.items(), key=lambda x: len(x[1])):
        print(f"  {sym:<10} {frequencias[sym]:>12,} {cod:<10} {len(cod):>5}")

    print("=" * 60)

    # --- Tarefa 3: Comprimento total ---
    print("\n" + "=" * 60)
    print("  COMPRIMENTO TOTAL DE CODIFICACAO")
    print("=" * 60)

    tamanho_total = 0
    for sym, cod in codigos_gerados.items():
        bits_simbolo = frequencias[sym] * len(cod)
        tamanho_total += bits_simbolo
        print(f"  {sym:<10}: {frequencias[sym]:>6} x {len(cod)} bits = {bits_simbolo:>10,} bits")

    print(f"  {'-' * 45}")
    print(f"  TOTAL: {tamanho_total:>10,} bits")

    # Comparacao com codigo fixo
    num_simbolos = len(frequencias)
    import math
    bits_fixos = math.ceil(math.log2(num_simbolos))
    total_linhas = sum(frequencias.values())
    tamanho_fixo = total_linhas * bits_fixos

    print(f"\n  Sem Huffman (codigo fixo de {bits_fixos} bits): {tamanho_fixo:>10,} bits")
    print(f"  Com Huffman:                          {tamanho_total:>10,} bits")
    poupanca = ((tamanho_fixo - tamanho_total) / tamanho_fixo) * 100
    print(f"  Poupanca: {poupanca:.1f}%")
    print("=" * 60)