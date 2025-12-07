notes = [12, 5.5, 17, 9, 13, 8, 10]

# Minimum et maximum
print("Min :", min(notes))
print("Max :", max(notes))

# Calcul de la somme et de la moyenne
somme = 0
for note in notes:
    somme += note

moyenne = somme / len(notes)
print("Moyenne :", moyenne)

# Comptage des réussites (notes >= 10)
compteur_reussite = 0
for note in notes:
    if note >= 10:
        compteur_reussite += 1
print("Nombre de réussites (>= 10) :", compteur_reussite)

# Pourcentage de réussites
prc_reussite = (compteur_reussite * 100) / len(notes)
print(prc_reussite)
