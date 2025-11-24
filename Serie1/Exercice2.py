# Exercice 2
prixHT=(input("Entrez le prix HT "))
tauxTVA=(input("Entrez le taux du TVA en pourcentage "))
prixHT=float(prixHT)
tauxTVA=float(tauxTVA)
tva = prixHT * tauxTVA/ 100
prixTTC= prixHT + tauxTVA
print (f"pour un prix HT de {prixHT}€ et une TVA de {tauxTVA}%, le prix TTC est de {prixTTC}€")

