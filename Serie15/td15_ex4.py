class Logger:
    def log(self, message):
        print(f"[INFO] {message}")


class TimestampLogger(Logger):
    def log(self, message):
        # Ajout de l'horodatage avant d'appeler Logger.log
        from datetime import datetime
        super().log(f"{datetime.now().isoformat(timespec='seconds')} - {message}")


class UppercaseLogger(Logger):
    def log(self, message):
        # Affiche le message en majuscules
        super().log(message.upper())


class Application:
    # COMPOSITION : l'application possède un logger
    def __init__(self, logger):
        self.logger = logger

    def executer(self):
        self.logger.log("L'application a exécuté une action.")


# --- MAIN ---
if __name__ == "__main__":

    # Test des trois loggers
    l = Logger()
    tl = TimestampLogger()
    ul = UppercaseLogger()

    print("--- Test Logger ---")
    l.log("test du logger")

    print("--- Test TimestampLogger ---")
    tl.log("test du logger")

    print("--- Test UppercaseLogger ---")
    ul.log("test du logger")

    # Test de la composition avec Application
    print("\n--- Application avec TimestampLogger ---")
    app1 = Application(TimestampLogger())
    app1.executer()

    print("\n--- Application avec UppercaseLogger ---")
    app2 = Application(UppercaseLogger())
    app2.executer()



# RÉPONSES AUX QUESTIONS

# 1. Dans cet exemple, quelles classes sont liées par héritage ?
#    → TimestampLogger hérite de Logger.
#    → UppercaseLogger hérite aussi de Logger.

# 2. Quelle classe utilise la composition ?
#    → La classe Application utilise la composition : elle *possède* un logger.

# 3. Pourquoi la composition offre-t-elle ici plus de flexibilité ?
#    → Parce que la classe Application n'a pas besoin de connaître les détails
#      ou les variantes du logger. On peut lui fournir n'importe quel objet
#      compatible (Logger, TimestampLogger, UppercaseLogger, ou un futur autre logger).
#      Aucun changement du code d'Application n'est nécessaire.
#      Cela permet de changer le comportement dynamiquement sans modifier la classe.

