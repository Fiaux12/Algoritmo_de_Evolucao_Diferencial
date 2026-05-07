import numpy as np
import random

"""
                PROBLEMA 1

    Minimizar f(x) = Σ xi^2,
    para i de 1 a 10,
    onde 
        -5 ≤ x ≤ 5
"""


N = 5 #tamanho da população
D = 10 #numero de variaveis
F = 0.5 #Fator de Escala (0, 2], magnitude do passo
CR = 0.7 #Prob. de Cruzamento CR [0, 1]

def evolucao_diferencial():
    
    populacao = inicia_populacao()
    # print(populacao)

    iteracoes = 0

    while iteracoes < 1:

        for i in range(N):
            xi = populacao[i]

            v = mutacao(populacao, i)
            u = cruzamento(v, xi)
            populacao[i] = selecao(xi, u)

        iteracoes += 1
    
    print('Custos:')
    for x in populacao:
        print("     ", avaliar_fitness(x))
    
    melhor_solucao = min(populacao, key=avaliar_fitness)
    return melhor_solucao
    

def mutacao(populacao, i,):
    indices = list(range(N))
    indices.remove(i)
    xr1, xr2, xr3 = populacao[np.random.choice(indices, 3, replace=False)]            
    v = xr1 + F * (xr2 - xr3)

    #Aplica a borda
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
        
# inicia população: conjunto de varios vetores candidados a x
def inicia_populacao():
    p = np.random.uniform(-5, 5, (N, D))
    return np.round(p, 2)

# verificar qualidade da solução: quanto mais baixo melhor
def avaliar_fitness(x):
    return np.sum(x**2)


solucao = evolucao_diferencial()

print("Melhor solução:", solucao)
print("Custo minimo:", avaliar_fitness(solucao))