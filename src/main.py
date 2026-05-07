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
    print(populacao)

    custos = np.array([avaliar_fitness(x) for x in populacao])

    iteracoes = 0

    while iteracoes < 1:

        for i in range(N):
            # Mutação
            xi = populacao[i]
            indices = list(range(N))
            indices.remove(i)
            
            xr1, xr2, xr3 = populacao[np.random.choice(indices, 3, replace=False)]            
            v = xr1 + F * (xr2 - xr3)

            #Aplica a borda
            v = np.clip(v, -5, 5)

            # Cruzamento/Recombinação
            u = np.zeros(D)
            for j in range(D):
                num = random.random()
                if(num < CR):
                    u[j] = v[j]
                else:
                    u[j] = xi[j]
                

            # 
            # Seleção

        iteracoes += 1


# inicia população: conjunto de varios vetores candidados a x
def inicia_populacao():
    p = np.random.uniform(-5, 5, (N, D))
    return np.round(p, 2)


# verificar qualidade da solução: quanto mais baixo melhor
def avaliar_fitness(x):
    return np.sum(x**2)


evolucao_diferencial()