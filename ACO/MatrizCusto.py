import pandas as pd

class MatrizCusto:
    def __init__(self, file_name="DadosAtividadesACO.xlsx"):
        self.file_name = file_name
        self.matriz_custo = []
        self.num_cidades = 5
        self.matriz_feromonio = []
        self.alpha = 0.5
        self.beta = 0.5
        self.inverso_matriz_custo = []

    def inicializar_matriz_custo(self):
        df = pd.read_excel(self.file_name, sheet_name=0, header=None)
       
        self.matriz_custo = df.iloc[14:19, 1:6].values.tolist()
        self.num_cidades = len(self.matriz_custo)
        return self.matriz_custo

    def inicializar_matriz_feromonio(self):
        df = pd.read_excel(self.file_name, sheet_name=0, header=None)
       
        self.matriz_feromonio = df.iloc[22:27, 1:6].values.tolist()
        return self.matriz_feromonio

    def inicializar_inverso_matriz_custo(self):
     
        df = pd.read_excel(self.file_name, sheet_name=0, header=None)

       
        matriz_custo = df.iloc[15:20, 7:12].values.tolist()

        self.inverso_matriz_custo = []

        for i, linha in enumerate(matriz_custo):
            nova_linha = []
            for j, valor in enumerate(linha):
           
                if pd.isna(valor):
                    nova_linha.append(0)
           
                elif valor == 0:
                    nova_linha.append(0)
                else:
                    nova_linha.append(valor)
            self.inverso_matriz_custo.append(nova_linha)

        return self.inverso_matriz_custo
    
    def inicializar_matrizes(self):
        self.inicializar_matriz_custo()
        self.inicializar_matriz_feromonio()
        self.inicializar_inverso_matriz_custo()

    def atualizar_matriz_feromonio(self, formigas, rho=0.1, Q=1.0):
       
        delta = [[0.0 for _ in range(self.num_cidades)] for _ in range(self.num_cidades)]
        for formiga in formigas:
            if formiga.custo_total > 0:
                for k in range(len(formiga.tabu) - 1):
                    i = formiga.tabu[k]
                    j = formiga.tabu[k + 1]
                    delta[i][j] += Q / formiga.custo_total

        for i in range(self.num_cidades):
            for j in range(self.num_cidades):
                self.matriz_feromonio[i][j] = (1 - rho) * self.matriz_feromonio[i][j] + delta[i][j]
        return self.matriz_feromonio
