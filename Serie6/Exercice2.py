class compteBancaire:
    def __init__(self,titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self,montant):
        if montant > 0:
            self.solde += montant
            return self.solde
        else:
            print(f"le montant est négatif")
        
    def retirer(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            return self.solde
        else:
            print(" le solde est insuffisant pour un retrait")
            
    def afficher (self):
        print(f"Le titulaire de ce compte est : {self.titulaire} et Son solde actuel est de : {self.solde} €")
    
a = compteBancaire ("Alice", 7000)
a.afficher()
print(f"Le solde actuel est : {a.deposer(500)} €")
print(f"Le solde actuel est : {a.retirer(20)} €")


