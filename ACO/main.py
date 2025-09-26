from MatrizCusto import MatrizCusto
from formiga import Formiga
import random
import numpy as np

def calcula_proxima_cidade(formiga, matriz):
    i = formiga.cidade_atual
    nao_visitadas = [c for c in range(matriz.num_cidades) if c not in formiga.tabu]

    if not nao_visitadas:
        return None

   
    denominador = 0
   # print(f"DEBUG: matriz.matriz_feromonio type: {type(matriz.matriz_feromonio)}")
   #print(f"DEBUG: matriz.inverso_matriz_custo type: {type(matriz.inverso_matriz_custo)}")
   # print(f"DEBUG: i={i}, nao_visitadas={nao_visitadas}")
    print(f"DEBUG: matriz.matriz_feromonio={matriz.matriz_feromonio}")
   # print(f"DEBUG: matriz.inverso_matriz_custo={matriz.inverso_matriz_custo}")
    for k in nao_visitadas:
        denominador += (matriz.matriz_feromonio[i][k] ** matriz.alpha) * \
                       (matriz.inverso_matriz_custo[i][k] ** matriz.beta)

    if denominador == 0:
        return random.choice(nao_visitadas)

  
    probabilidades = []
    for j in nao_visitadas:
        numerador = (matriz.matriz_feromonio[i][j] ** matriz.alpha) * \
                    (matriz.inverso_matriz_custo[i][j] ** matriz.beta)
        probabilidades.append(numerador / denominador)

    
    proxima_cidade = random.choices(nao_visitadas, weights=probabilidades, k=1)[0]
    return proxima_cidade



def calcula_custo_total(formiga, matriz):
    custo_total = 0
    for i in range(len(formiga.tabu) - 1):
        cidade_atual = formiga.tabu[i]
        proxima_cidade = formiga.tabu[i + 1]
        custo_total += matriz.matriz_custo[cidade_atual][proxima_cidade]
    formiga.custo_total = custo_total
    return custo_total



def main():
    matriz = MatrizCusto("DadosAtividadesACO.xlsx")
    matriz.inicializar_matriz_custo()
    matriz.inicializar_inverso_matriz_custo()
    matriz.inicializar_matriz_feromonio()

    num_formigas = 5
    max_iteracoes = 15

    melhor_custo = float('inf')
    melhor_rota = []

    formigas = [Formiga(matriz.num_cidades) for _ in range(num_formigas)]
    for f in formigas:
        f.inicializar()

    for t in range(max_iteracoes):
        
        for formiga in formigas:
            cidade_inicial = random.randint(0, matriz.num_cidades - 1)
            formiga.reset(cidade_inicial)

           
            while len(formiga.tabu) < matriz.num_cidades:
                    proxima = calcula_proxima_cidade(formiga, matriz)
                    if proxima is not None:
                        formiga.tabu.append(proxima)
                        formiga.cidade_atual = proxima
                    else:
                        break

            # Fecha o ciclo retornando à cidade inicial
            formiga.tabu.append(formiga.tabu[0])

          
            calcula_custo_total(formiga, matriz)

           
            if formiga.custo_total < melhor_custo:
                melhor_custo = formiga.custo_total
                melhor_rota = formiga.tabu.copy()

       
        matriz.atualizar_matriz_feromonio(formigas)

        print(f"Iteração {t+1}: Melhor custo até agora = {melhor_custo}")

    print("\nMelhor rota encontrada:", melhor_rota)
    print("Custo da melhor rota:", melhor_custo)



if __name__ == "__main__":
    main()