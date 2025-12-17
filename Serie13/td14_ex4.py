# td13_ex4.py
from dataclasses import dataclass

@dataclass
class Client:
    nom: str
    email: str
    actif: bool = True

    def desactiver(self):
        """Méthode pour désactiver le client"""
        self.actif = False


if __name__ == "__main__":
    # Création de plusieurs clients
    client1 = Client("Alice", "alice@example.com")
    client2 = Client("Bob", "bob@example.com")
    client3 = Client("Charlie", "charlie@example.com", actif=False)

    # Affichage des clients
    print(client1)
    print(client2)
    print(client3)

    # Désactivation d'un client
    client1.desactiver()
    print("Après désactivation :", client1)

"""
Explications / avantages des dataclasses :

- Le décorateur @dataclass génère automatiquement :
    - __init__ (constructeur)
    - __repr__ (représentation lisible pour print)
    - __eq__ (comparaison d'égalité)
    - et d'autres méthodes utiles selon les options

- Cela évite d'écrire manuellement le constructeur et __repr__, 
  surtout pour des classes qui contiennent surtout des données.

- On peut toujours ajouter des méthodes métiers comme 'desactiver'.
"""
