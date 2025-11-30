class Employee :
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base

    def calculer_salaire(self):
        return self.salaire_base
    
    def afficher(self):
        print(f"Nom : {self.nom}, Salaire : {self.calculer_salaire()}")

class Developpeur(Employee):
    def __init__(self, nom, salaire_base, prime_technique):
        super().__init__(nom, salaire_base)
        self.prime_technique = prime_technique

    def calculer_salaire(self):
        return self.salaire_base + self.prime_technique
        
class Manager(Employee):
    def __init__(self, nom, salaire_base, prime_management):
          super().__init__(nom, salaire_base)
          self.prime_management = prime_management

    def calculer_salaire(self):
        return self.salaire_base + self.prime_management



dev1 = Developpeur("Ines", 7000, 1400)
dev2 = Developpeur("Alice", 3000, 50)
dev3 = Developpeur("Ali", 8000, 100)

man1 = Manager("Bob", 1500, 80)
man2 = Manager("Sam", 2500, 150)
man3 = Manager("Aymen", 5000, 900)

list = [dev1, dev2, dev3, man1, man2, man3]

for i in list:
    print(f"Type : {type(i).__name__} , Nom : { i.nom}, Salaire calculé {i.calculer_salaire()}")
