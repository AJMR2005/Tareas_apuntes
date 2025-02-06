def matriz_simetrica(X):
 bandera = True
 for i in range(len(X)-1):
    for j in range(i+1,len(X)):
        bandera = bandera and (X[i][j] == X[j][i])
 return bandera
 print(matriz_simetrica([[1,-3],[4,11]]))
 print(matriz_simetrica([["A","B"],["B","A"]]))