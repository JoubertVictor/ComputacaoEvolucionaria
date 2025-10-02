import random

class Formiga:
    def __init__(self, num_cidades=5):
        self.tabu = []            
        self.cidade_atual = 0      
        self.custo_total = 0       
        self.num_cidades = num_cidades

    def inicializar(self):
        self.cidade_atual = random.randint(0, self.num_cidades - 1)
        self.tabu = [self.cidade_atual]
        self.custo_total = 0

    def reset(self, cidade_inicial):
        self.cidade_atual = cidade_inicial
        self.tabu = [cidade_inicial]
        self.custo_total = 0
