# Lecture des notes depuis un fichier et stockage dans une liste
notes = []

with open("notes.txt", "r") as fichier:
    for ligne in fichier:
        note = float(ligne.strip())
        notes.append(note)

print(notes)
# Affichage de la note minimale et maximale
print("Min :", min(notes))
print("Max :", max(notes))
# Calcul de la moyenne
somme = 0
for note in notes:
    somme += note

moyenne = somme / len(notes)
print ("Moyenne :", moyenne)
# Comptage des réussites (notes >= 10)
compteur_reussite = 0
for note in notes:
    if note >= 10:
        compteur_reussite += 1

print("Nombre de réussites (>= 10) :", compteur_reussite)
# Calcul du pourcentage de réussite
prc_reussite = (compteur_reussite * 100) / len(notes)
print("Pourcentage de réussite :", prc_reussite)
