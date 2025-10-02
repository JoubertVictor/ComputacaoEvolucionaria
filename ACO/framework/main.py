import numpy as np
import pyants
from explicito.MatrizCusto import MatrizCusto

def main():

   
    matriz = MatrizCusto("DadosAtividadesACO.xlsx")
    matriz.inicializar_matriz_custo()

    
    def distancia(a, b):
        return matriz.matriz_custo[a][b]

    #
    num_cidades = matriz.num_cidades

    
    world = pyants.World(range(num_cidades), distancia)

    
    solver = pyants.Solver(
        ant_count=5,       
        alpha=1,         
        beta=5,            
        rho=0.5,           
        q=1,              
        limit=10           
    )

    
    best_path = solver.solve(world)

    
    print("Melhor rota encontrada:", best_path.tour)
    print("Custo da melhor rota:", best_path.distance)


if __name__ == "__main__":
    main()
