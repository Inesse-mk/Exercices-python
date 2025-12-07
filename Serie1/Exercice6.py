# Fonction pour vérifier si un nombre est pair
def est_pair(n):
    return n % 2 == 0

print(est_pair(1))   # False
print(est_pair(4))   # True

# Fonction pour calculer le prix TTC à partir du prix HT et du taux de TVA
def calculer_tv(prix_ht, taux):
    tva = prix_ht * taux / 100
    return prix_ht + tva

print(calculer_tv(15, 13))  # 16.95

# Fonction pour calculer la moyenne d'une liste de nombres
def moyenne(liste_nombres):
    if len(liste_nombres) == 0:
        return 0
    return sum(liste_nombres) / len(liste_nombres)

print(moyenne([9.99, 14.5, 3.2, 29.0]))  # 14.4225