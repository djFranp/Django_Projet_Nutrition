# 🥗 Projet Django Nutrition — Kanban

> Mini cahier des charges — cards GitHub Projects par sprint

---

## 🗂️ Semaine 1 — Initialisation du projet

---

### 📌 Card : Setup du projet Django

**Description**
Initialiser le projet Django, configurer l'environnement et le dépôt Git.

**Tâches**
- [ ] Créer le projet Django (`django-admin startproject`)
- [ ] Configurer les statics et media dans `settings.py`
- [ ] Configurer la langue (`LANGUAGE_CODE = 'fr-fr'`)
- [ ] Installer et configurer `django-environ` (fichier `.env`)
- [ ] Ajouter l'URL media en mode `DEBUG=True`
- [ ] Ajouter un `.gitignore` adapté Django
- [ ] Générer le fichier `requirements.txt`
- [ ] Initialiser le dépôt Git et pousser sur GitHub

**Branche** : `setup/init-projet`

---

## 🗂️ Semaine 2 — Application Accounts

---

### 📌 Card : Modèle utilisateur custom

**Description**
Créer un modèle utilisateur personnalisé pour remplacer le `User` par défaut de Django.

**Tâches**
- [ ] Créer l'application `accounts`
- [ ] Définir le modèle `CustomUser` (hérite de `AbstractUser`)
- [ ] Ajouter `first_name` et `last_name` avec validateurs
- [ ] Déclarer `AUTH_USER_MODEL` dans `settings.py`
- [ ] Créer et appliquer les migrations
- [ ] Créer un superuser

**Branche** : `accounts/user-model`

---

### 📌 Card : Administration des comptes

**Description**
Configurer l'interface admin pour le modèle utilisateur custom.

**Tâches**
- [ ] Enregistrer `CustomUser` dans `admin.py`
- [ ] Personnaliser l'affichage (`list_display`, `search_fields`)
- [ ] Écrire les premiers tests unitaires
- [ ] Mettre en place la CI GitHub Actions (`.github/workflows/`)

**Branche** : `accounts/admin-et-tests`

---

## 🗂️ Semaine 3 — Template de base

---

### 📌 Card : Base template Bootstrap

**Description**
Mettre en place le template de base commun à toute l'application.

**Tâches**
- [ ] Ajouter le dossier `templates/` au `BASE_DIR` dans `settings.py`
- [ ] Créer `base.html` avec Bootstrap 5 (CDN)
- [ ] Intégrer la navbar et le bloc `content`
- [ ] Configurer le framework messages Django (`MESSAGE_TAGS`)
- [ ] Afficher les messages flash dans `base.html`

**Branche** : `core/base-template`

---

## 🗂️ Semaine 4 — Index & Authentification

---

### 📌 Card : Application core & page index

**Description**
Créer l'application `core` avec la page d'accueil du site.

**Tâches**
- [ ] Créer l'application `core`
- [ ] Déclarer `urls.py` et inclure dans le routeur principal
- [ ] Créer la `IndexView` (TemplateView)
- [ ] Créer le template `index.html` (hero, présentation)
- [ ] Inclure les urls de `core` et `accounts` dans `urls.py` principal

**Branche** : `core/index`

---

### 📌 Card : Signup & Login

**Description**
Permettre à un utilisateur de s'inscrire et de se connecter.

**Tâches**
- [ ] Installer et configurer `django-crispy-forms` + `crispy-bootstrap5`
- [ ] Créer le formulaire de signup (`UserCreationForm` custom)
- [ ] Créer la `SignupView` avec vérification par email
- [ ] Configurer l'envoi d'email (console backend en dev)
- [ ] Créer la `LoginView` (utiliser `django.contrib.auth`)
- [ ] Créer la `LogoutView`
- [ ] Créer le template `profile.html` (vue profil utilisateur)
- [ ] Écrire les tests pour signup

**Branche** : `accounts/signup-login`

---

### 📌 Card : Gestion des mots de passe

**Description**
Permettre le changement et la réinitialisation du mot de passe.

**Tâches**
- [ ] Vue et template `change_password`
- [ ] Vues et templates `password_reset` (4 étapes Django)
- [ ] Personnaliser l'email de reset
- [ ] Ajouter le lien "Mot de passe oublié ?" dans la page login
- [ ] Mettre à jour la navbar dans `base.html`
- [ ] Mettre à jour `requirements.txt` et les secrets CI

**Branche** : `accounts/gestion-mot-de-passe`

---

## 🗂️ Semaine 5 — Modèles & Admin Nutrition

---

### 📌 Card : Modèles de l'app Nutrition

**Description**
Créer les modèles de données pour les plats et les ingrédients.

**Tâches**
- [ ] Créer l'application `nutrition`
- [ ] Créer `choices.py` (ex : unités `g` / `pièce`)
- [ ] Créer le modèle `Ingredient` (nom, unité, calories…)
- [ ] Créer le modèle `Plate` (nom, utilisateur FK, ingrédients M2M via `PlateIngredient`)
- [ ] Créer le modèle intermédiaire `PlateIngredient` (quantité)
- [ ] Créer et appliquer les migrations
- [ ] Écrire les tests unitaires des modèles

**Branche** : `nutrition/modeles`

---

### 📌 Card : Administration Nutrition

**Description**
Configurer l'interface admin pour les modèles nutrition.

**Tâches**
- [ ] Enregistrer `Ingredient`, `Plate`, `PlateIngredient` dans `admin.py`
- [ ] Ajouter un `InlineModelAdmin` pour les ingrédients d'un plat
- [ ] Personnaliser `list_display` et `search_fields`

