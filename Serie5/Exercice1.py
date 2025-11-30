utilisateur = {
    "nom": "Alice",
    "email": "alice@example.com",
    "age": 30
}
def get_age_lbyl(utilisateur):
    if "age" in utilisateur:
        return utilisateur["age"]

    else:
        print("Clé 'age' absente, valeur par défaut utilisée.")
        return None

res=get_age_lbyl(utilisateur)
print(f"Age récupéré : {res}")

def get_age_eafp(utilisateur):
    try:
        age = utilisateur["age"]
        return utilisateur["age"]

    except KeyError:
        print("Clé 'age' absente, valeur par défaut utilisée.")
        return None

res2=get_age_eafp(utilisateur)
print(f"Age récupéré : {res2}")

if __name__ == "__main__":
    # dictionnaire QUI CONTIENT "age"
    print("=== Test avec dictionnaire contenant 'age' ===")
    res = get_age_lbyl(utilisateur)
    print(f"LBYL -> Age récupéré : {res}")

    res2 = get_age_eafp(utilisateur)
    print(f"EAFP -> Age récupéré : {res2}")

    # dictionnaire QUI NE CONTIENT PAS "age"
    utilisateur_sans_age = {
        "nom": "Bob",
        "email": "bob@example.com"
    }

    print("\n=== Test avec dictionnaire SANS 'age' ===")
    res = get_age_lbyl(utilisateur_sans_age)
    print(f"LBYL -> Age récupéré : {res}")

    res2 = get_age_eafp(utilisateur_sans_age)
    print(f"EAFP -> Age récupéré : {res2}")