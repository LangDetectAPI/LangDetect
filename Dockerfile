# image de base Python 3.10
FROM python:3.10-slim

# le répertoire de travail dans le conteneur.
WORKDIR /app

# les fichiers de dépendances 
COPY requirements.txt .

# Installez les dépendances.
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le reste de votre code d'application dans le conteneur.
COPY . .

# Exposez le port sur lequel votre application Flask s'exécute.
EXPOSE 5080

# Définissez les variables d'environnement pour Flask.
ENV FLASK_APP=src/api/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5080

# Exécutez l'application Flask.
CMD ["flask", "run"]