**Branche** : `nutrition/admin`

---

## 🗂️ Semaine 6 — Vues Nutrition (lecture & suppression)

---

### 📌 Card : Liste des plats (ListView + HTMX)

**Description**
Afficher la liste des plats de l'utilisateur connecté avec recherche HTMX.

**Tâches**
- [ ] Créer `PlateListView` avec `queryset` filtré sur `request.user`
- [ ] Utiliser `select_related` / `prefetch_related` pour optimiser
- [ ] Créer le template `user_plates.html` + partial `plate_list.html`
- [ ] Ajouter la méthode `display_unit` sur le modèle
- [ ] Intégrer HTMX pour la recherche en temps réel
- [ ] Écrire les tests de la ListView

**Branche** : `nutrition/list-view`

---

### 📌 Card : Détail d'un plat (DetailView)

**Description**
Afficher le détail d'un plat avec ses ingrédients.

**Tâches**
- [ ] Créer `PlateDetailView`
- [ ] Définir `get_absolute_url` sur le modèle `Plate`
- [ ] Créer le template `plate_detail.html` (ingrédients, quantités)
- [ ] Écrire les tests de la DetailView

**Branche** : `nutrition/detail-view`

---

### 📌 Card : Créer & Supprimer un plat

**Description**
Permettre à l'utilisateur de créer et supprimer ses plats.

**Tâches**
- [ ] Créer `PlateCreateView` (formulaire avec le nom du plat)
- [ ] Rediriger vers `get_absolute_url` après création
- [ ] Ajouter le lien "Créer un plat" dans `user_plates.html` et `plate_list.html`
- [ ] Créer `PlateDeleteView` avec confirmation
- [ ] Restreindre la suppression au propriétaire du plat
- [ ] Écrire les tests CreateView et DeleteView

**Branche** : `nutrition/create-delete`

---

## 🗂️ Semaine 7 — Update plat (HTMX + Formset)

---

### 📌 Card : Update plat avec HTMX et formset

**Description**
Page d'édition d'un plat : ajout/retrait d'ingrédients via HTMX, modification des quantités via formset.

**Tâches**
- [ ] Créer les formulaires (`PlateForm`, `PlateIngredientFormSet`)
- [ ] Créer `PlateUpdateView` et son URL
- [ ] Créer les templates `update_plate.html` et `ingredient_formset.html`
- [ ] Vérifier que l'update basique fonctionne avant d'ajouter HTMX
- [ ] Créer la vue de recherche d'ingrédients + URL
- [ ] Créer le partial `ingredient_search_results.html`
- [ ] Brancher HTMX (`hx-get` sur le champ de recherche → `#search-results`)
- [ ] Créer la vue `add_ingredient` (POST, ajoute avec quantité 100 par défaut)
- [ ] Brancher HTMX (`hx-post` sur le bouton Ajouter → refresh du formset)
- [ ] Utiliser `request.GET.getlist(...)` pour récupérer les IDs multiples
- [ ] Interdire la modification de l'ingrédient dans le formset (champ en lecture seule)

**Branche** : `nutrition/update-htmx-formset`

---

## 🗂️ Bonus (si le temps le permet)

---

### 📌 Card : Signaux Django

**Description**
Utiliser les signaux pour automatiser des actions lors d'événements modèles.

**Tâches**
- [ ] Créer un signal `post_save` (ex : email de bienvenue à l'inscription)
- [ ] Connecter le signal dans `apps.py` (`ready()`)

**Branche** : `bonus/signals`

---

### 📌 Card : Tâches asynchrones avec Celery

**Description**
Mettre en place Celery + Redis pour les tâches de fond.

**Tâches**
- [ ] Installer `celery` et `redis`
- [ ] Configurer Celery dans le projet Django
- [ ] Créer une tâche simple (ex : envoi d'email asynchrone)
- [ ] Tester avec `celery worker`

**Branche** : `bonus/celery`

---

### 📌 Card : django-allauth

**Description**
Remplacer le système d'auth custom par django-allauth.

**Tâches**
- [ ] Installer et configurer `django-allauth`
- [ ] Migrer signup / login / logout vers allauth
- [ ] Configurer un provider social si souhaité (Google)

**Branche** : `bonus/allauth`

---

## 📊 Récapitulatif des branches

| Branche | Semaine | Contenu |
|---|---|---|
| `setup/init-projet` | 1 | Init Django, settings, git |
| `accounts/user-model` | 2 | CustomUser, migrations |
| `accounts/admin-et-tests` | 2 | Admin, CI |
| `core/base-template` | 3 | base.html, Bootstrap, messages |
| `core/index` | 4 | App core, page accueil |
| `accounts/signup-login` | 4 | Signup, login, logout, profil |
| `accounts/gestion-mot-de-passe` | 4 | Change/reset password |
| `nutrition/modeles` | 5 | Ingredient, Plate, PlateIngredient |
| `nutrition/admin` | 5 | Admin nutrition |
| `nutrition/list-view` | 6 | ListView + HTMX search |
| `nutrition/detail-view` | 6 | DetailView |
| `nutrition/create-delete` | 6 | CreateView, DeleteView |
| `nutrition/update-htmx-formset` | 7 | UpdateView + HTMX + formset |
| `bonus/signals` | — | Signaux Django |
| `bonus/celery` | — | Celery + Redis |
| `bonus/allauth` | — | django-allauth |
