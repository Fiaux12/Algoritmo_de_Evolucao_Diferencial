import numpy as np
import random

D =  10                #numero de variaveis
N =  [10, 20, 50]      #tamanho da população
F =  [0.3, 0.5, 0.8]   #Fator de Escala (0, 2]
CR = [0.5, 0.7, 0.9]   #Prob. de Cruzamento CR [0, 1]

def evolucao_diferencial():
    
    populacao = inicia_populacao()
    iteracoes = 0

    while iteracoes < 1000:
        for i in range(N):
            xi = populacao[i]

            v = mutacao(populacao, i)
            u = cruzamento(v, xi)
            populacao[i] = selecao(xi, u)

        iteracoes += 1
  
    melhor_solucao = min(populacao, key=avaliar_fitness)
    return melhor_solucao
    

def mutacao(populacao, i,):
    indices = list(range(N))
    indices.remove(i)
    xr1, xr2, xr3 = populacao[np.random.choice(indices, 3, replace=False)]            
    v = xr1 + F * (xr2 - xr3)

    #Aplica limites
    v = np.clip(v, -5, 5)
    return v

def cruzamento(v, xi):
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
        
def inicia_populacao():
    p = np.random.uniform(-5, 5, (N, D))
    return np.round(p, 2)

def avaliar_fitness(x):
    return np.sum(x**2)


solucao = evolucao_diferencial()

print("Melhor solução:", solucao)
print("Custo minimo:", avaliar_fitness(solucao))