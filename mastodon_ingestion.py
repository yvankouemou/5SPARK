import os
import time
import logging
from mastodon import Mastodon, StreamListener
from confluent_kafka import Producer
import json
from bs4 import BeautifulSoup

# Configuration du logging
logging.basicConfig(level=logging.INFO)

# Connexion à l'API Mastodon
mastodon = Mastodon(
    access_token='o9PA-jEzoPJxm5EM0TxRreGi5QCkUBbzG5it8tT9Qe0',
    api_base_url='https://mastodon.social'
)

# Configuration du producteur Kafka
try:
    producer = Producer({'bootstrap.servers': 'kafka:9092'})  # Changer localhost par kafka si c'est un conteneur
except Exception as e:
    logging.error(f"Erreur de connexion au producteur Kafka : {e}")
    exit(1)

# Listener pour recevoir les toots en temps réel
class TootListener(StreamListener):
    def on_update(self, status):
        try:
            cleaned_content = BeautifulSoup(status['content'], "html.parser").get_text()

            toot_data = {
                'id': status['id'],
                'content': cleaned_content,
                'created_at': status['created_at'].isoformat(),
                'account': status['account']['username'],
                'hashtags': [tag['name'] for tag in status['tags']],
                'favourites_count': status['favourites_count'],
                'reblogs_count': status['reblogs_count']
            }

            # Envoie des données dans le topic Kafka 'mastodon_stream'
            producer.produce('mastodon_stream', value=json.dumps(toot_data).encode('utf-8'))

            logging.info(f"Toot reçu et publié : {toot_data['content']}")

        except Exception as e:
            logging.error(f"Erreur lors du traitement du toot : {e}")

# Démarrer la capture des toots en temps réel
if __name__ == "__main__":
    while True:
        try:
            mastodon.stream_public(TootListener())
        except Exception as e:
            logging.error(f"Erreur ou interruption de la connexion : {e}")
            time.sleep(60)  # Attendre avant de réessayer
