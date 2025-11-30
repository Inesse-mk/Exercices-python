notes = []

with open("notes.txt", "r") as fichier:
    for ligne in fichier:
        note = float(ligne.strip())
        notes.append(note)

print(notes)

print("Min :", min(notes))
print("Max :", max(notes))

somme = 0
for note in notes:
    somme += note

moyenne = somme / len(notes)
print ("Moyenne :", moyenne)

compteur_reussite = 0
for note in notes:
    if note >= 10:
        compteur_reussite += 1

print("Nombre de réussites (>= 10) :", compteur_reussite)

prc_reussite = (compteur_reussite * 100) / len(notes)
print("Pourcentage de réussite :", prc_reussite)
