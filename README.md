# Gestion des Clients — Mini-projet Django

Application web développée avec **Django** pour une agence commerciale. Elle permet de gérer une base de clients via une interface simple et intuitive.

## Description

Ce projet répond à un cahier des charges de mini-projet web : enregistrer des clients en base de données, les afficher dans un tableau, les modifier, les supprimer et les filtrer par nom. Les formulaires sont validés (champs obligatoires) et des messages de confirmation s’affichent après chaque ajout ou suppression.

## Fonctionnalités

- Ajout d’un client via un formulaire validé
- Liste des clients sous forme de tableau
- Modification des informations d’un client
- Suppression avec page de confirmation
- Recherche / filtre par nom
- Messages de confirmation (framework Messages de Django)
- Navigation entre les pages
- Interface responsive et moderne

## Technologies

- Python 3.10+
- Django 6.x
- SQLite
- HTML / CSS (templates Django)

## Installation

```bash
git clone https://github.com/abdessamadben12/-Gestion-des-Clients-Mini-projet-Django.git
cd -Gestion-des-Clients-Mini-projet-Django
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Ouvrir dans le navigateur : **http://127.0.0.1:8000/**

## Structure du projet

```
django_tp/
├── gestion_clients/     # Configuration du projet Django
├── clients/             # Application (modèles, vues, formulaires, templates)
├── static/css/          # Feuille de style
├── DOCUMENTATION_COMMANDES.md
├── DOCUMENTATION_CODE.md
└── manage.py
```

## Documentation

| Fichier | Contenu |
|---------|---------|
| [DOCUMENTATION_COMMANDES.md](DOCUMENTATION_COMMANDES.md) | Commandes Django (migrations, serveur, admin…) |
| [DOCUMENTATION_CODE.md](DOCUMENTATION_CODE.md) | Explication de l’architecture et du code |

## Auteur

Mini-projet réalisé dans le cadre d’un cours de développement web avec Django.

## Licence

Projet à usage pédagogique.
