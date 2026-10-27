# E-CREDIT

API REST de gestion de crédit construite avec Django et Django REST Framework. Elle expose des opérations CRUD pour les clients, les comptes, les agents, les demandes de crédit, les remboursements et les transactions.

> **Description courte :** API REST Django pour gérer les clients, les comptes bancaires, les agents, les demandes de crédit, les remboursements et les transactions.

## Technologies

- Python
- Django 6.1.2
- Django REST Framework 3.18.3
- SQLite (configuration locale par défaut)

## Installation locale

Depuis le dossier contenant `manage.py` :

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Le serveur de développement sera disponible à l’adresse `http://127.0.0.1:8000/`.

## Endpoints API

Les routes sont préfixées par `/api/core/` :

| Ressource | Endpoint |
|---|---|
| Clients | `/api/core/clients/` |
| Comptes | `/api/core/comptes/` |
| Agents | `/api/core/agents/` |
| Demandes de crédit | `/api/core/demandes-credit/` |
| Remboursements | `/api/core/remboursements/` |
| Transactions | `/api/core/transactions/` |

Chaque ressource utilise un `ModelViewSet` et prend en charge les opérations CRUD fournies par Django REST Framework.

## Administration

L’administration Django est accessible à `http://127.0.0.1:8000/admin/`. Créez un compte administrateur avec :

```powershell
python manage.py createsuperuser
```

## Configuration et sécurité

La base SQLite locale et les fichiers d’environnement ne sont pas suivis par Git. Pour un déploiement, définissez une variable d’environnement `DJANGO_SECRET_KEY` avec une clé secrète privée et configurez `DEBUG` et `ALLOWED_HOSTS` selon l’environnement. Le serveur `runserver` est réservé au développement.
