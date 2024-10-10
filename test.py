import json
from mastodon import Mastodon, StreamListener
import logging

#ce fichier permet de connaitre toute les colonnes de notre API mastodon

# Configurer le journal pour capturer les erreurs et les informations
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurer Mastodon avec les identifiants de l'application
mastodon = Mastodon(
    client_id='zpKnUj8gbpTjVf8b72lIRTkuQ5xix8B445-q-E8JtEs',
    client_secret='c-bU98x_9kFr93LPSNPOJTKNqNWP5WcuYkYCMDeHvPI',
    access_token='4_AxEF5KWVycxBtq4vd09yw3iEo2vTOTcbirkQ06-PY',
    api_base_url='https://mastodon.social'
)


# Créer une classe StreamListener pour écouter les toots en temps réel
class TootStreamListener(StreamListener):

    def contains_ai(self, hashtag_list):
        relevant_hashtags = ['ai', 'datascience']
        # Vérifie si l'un des hashtags dans le toot correspond à 'AI' ou 'DataScience' (insensible à la casse)
        return any(tag['name'].lower() in relevant_hashtags for tag in hashtag_list)

    def on_update(self, toot):
        try:
            if self.contains_ai(toot['tags']):  # Appel à la méthode d'instance
                # Afficher les données brutes du toot en console
                print(json.dumps(toot, ensure_ascii=False, default=str))
                logger.info("Toot brut affiché en console.")
        except Exception as e:
            logger.error(f"Erreur lors de l'affichage du toot: {e}")


# Démarrer le streaming public pour écouter les toots en temps réel
listener = TootStreamListener()
mastodon.stream_public(listener)