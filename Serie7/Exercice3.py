import matplotlib.pyplot as plt
import numpy as np

# 1. Données sur 10 jours
jours = list(range(1, 11))
trafic = [800, 950, 1100, 1250, 1400, 1600, 1750, 1900, 2100, 2250]
revenu = [2000, 2300, 2700, 3100, 3400, 3900, 4200, 4600, 5100, 5400]

# 2. Créer une figure avec 2 graphiques
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# --- GRAPHIQUE 1 : Nuage de points basique ---
ax1.scatter(trafic, revenu, alpha=0.7, s=100, color='#3498db', edgecolors='black', linewidth=1.5)
ax1.set_title("Relation entre trafic et revenu", fontsize=15, fontweight='bold', pad=15)
ax1.set_xlabel("Trafic (nombre de visites)", fontsize=12, fontweight='bold')
ax1.set_ylabel("Revenu (€)", fontsize=12, fontweight='bold')
ax1.grid(True, alpha=0.3, linestyle='--')

# --- GRAPHIQUE 2 : Nuage de points avancé avec ligne de tendance ---
# Points colorés selon le jour (du bleu au rouge)
couleurs = plt.cm.coolwarm(np.linspace(0, 1, len(jours)))
scatter = ax2.scatter(trafic, revenu, c=jours, cmap='coolwarm', 
                      alpha=0.7, s=150, edgecolors='black', linewidth=1.5)

# Ajouter une ligne de tendance (régression linéaire)
z = np.polyfit(trafic, revenu, 1)  # Degré 1 = ligne droite
p = np.poly1d(z)
ax2.plot(trafic, p(trafic), "r--", linewidth=2, label=f'Tendance: y = {z[0]:.2f}x + {z[1]:.0f}')

# Annoter quelques points intéressants
ax2.annotate(f'Jour 1\n{trafic[0]} visites\n{revenu[0]} €', 
             xy=(trafic[0], revenu[0]), xytext=(trafic[0]-150, revenu[0]+500),
             arrowprops=dict(arrowstyle='->', color='gray', lw=1.5),
             fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))

ax2.annotate(f'Jour 10\n{trafic[-1]} visites\n{revenu[-1]} €', 
             xy=(trafic[-1], revenu[-1]), xytext=(trafic[-1]-200, revenu[-1]-600),
             arrowprops=dict(arrowstyle='->', color='gray', lw=1.5),
             fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.3))

ax2.set_title("Relation trafic/revenu avec ligne de tendance", fontsize=15, fontweight='bold', pad=15)
ax2.set_xlabel("Trafic (nombre de visites)", fontsize=12, fontweight='bold')
ax2.set_ylabel("Revenu (€)", fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.legend(loc='upper left', fontsize=10)

# Ajouter une barre de couleur pour indiquer les jours
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Jour', rotation=270, labelpad=20, fontsize=11, fontweight='bold')

plt.tight_layout()
plt.show()


# --- GRAPHIQUE 3 : Version avec taille variable des points ---
print("\n--- Version avec taille des points proportionnelle au revenu ---\n")

fig, ax = plt.subplots(figsize=(12, 8))

# Taille des points proportionnelle au revenu
tailles = [r/10 for r in revenu]  # Diviser par 10 pour des tailles raisonnables

scatter3 = ax.scatter(trafic, revenu, s=tailles, alpha=0.6, 
                      c=jours, cmap='viridis', edgecolors='black', linewidth=2)

# Ajouter les numéros de jour sur chaque point
for i, jour in enumerate(jours):
    ax.text(trafic[i], revenu[i], str(jour), 
            ha='center', va='center', fontsize=10, fontweight='bold', color='white')

ax.set_title("Trafic vs Revenu - Taille proportionnelle au CA", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Trafic (nombre de visites)", fontsize=13, fontweight='bold')
ax.set_ylabel("Revenu (€)", fontsize=13, fontweight='bold')
ax.grid(True, alpha=0.3, linestyle='--')

# Barre de couleur
cbar3 = plt.colorbar(scatter3, ax=ax)
cbar3.set_label('Jour', rotation=270, labelpad=20, fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()


# --- Calcul de la corrélation ---
correlation = np.corrcoef(trafic, revenu)[0, 1]

print("\n=== Analyse de la relation Trafic / Revenu ===")
print(f"Coefficient de corrélation : {correlation:.3f}")
print(f"Interprétation : ", end="")
if correlation > 0.9:
    print("Très forte corrélation positive ✓")
elif correlation > 0.7:
    print("Forte corrélation positive")
elif correlation > 0.5:
    print("Corrélation positive modérée")
else:
    print("Corrélation faible")

print(f"\nRevenu moyen par visite : {sum(revenu)/sum(trafic):.2f} €")
print(f"Évolution du trafic : +{((trafic[-1]-trafic[0])/trafic[0]*100):.1f}%")
print(f"Évolution du revenu : +{((revenu[-1]-revenu[0])/revenu[0]*100):.1f}%")