# Application Cantine

Cette application de gestion de cantine permet d'afficher et de manipuler des menus et des plats de manière dynamique, en utilisant Django et une base de données MySQL.

## Fonctionnalités principales
- Gestion des **menus** et des **plats**.
- Affichage dynamique des données en fonction des informations stockées dans la base de données MySQL.
- Interface utilisateur adaptée avec un template HTML intégré.

Créer et activer un environnement virtuel :
python -m venv env
source env/bin/activate  
Sur Windows, utilisez env\Scripts\activate
Installer les dépendances :
pip install -r requirements.txt
Configurer la base de données MySQL :

Créez une base de données nommée cantine_db dans MySQL :
CREATE DATABASE cantine_db;
Mettez à jour vos informations de connexion MySQL dans le fichier settings.py :
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cantine_db',
        'USER': 'root',
        'PASSWORD': 'password',  # Changez-le si nécessaire
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Appliquer les migrations pour créer les tables :
python manage.py makemigrations
python manage.py migrate
Charger les données initiales ou créer des menus et des plats via l'interface d'administration :

Pour accéder à l'admin Django :
python manage.py createsuperuser
python manage.py runserver
