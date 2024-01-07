Sur vim:

u(undo) pour retour en arrière <br>
y pour copier <br>
yy pour coppier la ligne <br>
p pour coller <br>
d pour couper <br>
dd pour couper la ligne <br>

# Lignes de commande

Installer django:

```sh
pip install django
```

Connaître la version d'un module:

```sh
python -m django --version
```

Trouver de l'aide sur django

```sh
jango-admin --help
```

Créer l'arborescence de base d'un projet Django:

```bash
django-admin startproject nom_projet
```
Pour créer une application:

```bash
python3 manage.py startapp nom_app
```

Pour démarrer le serveur sur un port est de se positionner dans src:

```sh
python manage.py runserver port
```

Pour créer un super-utilisateur:

```sh
python manage.py createsuperuser
```

La ligne de commande proposera d'y inscrire un nom d'utilisateur, une adresse mail et un mot de passe.

On crée un fichier views.py avec les fichiers settings.py etc pour les vues.
Pour faire le lien entre urls.py et views.py dans urls.py par urlpatterns:

# settings.py

Le fichier settings.py contient les paramètres du projet. Il est important de le configurer correctement sous peine d'avoir des problèmes de chemin. Il faut faire attention à la syntaxe. 

BASE_DIR est le chemin du dossier src.

DEBUG est un booléen qui permet de savoir si on est en mode debug ou non. Il est à True par défaut. Il faut le mettre à False en production.

INSTALLED_APPS est une liste contenant toutes les applications que Django doit utilisé. Il faut ajouter les applications que l'on crée à l'intérieur.

TEMPLATES est une liste contenant les options des templates. Il faut ajouter le chemin du dossier templates du projet.

Root_urlconf est le chemin du fichier urls.py du projet à partir du dossier src. Ce fichier est le point d'entrée par lequel Django va effectuer la résolution des urls.

AUTH_USER_MODEL est le modèle utilisateur que Django va utiliser. nom_app.nom_model

AUTHENTICATION_BACKENDS est le module d'authentification que Django va utiliser. C'est utilse pour pouvoir customiser l'authentification.

STATIC_URL est le nom du dossier static. Il est à /static/ par défaut. Cela signifie que Django va chercher tous les dossiers static/ dans les applications.

STATICFILES_DIRS est une liste de tous les chemins des dossiers static. Il faut ajouter le chemin du dossier static du projet.

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'. Ce modèle ajoute un champ id par défaut à tous les modèles.

## Templates/statics

Pour faire le lien entre le fichier html et le fichier css, il faut ajouter la ligne suivante au début du fichier html pour indiquer que l'on utilise le système du dossier static:

```python
{% load static %}
```

Puis, on indique de manière propre le chemin à partir du dossier static:

```html
href = "{% static 'css/style.css}"
```

Mais Django chercher le premier dossier static qu'il trouve. En indiquant le même lien, chaque html aura la même feuille de style. On fait donc d'une autre manière pour différencier les fichiers statics.

```html
href = "{% static 'nom_app/css/style.css %}
```

Le même problème se pose pour les dossiers templates. On résout le problème de la même manière. On place un dossier avec le nom de l'application en dessous du dossier templates. 

Le chemin à partir de src pour un fichier html:

```
nom_app/templates/nom_app/html/index.html
```

Le chemin à partir de src pour un fichier static:

```
nom_app/static/nom_app/static/css/style.css
```

# urls.py

Le fichier urls.py permet de router les urls. Dans ce fichier il faut importer les fonctions path et include si on en a besoin. A l'intérieur de urlpatterns, on met les urls sous la forme:

```python
from .views import fonction
path("nom_app/chemin", fonction, name="nom_url")
```

Cela se passe ainsi lorsque la vue se positionne dans la même application. Si la vue se trouve dans une autre application, il faut importer la fonction include et mettre dans urlpatterns:

```python
path("nom_app/", include("nom_app.urls"), name="nom_url")
```

Et ensuite, dans le fichier urls.py de l'app, on met:

```python
from .views import fonction
path("", fonction, name="nom_url")
```

