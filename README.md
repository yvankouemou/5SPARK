# 5SPARK
creer un dossier kafka-zookeeper en local

creer dans ce dossier un docker-compose.yml qui compose le kafka et zookeeper à installer

Dans linvite de commande acceder au dossier et lancer le docker-compose (docker-compose up -d)

verifier que limage a bien été crée (docker-compose ps)

Acceder à linterface kafka (docker exec -it "nom ou id du conteneur" bash)

Creer le topic (kafka-topics.sh --create --topic mastodon_stream --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1)

verifier la creation(kafka-topics.sh --list --bootstrap-server kafka:9092)