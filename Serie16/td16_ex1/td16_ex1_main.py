# td16_ex1_main.py

import outils_chaine

def main():
    phrase = input("Saisis une phrase : ")

    print(outils_chaine.SEPARATEUR)
    print(f"Nombre de mots : {outils_chaine.compter_mots(phrase)}")
    print(f"Palindrome : {outils_chaine.est_palindrome(phrase)}")
    print(outils_chaine.SEPARATEUR)

if __name__ == "__main__":
    main()
