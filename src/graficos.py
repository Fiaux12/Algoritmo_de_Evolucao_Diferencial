import statistics
import matplotlib.pyplot as plt

def grafico_N(resultados, N_): 
    media_N = []

    print("medias N:")

    for N in N_:

        valores = [r["media"] for r in resultados if r["N"] == N]
        media_N.append(statistics.mean(valores))

        print(statistics.mean(valores))
    

    plt.figure(figsize=(6,4))
    plt.plot(N_, media_N, marker='o',color='blue')
    plt.xlabel("Tamanho da População (N)")
    plt.ylabel("Média do Custo")
    plt.title("N vs Média")
    plt.grid(True)
    plt.show()

def grafico_F(resultados, F_): 
    media_F = []
    print("medias F:")

    for F in F_:

        valores = [r["media"] for r in resultados if r["F"] == F]
        media_F.append(statistics.mean(valores))
    
        print(statistics.mean(valores))

    plt.figure(figsize=(6,4))
    plt.plot(F_, media_F, marker='o',color='purple')
    plt.xlabel("Fator de Escala (F)")
    plt.ylabel("Média do Custo")
    plt.title("F vs Média")
    plt.grid(True)
    plt.show()


def grafico_CR(resultados, CR_): 
    media_CR = []
    print("medias CR:")

    for CR in CR_:
        valores = [r["media"] for r in resultados if r["CR"] == CR]
        media_CR.append(statistics.mean(valores))

        print(statistics.mean(valores))

    plt.figure(figsize=(6,4))
    plt.plot(CR_, media_CR, marker='o', color='pink')
    plt.xlabel("Probabilidade de Cruzamento (CR)")
    plt.ylabel("Média do Custo")
    plt.title("CR vs Média")
    plt.grid(True)
    plt.show()

