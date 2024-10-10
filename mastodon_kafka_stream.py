import os
import time
import logging
from mastodon import Mastodon
from confluent_kafka import Producer
import json
from bs4 import BeautifulSoup

# Configuration du logging
logging.basicConfig(level=logging.INFO)

# Connexion à l'API Mastodon
mastodon = Mastodon(
    client_id='zpKnUj8gbpTjVf8b72lIRTkuQ5xix8B445-q-E8JtEs',  
    client_secret='c-bU98x_9kFr93LPSNPOJTKNqNWP5WcuYkYCMDeHvPI',
    access_token='4_AxEF5KWVycxBtq4vd09yw3iEo2vTOTcbirkQ06-PY',
    api_base_url='https://mastodon.social'
)

# Configuration du producteur Kafka
producer = Producer({'bootstrap.servers': 'localhost:9092'})

#Fonction pour vérifier si un hashtag contient "AI" et "datascience"
def contains_ai(hashtag_list):
    relevant_hashtags = ['ai', 'datascience']
    # Vérifie si l'un des hashtags dans le toot correspond à 'AI' ou 'DataScience' (insensible à la casse)
    return any(tag['name'].lower() in relevant_hashtags for tag in hashtag_list)

# Fonction pour récupérer et envoyer les toots dans Kafka
def fetch_and_send_toots():
    try:
        toots = mastodon.timeline_public(limit=5)
        if not toots:
            logging.info("Aucun toot trouvé.")
        
        for toot in toots:
            # Filtrer les toots avec des hashtags contenant "AI"
            if contains_ai(toot['tags']):

                cleaned_content = BeautifulSoup(toot['content'], "html.parser").get_text()

                structured_toot = {
                    'id': toot['id'],
                    'user': toot['account']['username'],
                    'user_id': toot['account']['id'],
                    'followers_count': toot['account']['followers_count'],
                    'timestamp': toot['created_at'].isoformat(),
                    'content': cleaned_content,
                    'language': toot['language'],
                    'hashtags': [tag['name'] for tag in toot['tags']],
                    'favourites_count': toot['favourites_count'],
                    'reblogs_count': toot['reblogs_count']
                }
                producer.produce('message_kafka', json.dumps(structured_toot).encode('utf-8'))
                logging.info(f"Toot publié : {structured_toot['content']}")
        
        producer.flush()  # Assure que les messages sont envoyés

    except Exception as e:
        logging.error(f"Erreur ou limite de débit atteinte : {e}")
        time.sleep(60)  # Attendre 1 minute avant de réessayer

# Boucle pour récupérer et envoyer les toots en continu
if __name__ == "__main__":
    while True:
        fetch_and_send_toots()
        time.sleep(2)  # Délai entre chaque appel à l'API (2 secondes)
