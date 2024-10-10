# Définition de l'image Spark
FROM bitnami/spark:latest

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le script Python mastodon_kafka_stream.py dans le conteneur
COPY mastodon_kafka_stream.py .

# Installer les dépendances nécessaires
RUN pip install --no-cache-dir mastodon.py confluent_kafka beautifulsoup4 pyspark[sql,kafka] psycopg2-binary

# Commande par défaut pour lancer Spark avec le script Python
CMD ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0,org.apache.kafka:kafka-clients:2.7.0", "mastodon_kafka_stream.py"]
