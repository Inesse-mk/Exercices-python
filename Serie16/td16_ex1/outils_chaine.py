# outils_chaine.py

SEPARATEUR = "-" * 40

def compter_mots(texte: str) -> int:
    """Compte le nombre de mots dans une chaîne."""
    return len(texte.split())

def est_palindrome(texte: str) -> bool:
    """Vérifie si le texte est un palindrome (ignorer espaces et majuscules)."""
    t = texte.replace(" ", "").lower()
    return t == t[::-1]
