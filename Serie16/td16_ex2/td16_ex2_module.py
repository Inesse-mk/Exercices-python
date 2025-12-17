def demo():
    print("Fonction demo() appelée")

# Ce print s'exécute même quand on importe le module
print("Import de td16_ex2_module")

if __name__ == "__main__":
    print("Exécution directe de td16_ex2_module")
    demo()