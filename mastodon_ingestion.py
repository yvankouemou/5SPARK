from mastodon import Mastodon, StreamListener
from kafka import KafkaProducer
import json

# Authentification Mastodon
mastodon = Mastodon(
    access_token='o9PA-jEzoPJxm5EM0TxRreGi5QCkUBbzG5it8tT9Qe0',
    api_base_url='https://mastodon.social'
)

# Configuration du producteur Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Listener pour recevoir les toots en temps réel
class TootListener(StreamListener):
    def on_update(self, status):
        toot_data = {
            'id': status['id'],
            'content': status['content'],
            'created_at': status['created_at'].isoformat(),  # Convert to string
            'account': status['account']['username'],
            'hashtags': [tag['name'] for tag in status['tags']]
        }
        print(f"Toot reçu : {toot_data}")
        producer.send('mastodon_stream', value=toot_data)

# Démarrer la capture des toots
mastodon.stream_public(TootListener())
