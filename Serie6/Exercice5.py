# Classe représentant un client
class Client:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
    
# Classe représentant une ligne de commande (produit + quantité + prix unitaire)
class LigneCommande:
    def __init__(self, description, quantite, prix_unitaire):
        self.description = description
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire
     # Calcul du total pour cette ligne
    def total_ligne(self):
        return self.prix_unitaire * self.quantite
# Classe représentant une commande complète pour un client   
class Commande:
    def __init__(self, client):
        self.client = client
        self.lignes=[]
    
    # Ajouter une ligne à la commande
    def ajouter_ligne(self, ligne):
        self.lignes.append(ligne)
    # Calcul du total de la commande
    def total(self):
        somme = 0
        for lignes in self.lignes:
            somme += lignes.total_ligne()
        return somme 
# Création d'un client
c = Client("Ines", "ines.malek9@gmail.com")  
# Création de lignes de commande
l1= LigneCommande("Stylo bleu", 12, 1.5)
l2= LigneCommande("Clavier mécanique", 5, 89.99)
l3= LigneCommande("Cahier", 30, 2.4)
# Création de la commande pour le client
cmd = Commande(c)
# Ajout des lignes à la commande
cmd.ajouter_ligne(l1)
cmd.ajouter_ligne(l2)
cmd.ajouter_ligne(l3)
# Affichage des informations de la commande
print(f"Client : {cmd.client.nom} ({cmd.client.email})")
print("\nLignes de commande :")

for ligne in cmd.lignes:
    print(f"- {ligne.description} x{ligne.quantite} → {ligne.total_ligne():.2f}€")
# Affichage du total de la commande
print(f"\nTotal de la commande : {cmd.total():.2f}€")


        
        