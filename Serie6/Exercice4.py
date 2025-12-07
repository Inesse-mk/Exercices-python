# Classe de base pour un employé
class Employee :
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base
    # Calcul du salaire de base
    def calculer_salaire(self):
        return self.salaire_base
    # Affichage des informations de l'employé
    def afficher(self):
        print(f"Nom : {self.nom}, Salaire : {self.calculer_salaire()}")
# Classe pour un développeur, héritée de Employee
class Developpeur(Employee):
    def __init__(self, nom, salaire_base, prime_technique):
        super().__init__(nom, salaire_base)
        self.prime_technique = prime_technique
    # Calcul du salaire avec prime technique
    def calculer_salaire(self):
        return self.salaire_base + self.prime_technique
# Classe pour un manager, héritée de Employee       
class Manager(Employee):
    def __init__(self, nom, salaire_base, prime_management):
          super().__init__(nom, salaire_base)
          self.prime_management = prime_management
    # Calcul du salaire avec prime management
    def calculer_salaire(self):
        return self.salaire_base + self.prime_management


# Création d'objets
dev1 = Developpeur("Ines", 7000, 1400)
dev2 = Developpeur("Alice", 3000, 50)
dev3 = Developpeur("Ali", 8000, 100)

man1 = Manager("Bob", 1500, 80)
man2 = Manager("Sam", 2500, 150)
man3 = Manager("Aymen", 5000, 900)
# Liste des employés
employes = [dev1, dev2, dev3, man1, man2, man3]

# Affichage du type, du nom et du salaire calculé
for employe in employes:
    print(f"Type : {type(employe).__name__} , Nom : {employe.nom}, Salaire calculé : {employe.calculer_salaire()}")