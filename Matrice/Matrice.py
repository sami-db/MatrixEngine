import random

# Génère une matrice aléatoire de taille n
def generer_matrice_aleatoire(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
