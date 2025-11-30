while True:
    def division_securisee():
        try:
            x = int(input("Numérateur : "))
            y = int(input("Dénominateur : "))
            resultat = x / y
        except ValueError:
            print("Veuillez entrer des entiers uniquement.")

        except ZeroDivisionError:
            print("Le dénominateur ne peut pas être zéro.")
        else:
            print("Résultat :", resultat)

    division_securisee()  
    
    stocker=division_securisee()
    if stocker is not None:
        print(f"Le résulat de la division est :{stocker}")