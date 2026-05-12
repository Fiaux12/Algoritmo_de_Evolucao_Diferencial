import numpy as np
import random
import statistics
from itertools import product
from graficos import grafico_F, grafico_CR, grafico_N

D =  10                #numero de variaveis
N_ =  [10, 20, 30, 40, 50]      #tamanho da população
F_ =  [0.3, 0.4, 0.5, 0.7, 0.8]   #Fator de Escala (0, 2]
CR_ = [0.3, 0.4, 0.5, 0.7, 0.8]   #Prob. de Cruzamento CR [0, 1]

# N = 20
# F = 0.5
# CR = 0.7
def evolucao_diferencial(N, F, CR):
    
    populacao = inicia_populacao(N)
    iteracoes = 0

    while iteracoes < 100:
        for i in range(N):
            xi = populacao[i]

            v = mutacao(populacao, i, N, F)
            u = cruzamento(v, xi, CR)
            populacao[i] = selecao(xi, u)

        iteracoes += 1
  
    solucao = min(populacao, key=avaliar_fitness)
    custo = avaliar_fitness(solucao)
    return solucao, custo
    

def mutacao(populacao, i, N, F):
    indices = list(range(N))
    indices.remove(i)
    xr1, xr2, xr3 = populacao[np.random.choice(indices, 3, replace=False)]            
    v = xr1 + F * (xr2 - xr3)

    #Aplica limites
    v = np.clip(v, -5, 5)
    return v

def cruzamento(v, xi, CR):
    u = np.zeros(D)

    # Garante ao menos um gene de v
    j_rand = np.random.randint(D)

    for j in range(D):
        num = random.random()
        if(num < CR) or j == j_rand:
            u[j] = v[j]
        else:
            u[j] = xi[j]
    
    return u

def selecao(xi, u):
    custo_xi = avaliar_fitness(xi)
    custo_u = avaliar_fitness(u)

    if(custo_u <= custo_xi):
        return u
    else:
        return xi
        
def inicia_populacao(N):
    p = np.random.uniform(-5, 5, (N, D))
    return np.round(p, 2)

def avaliar_fitness(x):
    return np.sum(x**2)

def main():
    resultados = []
    for N, F, CR in product(N_, F_, CR_ ):
        custos = []
        # solucoes = []

        for i in range(30):
            solucao, custo = evolucao_diferencial(N, F, CR)
            custos.append(custo)
            # solucoes.append(solucao)

        melhor_indice = np.argmin(custos)

        media = statistics.mean(custos)
        # print(f"N={N}, F={F}, CR={CR} -> Média: {media}")

        resultados.append({
            "N": N,
            "F": F,
            "CR": CR,
            "media": media
        })

        # print("Melhor solução:", solucoes[melhor_indice])
        print(f"N={N}, F={F}, CR={CR} -> Menor custo: {custo}")
        # print("Média dos custos:", statistics.mean(custos))

    grafico_N(resultados, N_)
    grafico_F(resultados, F_)
    grafico_CR(resultados, CR_)

main()