Il faut mettre l'argument name pour pouvoir faire le lien entre les urls et les vues.

# views.py

Le fichier views.py permet de créer les vues. Ce sont des fonctions qui prennent en argument request et qui renvoient une réponse(la page web). Par exemple, la méthode POST sera utilisé pour envoyer des données au serveur et sera routé par le fichier urls.py vers la fonction vue qui va traiter les données et renvoyer une réponse. C'est également ici que l'on va gérer l'authentification. 
Le code suivant permet de renvoyer une page html contenu dans le dossier templates de l'application:

```python
from django.shortcuts import render

def index(request):
	return render(request, "nom_app/html/index.html")
```

Pour faire des pages dynamiques, on utilise le context. On passe en argument à render, un dictionnaitre qui s'appelle context. Il fait le lien entre le template et les données de la base. A l'intérieur de la page html, on met une double accolade et une clé du dictionnaire.

```python
from django.shortcuts import render

def index(request):
	return render(request, "nom_app/html/index.html", context={"cle": "valeur"})
```

# models.py

Le fichier models.py regroupe tous les modèles.
Les modèles sont des classes qui permettent de représenter des tables des données dans la base de données. Chaque attribut de la classe représente un champ de base de données. Par défaut, Django utilise une base de données SQLite.
Après créé un modèle, il faut effectuer la commande suivante pour que Django puisse l'utiliser :

```sh
python manage.py makemigrations
```

Puis:

```sh
python manage.py migrate
```

## models.Model

 Chaque classe créé va hériter de cette classe pour devenir un modèle. Le nom de la table est le nom de la classe nouvellement créé:

```python
from django.db import models
class NomModel(models.Model):
	pass
```

On peut définir le nom des champs par une variable et leur type par des méthodes prédéfinites:

```python
from django.db import models
class NomModel(models.Model):
	nom_champ = models.CharField(max_length=100)
```

 On peut aussi définir des contraintes sur les champs.

## Relationnel

Pour créer une relation entre deux tables, il existe trois types de relations:

ManyToMany(plusieurs à plusieurs): Une table peut avoir plusieurs instances d'une autre table et une instance d'une table peut avoir plusieurs instances d'une autre table.

OneToMany(plusieurs à un): Une table peut avoir plusieurs instances d'une autre table mais une instance d'une table ne peut avoir qu'une seule instance d'une autre table.

OneToOne(un à un): Une table peut avoir une seule instance d'une autre table et une instance d'une table peut avoir une seule instance d'une autre table.


```python
class NomModel():
	nom_champ = models.ForeignKey("NomAutreModel", on_delete=models.CASCADE)
```

# Admin.py

Le fichier admin.py permet de gérer les données de la base de données. Pour que l'administrateur puisse accéder aux modèles depuis l'interface web à l'url /admin/, on  inscrit les modèles commes suit dans n'importe quel fichier admin.py:

```python
from django.contrib import admin
from .models import nom_model

admin.site.register(nom_model)
```

# Authentification

Le modèle d'authentification User ne nous convient pas puisqu'il ne contient pas un champ "type" que l'on veut pour caractériser l'utilisateur(soit expéditeur, soit destinataire etc). On va donc créer un modèle CustomUser qui hérite des méthodes d'authentification et auquel on va ajouter un champ "type".

De plus, nous voulons que l'authentification se fasse avec l'adresse mail et non avec le nom d'utilisateur car elle se réalise par défaut avec le nom d'utilisateur et le mot de passe. La création d'un utilisateur ne se fera plus avec son nom comme identifiant. 

```python
USERNAME_FIELD = 'email'
```

De plus, on a besoin de redéfinir ce dont à besoin create_user pour réalisé la création d'un utilisateur. On va donc créer une classe UserManager qui hérite de BaseUserManager et qui va redéfinir les méthodes de créations d'utilisateur.

Création d'un utilisateur:

```python
CustomUser.objects.create_user(email="test@test.fr", password="test", type="addressee")
```

Ctrl-F5 pour rafraîchir la page sans utiliser le cache.