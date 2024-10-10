# 5SPARK
PROJECT 5SPARK

Réalisé par :
Raynald AKOTEGNON
Yvan KOUEMOU
Daïla MAFOGAING


The project comprises 3 key stages:

STEP 1: creation of the mastodon application
- Create an account on https://mastodon.social
- Create an application
- Retrieve the following elements:
Client ID: zpKnUj8gbpTjVf8b72lIRTkuQ5xix8B445-q-E8JtEs
Client Secret: c-bU98x_9kFr93LPSNPOJTKNqNWP5WcuYkYCMDeHvPI
Access Token: 4_AxEF5KWVycxBtq4vd09yw3iEo2vTOTcbirkQ06-PY


STEP2: Data ingestion
- Creation of an ingestion file mastodon_kafka_stream.py, which will be used to collect data from the mastodon API and insert it into our Topic Kafka, which we will then deploy.
- Creation of a Dockerfile to optimize loading of the libraries required for our files (ingestion file and docker-compose).
- Creation of a docker_compose file to deploy the following images: zookeeper, Kafka, spark, jupyter , dockerfile and postgres
- Execute commands in bash :
o	docker-compose build
o	docker-compose up -d
o	python mastodon_kafka_stream.py (let the data load)

STEP3: Data extraction, processing, loading and visualization on Jupyter
We did all this through the following files:
- Transformation(part1 & 2).ipynb
- Batch processing(part3).ipynb
- sentiment analysis(part4).ipynb
- visualization(part5).ipynb
