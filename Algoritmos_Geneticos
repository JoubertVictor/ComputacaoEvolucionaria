import random

"""Dados da Mochila"""

pesos = [350, 250, 160, 120, 200, 100, 120, 220, 40, 80, 100, 300, 180, 250, 220, 150, 280, 310, 120, 160, 110, 210]
valores = [300, 400, 450, 350, 250, 300, 200, 250, 150, 400, 350, 300, 450, 500, 350, 400, 200, 300, 250, 300, 150, 200]
capacidade = 3000
num_itens = len(pesos) 

"""Parametros """

tamanho_pop = 50         # tamanho da população
gen = 100       # número de gerações
taxa_crossover = 0.8 # probabilidade de aplicar crossover entre dois pais
taxa_mutacao = 0.05  # probabilidade de mutar cada gene (por bit)
torneio_k = 3        # tamanho do torneio para seleção
elitismo = 1         # quantos melhores preservamos diretamente (elitismo)

"""Funções"""

def criar_individuo():

    individuo = []
    for _ in range(num_itens):
        # rand < 0.5 => 1, else 0 
        if random.random() < 0.5:
            individuo.append(1)
        else:
            individuo.append(0)
    return individuo

def peso_total(individuo):
    
    total = 0
    for i in range(num_itens):
        if individuo[i] == 1:
            total += pesos[i]
    return total

def valor_total(individuo):

    total = 0
    for i in range(num_itens):
        if individuo[i] == 1:
            total += valores[i]
    return total

def fitness(individuo):

    p = peso_total(individuo)
    if p > capacidade:
        return 0
    return valor_total(individuo)

def selecao_torneio(populacao):
    
    melhor = None
    for _ in range(torneio_k):
        candidato = random.choice(populacao)   # seleciona um indivíduo aleatório
        if melhor is None or fitness(candidato) > fitness(melhor):
            melhor = candidato[:]  
    return melhor

def crossover_um_ponto(pai1, pai2):
    
    if random.random() < taxa_crossover:
        # escolhe ponto de corte entre 1 e num_itens-1 para evitar extremos
        ponto = random.randint(1, num_itens - 1)
        filho1 = pai1[:ponto] + pai2[ponto:]
        filho2 = pai2[:ponto] + pai1[ponto:]
        return filho1, filho2
    else:
        # retorna cópias dos pais (sem modifica-los)
        return pai1[:], pai2[:]

def mutacao(individuo):
    
    for i in range(num_itens):
        if random.random() < taxa_mutacao:
            if individuo[i] == 0:
                individuo[i] = 1
            else:
                individuo[i] = 0
    return individuo

"""Função"""

def algoritmo_genetico():
    # 1) Inicializa a população com indivíduos aleatórios
    populacao = []
    for _ in range(tamanho_pop):
        populacao.append(criar_individuo())

    # registra o melhor indivíduo encontrado e a geração onde foi encontrado
    melhor_individuo = populacao[0][:]
    melhor_fitness = fitness(melhor_individuo)
    geracao_melhor = 0

    # 2) Loop principal (uma iteração = uma geração)
    for g in range(1, gen + 1):
        # ordena/pop ou apenas encontra o melhor da geração atual
        # encontramos o melhor atual para aplicar elitismo e possivelmente atualizar global
        melhor_atual = populacao[0]
        for ind in populacao:
            if fitness(ind) > fitness(melhor_atual):
                melhor_atual = ind

        # atualiza melhor global se necessário
        if fitness(melhor_atual) > melhor_fitness:
            melhor_individuo = melhor_atual[:]    # copia
            melhor_fitness = fitness(melhor_individuo)
            geracao_melhor = g

        # 3) Cria nova população (aplicando elitismo)
        nova_pop = []
        # adiciona os 'elitismo' melhores indivíduos (aqui mantemos o melhor atual)
        # copiamos para evitar referências ao mesmo objeto
        for _ in range(elitismo):
            nova_pop.append(melhor_atual[:])

        # preenche o restante da nova população com reprodução
        while len(nova_pop) < tamanho_pop:
            # seleção de pais (cada seleção retorna uma cópia)
            pai1 = selecao_torneio(populacao)
            pai2 = selecao_torneio(populacao)

            # crossover
            filho1, filho2 = crossover_um_ponto(pai1, pai2)

            # mutação (modifica in-place)
            filho1 = mutacao(filho1)
            filho2 = mutacao(filho2)

            # adiciona filhos (copiando não precisa, já são listas novas)
            nova_pop.append(filho1)
            if len(nova_pop) < tamanho_pop:
                nova_pop.append(filho2)

        # substitui a população atual pela nova
        populacao = nova_pop

        # (opcional) pode imprimir resumo por geração - comente/descomente se quiser:
        if g % 10 == 0:
            print(f"Geração {g}: melhor fitness atual = {melhor_fitness}")

    # 4) Ao final, prepara e mostra o resultado final
    itens = []
    for i in range(num_itens):
        if melhor_individuo[i] == 1:
            itens.append(i + 1)   # usar i+1 para numerar itens a partir de 1

    peso_final = peso_total(melhor_individuo)
    valor_final = valor_total(melhor_individuo)

    print()
    print(f"Itens selecionados (nº): {itens}")
    print(f"Peso total (g): {peso_final}")
    print(f"Valor total: {valor_final}")
    print(f"A solução foi encontrada (melhor) na geração: {geracao_melhor}")


if __name__ == "__main__":
    # fixa semente para reprodutibilidade (pode remover se quiser resultados diferentes a cada execução)
    random.seed(42)
    algoritmo_genetico()
