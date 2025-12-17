def ajouter_tache(liste_taches, tache):
    liste_taches.append(tache)

def marquer_terminee(liste_taches, titre):
    for t in liste_taches:
        if t.titre == titre:
            t.statut = "terminée"
            return True
    return False # si titre non trouvé


def afficher_toutes(liste_taches):
    if not liste_taches:
        print("Aucune tâche.")
    for t in liste_taches:
        t.afficher()