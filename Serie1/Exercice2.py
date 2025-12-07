prixHT = float(input("Entrez le prix HT : "))          # saisie du prix HT
tauxTVA = float(input("Entrez le taux de TVA : "))     # saisie du taux en %

tva = prixHT * tauxTVA / 100                           # calcul de la TVA
prixTTC = prixHT + tva                                 # calcul du prix TTC

print(f"Pour un prix HT de {prixHT}€ et une TVA de {tauxTVA}%, le prix TTC est de {prixTTC}€")