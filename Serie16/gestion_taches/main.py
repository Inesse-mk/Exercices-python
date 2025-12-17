from todo import Tache, ajouter_tache, marquer_terminee, afficher_toutes

def main():
    # Créer la liste de tâches **avant** tout ajout
    liste_taches = []

    # Création des tâches
    t1 = Tache("Acheter du lait", "Acheter 2L de lait")
    t2 = Tache("Faire le ménage", "Nettoyer la cuisine et le salon")
    t3 = Tache("Etudier Python", "Terminer les exercices du chapitre 16")

    # Ajouter les tâches à la liste
    ajouter_tache(liste_taches, t1)
    ajouter_tache(liste_taches, t2)
    ajouter_tache(liste_taches, t3)

    print("--- Tâches initiales ---")
    afficher_toutes(liste_taches)

    # Marquer une tâche comme terminée
    marquer_terminee(liste_taches, "Faire le ménage")

    print("--- Après mise à jour ---")
    afficher_toutes(liste_taches)

if __name__ == "__main__":
    main()
