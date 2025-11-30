# Exercice 2
notes = [12, 5.5, 17, 9, 13, 8, 10]
print("Min :", min(notes))
print("Max :", max(notes))

somme = 0
for note in notes:
    somme = somme + note

moyenne = somme / len(notes)
print ("Moyenne :", moyenne)

compteur_reussite = 0
for note in notes:
    if note >= 10:
        compteur_reussite = compteur_reussite + 1
print("Nombre de réussites (>= 10) :", compteur_reussite)

prc_reussite= (compteur_reussite * 100)/len(notes)
print(prc_reussite)