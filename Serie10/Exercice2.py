import requests

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

def afficher_resume_posts(posts, n=5):
    for post in posts[:n]:
        print(f"Post #{post['id']} (user {post['userId']}) : {post['title']}")


posts = recuperer_posts()
print(f"Nombre total de posts récupérés : {len(posts)}")
afficher_resume_posts(posts, n=5)
