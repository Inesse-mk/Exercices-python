import requests
# Fonction pour récupérer les posts depuis l'API
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
# Fonction pour afficher un résumé des premiers posts
def afficher_resume_posts(posts, n=5):
    for post in posts[:n]:
        print(f"Post #{post['id']} (user {post['userId']}) : {post['title']}")

# Récupération des posts
posts = recuperer_posts()
print(f"Nombre total de posts récupérés : {len(posts)}")
# Affichage des 5 premiers posts
afficher_resume_posts(posts, n=5)

