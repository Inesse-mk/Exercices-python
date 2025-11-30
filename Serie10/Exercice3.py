import requests
from collections import defaultdict

def recuperer_posts():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        if response.status_code == 200:
            return response.json()
        else:
            print("Erreur HTTP :", response.status_code)
            return []
    except requests.RequestException as e:
        print("Erreur réseau :", e)
        return []

def calculer_stats_par_user(posts):
    stats = defaultdict(lambda: {"nb_posts": 0, "total_titres": 0})
    
    for post in posts:
        user_id = post['userId']
        stats[user_id]["nb_posts"] += 1
        stats[user_id]["total_titres"] += len(post['title'])
    
    # Calculer la moyenne directement
    for user_id in stats:
        stats[user_id]["longueur_moyenne_titre"] = stats[user_id]["total_titres"] / stats[user_id]["nb_posts"]
        del stats[user_id]["total_titres"]  # on supprime la clé temporaire
    
    return stats

def afficher_top_users(stats, top_n=3):
    # Trier par nb_posts décroissant
    for user_id, s in sorted(stats.items(), key=lambda x: x[1]["nb_posts"], reverse=True)[:top_n]:
        print(f"User {user_id} : {s['nb_posts']} posts (longueur moyenne titre : {s['longueur_moyenne_titre']:.1f})")

# Bloc principal
posts = recuperer_posts()
stats = calculer_stats_par_user(posts)
afficher_top_users(stats)
