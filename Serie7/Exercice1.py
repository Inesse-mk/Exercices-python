import matplotlib.pyplot as plt

# 1. Données sous forme de listes
jours = [1, 2, 3, 4, 5, 6, 7]
trafic = [1200, 1350, 900, 1500, 1700, 1600, 1800]

# 2. Créer une figure avec 2 sous-graphiques pour comparer les marqueurs
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Premier graphique avec marker="o" (rond)
ax1.plot(jours, trafic, marker="o", linewidth=2, markersize=8, color='#2E86AB')
ax1.set_title("Trafic du site sur 7 jours (marqueur rond)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Jour", fontsize=12)
ax1.set_ylabel("Nombre de visites", fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.set_xticks(jours)

# Second graphique avec marker="s" (carré) - BONUS
ax2.plot(jours, trafic, marker="s", linewidth=2, markersize=8, color='#A23B72')
ax2.set_title("Trafic du site sur 7 jours (marqueur carré)", fontsize=14, fontweight='bold')
ax2.set_xlabel("Jour", fontsize=12)
ax2.set_ylabel("Nombre de visites", fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.set_xticks(jours)

# Ajuster l'espacement entre les graphiques
plt.tight_layout()
plt.show()

# Version simple (graphique unique)
print("\n--- Version graphique unique ---\n")
plt.figure(figsize=(10, 6))
plt.plot(jours, trafic, marker="o", linewidth=2, markersize=8, color='#2E86AB')
plt.title("Trafic du site sur 7 jours", fontsize=14, fontweight='bold')
plt.xlabel("Jour", fontsize=12)
plt.ylabel("Nombre de visites", fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(jours)
plt.show()
