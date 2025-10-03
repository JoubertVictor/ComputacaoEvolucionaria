import os
import sys
import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from explicito.MatrizCusto import MatrizCusto
from ant_colony.graph import Graph, AntColony


def main():
    matriz = MatrizCusto("DadosAtividadesACO.xlsx")
    matriz.inicializar_matriz_custo()
    distances = np.array(matriz.matriz_custo)

    def distancia(a, b):
        return matriz.matriz_custo[a][b]

    num_cidades = matriz.num_cidades

    ant_count = 5
    alpha = 1
    beta = 5
    rho = 0.5
    q = 1
    limit = 10

    nodes = []
    n = distances.shape[0]
    for i in range(n):
        class _Node:
            def __init__(self, idx, dists):
                self.idx = idx
                self._d = dists

            def distance(self, other):
                return self._d[other.idx]

        nodes.append(_Node(i, distances[i].tolist()))

    graph = Graph(nodes, alpha=alpha, beta=beta, decay=rho, deposit=q)
    colony = AntColony(ant_count)
    colony.do_cycles(graph)
    best_path = getattr(colony, 'shortest_path', None) or getattr(colony, 'best', None)
    best_cost = getattr(colony, 'min_distance', None) or getattr(colony, 'best_distance', None)
    if best_path is not None and not isinstance(best_path, (list, tuple)):
        best_path = getattr(best_path, 'tour', None) or getattr(best_path, 'path', None) or best_path

    print('Melhor rota encontrada:', best_path)
    print('Custo da melhor rota:', best_cost)


if __name__ == "__main__":
    main()
