# Elimination de Gauss
def elimination_gauss(matrice):
    n = len(matrice)
    for i in range(n):
        if matrice[i][i] == 0:
            pivot_non_nul = False
            for k in range(i + 1, n):
                if matrice[k][i] != 0:
                    pivot_non_nul = True
                    matrice[i], matrice[k] = matrice[k], matrice[i]  # Échange les lignes
                    break
            if not pivot_non_nul:
                raise ValueError("La matrice est singulière")
        for j in range(i + 1, n):
            facteur = matrice[j][i] / matrice[i][i]
            for k in range(i, n):
                matrice[j][k] -= facteur * matrice[i][k]
    return matrice

# substitution arrière de gauss sur une matrice
def substitution_arriere_gauss(matrice):
    n = len(matrice)
    for i in range(n - 1, -1, -1):
        pivot = matrice[i][i]
        for j in range(i - 1, -1, -1):
            facteur = matrice[j][i] / pivot
            for k in range(n - 1, i - 1, -1):
                matrice[j][k] -= facteur * matrice[i][k]
        for j in range(n):
            matrice[i][j] /= pivot
    return matrice

# inversion de la matrice avec la methode de gauss
def inversion_gauss(matrice):
    matrice = elimination_gauss(matrice)
    matrice = substitution_arriere_gauss(matrice)
    return matrice
