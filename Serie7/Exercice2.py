import matplotlib.pyplot as plt

# 1. Données - 6 catégories
categories = ["Électronique", "Mode", "Maison", "Sport", "Beauté", "Livres"]
ca = [12000, 8000, 6000, 4000, 7500, 3500]

# 2. Créer le graphique avec des couleurs personnalisées
fig, ax = plt.subplots(figsize=(12, 7))

# Palette de couleurs
couleurs = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#C7CEEA']

# Tracer les barres
barres = ax.bar(categories, ca, color=couleurs, edgecolor='black', linewidth=1.2, alpha=0.8)

# 3. Titre et labels
ax.set_title("Chiffre d'affaires par catégorie - Année 2024", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Catégorie de produits", fontsize=13, fontweight='bold')
ax.set_ylabel("Chiffre d'affaires (€)", fontsize=13, fontweight='bold')

# Grille pour faciliter la lecture
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# 4. BONUS : Afficher les valeurs au-dessus des barres
for i, (barre, valeur) in enumerate(zip(barres, ca)):
    hauteur = barre.get_height()
    ax.text(barre.get_x() + barre.get_width() / 2, hauteur + 200,
            f'{valeur:,} €'.replace(',', ' '),
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# Ajuster les limites de l'axe Y pour laisser de l'espace au-dessus
ax.set_ylim(0, max(ca) * 1.15)

# Rotation des labels de catégories pour plus de lisibilité
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()


# --- VERSION ALTERNATIVE : Barres horizontales ---
print("\n--- Version avec barres horizontales ---\n")

fig, ax = plt.subplots(figsize=(10, 8))

# Barres horizontales avec barh()
barres_h = ax.barh(categories, ca, color=couleurs, edgecolor='black', linewidth=1.2, alpha=0.8)

ax.set_title("Chiffre d'affaires par catégorie - Vue horizontale", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Chiffre d'affaires (€)", fontsize=13, fontweight='bold')
ax.set_ylabel("Catégorie de produits", fontsize=13, fontweight='bold')

ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Afficher les valeurs à droite des barres
for i, (barre, valeur) in enumerate(zip(barres_h, ca)):
    largeur = barre.get_width()
    ax.text(largeur + 200, barre.get_y() + barre.get_height() / 2,
            f'{valeur:,} €'.replace(',', ' '),
            ha='left', va='center', fontsize=11, fontweight='bold')

ax.set_xlim(0, max(ca) * 1.15)

plt.tight_layout()
plt.show()


# --- Affichage des statistiques ---
print("\n=== Statistiques du chiffre d'affaires ===")
print(f"CA Total : {sum(ca):,} €".replace(',', ' '))
print(f"CA Moyen : {sum(ca)/len(ca):,.2f} €".replace(',', ' '))
print(f"Meilleure catégorie : {categories[ca.index(max(ca))]} ({max(ca):,} €)".replace(',', ' '))
print(f"Catégorie à améliorer : {categories[ca.index(min(ca))]} ({min(ca):,} €)".replace(',', ' '))