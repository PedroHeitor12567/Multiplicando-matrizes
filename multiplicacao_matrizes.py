def multiplica_matrizes(matriz1, matriz2):
    matriz_multiplicada = []
    if len(matriz1[0]) != len(matriz2):
        return "As matrizes não são compatíveis"
    else:
        for l in range(len(matriz1)):
            linha = []
            for c in range(len(matriz2[0])):
                resul = 0
                for i in range(len(matriz2)):
                    resul += matriz1[l][i] * matriz2[i][c]
                linha.append(resul)
            matriz_multiplicada.append(linha)
        return matriz_multiplicada         

matriz1 = [
    [1, 2, 3],
    [4, 5, 6]
]
matriz2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]
print(multiplica_matrizes(matriz1, matriz2))