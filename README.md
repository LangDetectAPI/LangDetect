# LangDetect API

LangDetect API est une API Flask qui utilise un modèle d'apprentissage profond (`langDetect shallow model`) pour détecter la langue d'un texte donné. Elle prend en charge plusieurs langues et est conçue pour être facilement déployée dans un conteneur Docker, rendant son intégration simple et efficace pour toute application nécessitant des capacités de détection de langue.

## Fonctionnalités Clés

- **Détection de langue précise** : Utilise un modèle d'apprentissage profond pour identifier la langue d'un texte avec une haute précision.
- **Support multilingue** : Capable de reconnaître de nombreuses langues, offrant une utilité globale.
- **Facile à déployer** : Conçu avec Docker en tête pour une mise en production et un déploiement aisés.

## Prérequis

- Docker
- (Optionnel) Python 3.10 pour une exécution locale sans Docker.

## Installation

### Utilisation de Docker

1. **Construire l'image Docker** :

   Clonez le dépôt, naviguez jusqu'au répertoire racine du projet et construisez l'image Docker en exécutant :

   ```bash
   docker build -t langdetector:latest .
   ```

2. **Démarrer un conteneur Docker** :

   Lancez votre API en utilisant :

   ```bash
   docker run -d -p 5080:5080 langdetector:latest
   ```

   Votre API est maintenant accessible à `http://localhost:5080`.

### Exécution Locale (Optionnelle)

Pour exécuter l'API localement, vous devez avoir Python 3.10 et les dépendances installées :

1. **Installer les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

2. **Lancer l'application** :

   ```bash
   python src/api/app.py
   ```

## Utilisation de l'API

- **Obtenir la liste des langues supportées** :

  Envoyez une requête GET à `/api/v1/` pour recevoir une réponse JSON des langues disponibles.

  ```bash
    curl -X GET http://localhost:5080/api/v1/
  ```

- **Détecter la langue d'un texte** :

  Envoyez une requête POST à `/api/v1/detect` avec un payload JSON contenant le texte à analyser :

  ```bash
    curl -X POST http://localhost:5080/api/v1/detect \
     -H "Content-Type: application/json" \
     -d '{"text": "This is a test sentence to detect the language."}'
  ```

  La réponse inclura la langue détectée ainsi que la probabilité de cette prédiction.

## Contribuer

Les contributions sont les bienvenues ! Si vous avez des suggestions d'amélioration, des corrections de bugs, ou souhaitez ajouter de nouvelles fonctionnalités, n'hésitez pas à créer une issue ou soumettre une pull request.

## Licence

Ce projet est distribué sous la licence MIT. Consultez le fichier `LICENSE` pour plus de détails.
