from typing import List

# Fonction qui calcule la moyenne d'une liste de notes
def calculer_moyenne(notes: List[float]) -> float:
    return sum(notes) / len(notes)

# Fonction qui filtre les notes supérieures ou égales à un seuil
def filtrer_notes_suffisantes(notes: List[float], seuil: float) -> List[float]:
    result = []
    for n in notes:
        if n >= seuil:
            result.append(n)
    return result

# Fonction qui formate un message pour un étudiant
def formater_message(nom: str, moyenne: float) -> str:
    return f"Étudiant {nom} : moyenne = {moyenne:.2f}"

# --- Utilisation des fonctions ---
notes = [10.5, 15.9, 6.3, 20]
nom_etudiant = "Alice"
seuil = 10

moyenne = calculer_moyenne(notes)
notes_suffisantes = filtrer_notes_suffisantes(notes, seuil)
message = formater_message(nom_etudiant, moyenne)

print("Moyenne générale :", moyenne)
print("Notes supérieures ou égales à", seuil, ":", notes_suffisantes)
print(message)
