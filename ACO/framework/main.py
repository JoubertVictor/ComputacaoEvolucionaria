import numpy as np
from ant_colony_optimization import AntColony
from explicito.MatrizCusto import MatrizCusto

def main():

   
    matriz = MatrizCusto("DadosAtividadesACO.xlsx")
    matriz.inicializar_matriz_custo()

    
    def distancia(a, b):
        return matriz.matriz_custo[a][b]

    #
    num_cidades = matriz.num_cidades

    
    # Create a distance matrix from our cost matrix
    distances = np.array([[distancia(i, j) for j in range(num_cidades)] for i in range(num_cidades)])
    
    # Create AntColony instance
    colony = AntColony(distances, 
                      n_ants=5,
                      n_best=2,
                      n_iterations=10,
                      decay=0.5,
                      alpha=1,
                      beta=5)
    
    # Find the best path
    best_path = colony.run()
    
    print("Melhor rota encontrada:", best_path)
    print("Custo da melhor rota:", sum(distances[best_path[i]][best_path[i+1]] for i in range(len(best_path)-1)))


if __name__ == "__main__":
    main()
