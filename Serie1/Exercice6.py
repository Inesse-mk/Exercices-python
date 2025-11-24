def est_pair(n):
    if n % 2 == 0:
        print("True")
    else:
        print("False")

est_pair(1)

def calculer_tv(prix_ht, taux):
    return prix_ht + taux
print(calculer_tv(15,13))

def moyenne(liste_nombres):
    return sum(liste_nombres)/len(liste_nombres)
print(moyenne([9.99, 14.5, 3.2, 29.0]))
