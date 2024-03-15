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

### Exécution Locale avec un Environnement Virtuel

Pour exécuter l'API LangDetect localement, il est recommandé d'utiliser un environnement virtuel Python. Cela garantit que les dépendances du projet sont gérées séparément, évitant ainsi tout conflit avec d'autres projets ou avec les packages systèmes.

1. **Installer Python 3.10** :

   Assurez-vous que Python 3.10 est installé sur votre machine. Vous pouvez vérifier cela en exécutant `python3 --version` dans votre terminal.

2. **Créer un environnement virtuel** :

   Naviguez jusqu'au répertoire racine de votre projet, puis exécutez la commande suivante pour créer un environnement virtuel :

   ```bash
   python3 -m venv .venv
   ```

   Ceci crée un nouvel environnement virtuel dans un dossier `.venv` situé à la racine de votre projet.

3. **Activer l'environnement virtuel** :

   Pour activer l'environnement virtuel, exécutez :

   - Sur Windows :
   
     ```bash
     .venv\Scripts\activate
     ```
   
   - Sur macOS et Linux :
   
     ```bash
     source .venv/bin/activate
     ```

   Une fois activé, votre invite de commande indiquera que vous travaillez actuellement dans l'environnement virtuel.

4. **Installer les dépendances** :

   Avec l'environnement virtuel activé, installez les dépendances requises en exécutant :

   ```bash
   pip install -r requirements.txt
   ```

5. **Lancer l'application** :

   Ensuite, démarrez l'application Flask en utilisant :

   ```bash
   flask run --port=5080
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
