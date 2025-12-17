# td16_ex1_main_from.py

from outils_chaine import compter_mots, est_palindrome, SEPARATEUR

def main():
    phrase = input("Saisis une phrase : ")

    print(SEPARATEUR)
    print(f"Nombre de mots : {compter_mots(phrase)}")
    print(f"Palindrome : {est_palindrome(phrase)}")
    print(SEPARATEUR)

if __name__ == "__main__":
    main()