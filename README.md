# Algoritmo de Evolução Diferencial

Trabalho prático da disciplina de Fundamentos de Inteligência Artificial (UFMG) com implementação do Algoritmo Evolução Diferencial (ED) para minimização contínua.

## Problema Solucionado 

O trabalho consiste em minimizar a função: 

```math
f(x) = \sum_{i=1}^{10} x_i^2
```
sujeito a:
```math
−5≤ x_i ​≤5
```
utilizando o algoritmo proposto.

### O que foi implementado:
- Inicialização aleatória da população
- Mutação diferencial
- Cruzamento binomial
- Seleção elitista
- Testes com diferentes valores de:
  - tamanho da população (`N`)
  - fator de escala (`F`)
  - probabilidade de cruzamento (`CR`)

Autor: Amanda Fiaux da Silva
