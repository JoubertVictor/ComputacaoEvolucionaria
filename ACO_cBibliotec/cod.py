import pandas as pd
import matplotlib.pyplot as plt
from pants.solver import Solver
from pants.world import World

#Mudar aqui para o seu caminho
EXCEL_FILE = "/home/joubert/ComputacaoEvolucionaria/ACO_cBibliotec/DadosAtividadesACO.xlsx"

def ler_matriz_custo(file_name=EXCEL_FILE):
    df = pd.read_excel(file_name, sheet_name=0, header=None)
    matriz = df.iloc[14:19, 1:6].values.tolist()
    return matriz

def criar_world_da_matriz(matriz_custo):
    num_cidades = len(matriz_custo)
    nodes = list(range(num_cidades))

    def length_func(a, b):
        return float(matriz_custo[a][b])

    return World(nodes, length_func, name="TSP_from_excel")

def extrair_rota_e_custo(ant):
    if not ant or not ant.path:
        return [], float("inf")

    rota = [edge.start for edge in ant.path]
    rota.append(ant.path[-1].end)
    custo = ant.distance
    return rota, custo

def main():
    matriz = ler_matriz_custo(EXCEL_FILE)
    world = criar_world_da_matriz(matriz)

    iteracoes = 15
    custos = []
    melhor_ant = None

    for i in range(iteracoes):
        solver = Solver(
            alpha=0.5,
            beta=0.5,
            rho=0.1,
            Q=1.0,
            t0=0.01,
            limit=1,     # roda 1 iteração de cada vez
            ant_count=5,
            elite=0.0
        )

        ant = solver.solve(world)
        rota, custo = extrair_rota_e_custo(ant)
        custos.append(custo)
        melhor_ant = ant  # guarda o último melhor

    # Plotando evolução do custo
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(custos) + 1), custos, marker="o")
    plt.xlabel("Iteração")
    plt.ylabel("Custo da melhor rota")
    plt.title("Evolução do custo ao longo das iterações (ACO)")
    plt.grid(True)
    plt.show()

    rota, custo = extrair_rota_e_custo(melhor_ant)
    print("Melhor rota:", rota)
    print("Custo final:", custo)

if __name__ == "__main__":
    main()
