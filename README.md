# 5SPARK
creer un dossier kafka-zookeeper en local

creer dans ce dossier un docker-compose.yml qui compose le kafka et zookeeper à installer

Dans linvite de commande acceder au dossier et lancer le docker-compose (docker-compose up -d)

verifier que limage a bien été crée (docker-compose ps)

Acceder à linterface kafka (docker exec -it "nom ou id du conteneur" bash)

Creer le topic (kafka-topics.sh --create --topic mastodon_stream --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1)

verifier la creation(kafka-topics.sh --list --bootstrap-server kafka:9092)

Ensuite jai crée mon fichier mastodon-ingestion.py

Puis jai upgrade ma librairie mastodon.py dans mon terminal (pip install mastodon.py --upgrade)

puis jai lancé mon fichier mastodon-ingestion.py

ensuite installer les dependances spark pour kafka(pip install pyspark
pip install kafka-python)

creer un jupyter notebook(docker run -p 8888:8888 -p 4040-4045:4040-4045 jupyter/pyspark-notebook) puis le run

Trouver son token pour louvrir dans le navigateur(docker exec -it CONTAINER_ID jupyter notebook list)

Dans ton Jupyter Notebook, commence par importer les bibliothèques nécessaires et configurer PySpark pour se connecter à Kafka 

Définis le schéma qui correspond à la structure des toots que tu as envoyés à Kafka dans ton code d'ingestion.

Tu vas maintenant configurer Spark Structured Streaming pour consommer les messages Kafka envoyés par ton script Mastodon 

À ce stade, tu peux commencer à effectuer des transformations sur les données en flux. Par exemple, tu peux filtrer les toots en fonction de certains mots-clés ou hashtags :