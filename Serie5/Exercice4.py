# Fonction pour appliquer une remise sur un prix
def appliquer_remise(prix: float, remise: float) -> float:
    """
    Calcule le prix final après application d'une remise.

    Parameters
    ----------
    prix : float
        Le prix initial du produit.
    remise : float
        La remise à appliquer (exprimée en fraction, par ex. 0.2 pour 20%).

    Returns
    -------
    float
        Le prix après application de la remise.

    Example
    -------
    >>> appliquer_remise(100, 0.2)
    80.0
    """
    prix_final = prix * (1 - remise)
    return prix_final

# Fonction pour compter le nombre de commandes supérieures à un seuil
def compter_commandes_superieures(commandes: list[float], seuil: float) -> int:
    """
    Compte le nombre de commandes supérieures ou égales à un certain seuil.

    Parameters
    ----------
    commandes : list[float]
        Liste des montants de commandes.
    seuil : float
        Le montant minimum pour qu'une commande soit comptée.

    Returns
    -------
    int
        Nombre de commandes supérieures ou égales au seuil.

    Example
    -------
    >>> compter_commandes_superieures([50, 120, 200], 100)
    2
    """
    compteur = 0
    for montant in commandes:
        if montant >= seuil:
            compteur += 1
    return compteur

# Fonction pour normaliser une adresse email
def normaliser_email(email: str) -> str:
    """
    Normalise une adresse email en supprimant les espaces superflus
    et en convertissant tous les caractères en minuscules.

    Parameters
    ----------
    email : str
        L'adresse email à normaliser.

    Returns
    -------
    str
        L'adresse email normalisée.

    Example
    -------
    >>> normaliser_email(" ExEMple@Mail.com ")
    'example@mail.com'
    """
    return email.strip().lower()
# Affiche la documentation de la fonction appliquer_remise
help(appliquer_remise)