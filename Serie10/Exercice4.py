import requests

class JsonPlaceholderClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def _get(self, endpoint, timeout=5):
        """Méthode interne pour faire un GET avec gestion des erreurs"""
        url = self.base_url + endpoint
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()  
            return response.json()
        except requests.RequestException as e:
            print(f"Erreur réseau ou HTTP pour {url} : {e}")
            return None

    def get_posts(self):
        """Retourne la liste des posts"""
        return self._get("/posts") or []

    def get_post(self, post_id):
        """Retourne un post unique par ID"""
        return self._get(f"/posts/{post_id}")

# Bloc principal
if __name__ == "__main__":
    client = JsonPlaceholderClient()
    
    posts = client.get_posts()
    print(f"Nombre total de posts : {len(posts)}")

    post_1 = client.get_post(1)
    if post_1:
        print(f"\nPost #1 : {post_1['title']}\n{post_1['body']}")
