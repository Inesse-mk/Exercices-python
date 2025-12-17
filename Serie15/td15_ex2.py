class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        # Constructeur de la classe parente
        self.titulaire = titulaire
        self.solde = solde_initial

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        # Vérifications du montant
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        if montant > self.solde:
            raise ValueError("Solde insuffisant.")
        self.solde -= montant

    def afficher(self):
        print(f"{self.titulaire} – solde : {self.solde} €")


class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire, solde_initial=0, taux_interet=0.02):
        # Utilisation de super() pour appeler le constructeur parent
        super().__init__(titulaire, solde_initial)
        self.taux_interet = taux_interet

    def appliquer_interets(self):
        # Application du taux d'intérêt
        self.solde += self.solde * self.taux_interet


class CompteCourant(CompteBancaire):
    def __init__(self, titulaire, solde_initial=0, decouvert_autorise=0):
        # Appel du constructeur parent avec super()
        super().__init__(titulaire, solde_initial)
        self.decouvert_autorise = decouvert_autorise

    def retirer(self, montant):
        # Surcharge de la méthode retirer pour autoriser un découvert
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        if self.solde - montant < -self.decouvert_autorise:
            raise ValueError("Découvert autorisé dépassé.")
        self.solde -= montant


# --- MAIN ---
if __name__ == "__main__":
    # Création des comptes
    cb = CompteBancaire("Alice", 1000)
    ce = CompteEpargne("Bob", 5000, 0.03)
    cc = CompteCourant("Charlie", 200, decouvert_autorise=300)

    # Opérations
    cb.deposer(200)
    cb.retirer(150)

    ce.deposer(500)
    ce.appliquer_interets()

    cc.deposer(100)

    try:
        cc.retirer(700)  # Devrait passer (solde final = -400, découvert = 300 → erreur)
    except ValueError as e:
        print("Erreur CC :", e)

    try:
        cc.retirer(500)  # Devrait passer jusqu'à -300
    except ValueError as e:
        print("Erreur CC :", e)

    # Affichage final
    cb.afficher()
    ce.afficher()
    cc.afficher()
