# Documentation des commandes — Gestion des Clients

Ce document décrit les commandes utiles pour installer, lancer et maintenir l'application Django.

---

## Prérequis

- **Python 3.10+** installé sur la machine
- Accès au terminal (PowerShell, CMD ou terminal intégré)

Vérifier Python et Django :

```powershell
python --version
python -m django --version
```

---

## 1. Installation des dépendances

Se placer dans le dossier du projet :

```powershell
cd C:\Users\T14S\Desktop\django_tp
```

Installer Django (si ce n'est pas déjà fait) :

```powershell
python -m pip install -r requirements.txt
```

Ou directement :

```powershell
python -m pip install Django
```

---

## 2. Création du projet (référence — déjà fait)

Ces commandes ont servi à initialiser le projet. Vous n'avez pas besoin de les relancer sauf pour un nouveau projet.

| Commande | Description |
|----------|-------------|
| `python -m django startproject gestion_clients .` | Crée le projet Django `gestion_clients` dans le dossier courant |
| `python manage.py startapp clients` | Crée l'application `clients` |

---

## 3. Base de données (migrations)

Après toute modification du fichier `clients/models.py`, exécuter :

```powershell
python manage.py makemigrations
```

Appliquer les migrations à la base SQLite :

```powershell
python manage.py migrate
```

Cela crée ou met à jour le fichier `db.sqlite3` à la racine du projet.

---

## 4. Lancer le serveur de développement

```powershell
python manage.py runserver
```

L'application est accessible à l'adresse : **http://127.0.0.1:8000/**

Pour utiliser un autre port (ex. 8080) :

```powershell
python manage.py runserver 8080
```

Arrêter le serveur : `Ctrl + C` dans le terminal.

---

## 5. Interface d'administration Django (optionnel)

Créer un compte administrateur :

```powershell
python manage.py createsuperuser
```

Lancer le serveur puis ouvrir : **http://127.0.0.1:8000/admin/**

Les clients y sont aussi gérables via l'interface admin.

---

## 6. Commandes utiles de maintenance

| Commande | Utilité |
|----------|---------|
| `python manage.py check` | Vérifie la configuration du projet |
| `python manage.py showmigrations` | Liste l'état des migrations |
| `python manage.py shell` | Ouvre un shell Python avec Django chargé |
| `python manage.py flush` | Vide la base (demande confirmation) |

Exemple dans le shell pour lister les clients :

```python
from clients.models import Client
Client.objects.all()
```

---

## 7. Structure des URLs de l'application

| URL | Page |
|-----|------|
| `/` | Liste des clients (+ recherche par nom) |
| `/ajouter/` | Formulaire d'ajout |
| `/&lt;id&gt;/modifier/` | Formulaire de modification |
| `/&lt;id&gt;/supprimer/` | Confirmation de suppression |

---

## 8. Résumé — démarrage rapide

```powershell
cd C:\Users\T14S\Desktop\django_tp
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Puis ouvrir **http://127.0.0.1:8000/** dans le navigateur.

---

## 9. Dépannage courant

| Problème | Solution |
|----------|----------|
| `django-admin` introuvable | Utiliser `python -m django` à la place |
| Erreur « No module named django » | `python -m pip install Django` |
| Table inexistante | `python manage.py migrate` |
| Modifications du modèle ignorées | `makemigrations` puis `migrate` |
| Fichiers statiques non chargés | Vérifier `STATICFILES_DIRS` dans `settings.py` |
