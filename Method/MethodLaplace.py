def determinant_laplace(matrice, memo={}):
    n = len(matrice)

    # Gestion des cas de matrice de taille 1x1 et 2x2 :
    if n == 1:
        return matrice[0][0]
    elif n == 2:
        return matrice[0][0] * matrice[1][1] - matrice[0][1] * matrice[1][0]

    det = 0

    # Gestion des cas des matrices de taille 3x3 et plus
    for j in range(n):
        # on stock dans memo_key les résultats des sous-matrices
        memo_key = tuple(tuple(row[k] for k in range(n) if k != j) for row in matrice[1:])

        if memo_key in memo:
            minor_det = memo[memo_key]
        else:
            # Sous-matrice en excluant la ligne 0 et la colonne j
            sous_matrice = [row[:j] + row[j + 1:] for row in matrice[1:]]
            minor_det = determinant_laplace(sous_matrice, memo)
            memo[memo_key] = minor_det

        cof = (-1) ** j * matrice[0][j]
        det += cof * minor_det

    return det
