# td13_ex3_version_fonctionnelle.py

# Fonctions "libres"
def creer_panier():
    return []

def ajouter_article(panier, article):
    panier.append(article)

def total_articles(panier):
    return len(panier)


if __name__ == "__main__":
    # Création d'un panier
    panier = creer_panier()

    # Ajout d'articles
    ajouter_article(panier, "Pommes")
    ajouter_article(panier, "Bananes")
    ajouter_article(panier, "Chocolat")

    # Affichage du total d'articles
    print("Total d'articles dans le panier :", total_articles(panier))
