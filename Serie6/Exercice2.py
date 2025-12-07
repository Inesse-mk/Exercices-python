# Définition d'une classe CompteBancaire
class compteBancaire:
    def __init__(self,titulaire, solde):
        # Constructeur : initialise le titulaire et le solde du compte
        self.titulaire = titulaire
        self.solde = solde
    # Méthode pour déposer de l'argent
    def deposer(self,montant):
        if montant > 0:
            self.solde += montant
            return self.solde
        else:
            print(f"le montant est négatif")
    # Méthode pour retirer de l'argent    
    def retirer(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            return self.solde
        else:
            print(" le solde est insuffisant pour un retrait")
    # Méthode pour afficher les informations du compte      
    def afficher (self):
        print(f"Le titulaire de ce compte est : {self.titulaire} et Son solde actuel est de : {self.solde} €")
# Création d'un compte bancaire pour Alice   
a = compteBancaire ("Alice", 7000)
# Affichage des informations du compte
a.afficher()
# Dépôt de 500 €
print(f"Le solde actuel est : {a.deposer(500)} €")
# Retrait de 20 €
print(f"Le solde actuel est : {a.retirer(20)} €")


