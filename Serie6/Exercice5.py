class Client:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
    

class LigneCommande:
    def __init__(self, description, quantite, prix_unitaire):
        self.description = description
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire
    
    def total_ligne(self):
        return self.prix_unitaire * self.quantite
    
class Commande:
    def __init__(self, client):
        self.client = client
        self.lignes=[]

    def ajouter_ligne(self, ligne):
        self.lignes.append(ligne)
    
    def total(self):
        somme = 0
        for lignes in self.lignes:
            somme += lignes.total_ligne()
        return somme 

c = Client("Ines", "ines.malek9@gmail.com")  

l1= LigneCommande("Stylo bleu", 12, 1.5)
l2= LigneCommande("Clavier mécanique", 5, 89.99)
l3= LigneCommande("Cahier", 30, 2.4)

cmd = Commande(c)

cmd.ajouter_ligne(l1)
cmd.ajouter_ligne(l2)
cmd.ajouter_ligne(l3)

print(f"Client : {cmd.client.nom} ({cmd.client.email})")
print("\nLignes de commande :")

for ligne in cmd.lignes:
    print(f"- {ligne.description} x{ligne.quantite} → {ligne.total_ligne():.2f}€")

print(f"\nTotal de la commande : {cmd.total():.2f}€")


        
        