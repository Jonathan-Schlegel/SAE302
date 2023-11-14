Sur vim:

u(undo) pour retour en arrière
y pour copier
yy pour coppier la ligne
p pour coller
d pour couper
dd pour couper la ligne

Installer django:

```python
pip install django
```

Connaître la version d'un module:

```python
python -m django --version
```

Trouver de l'aide sur django

```python
jango-admin --help
```

Créer les dossiers et fichiers nécessaires au projet django:

```python
django-admin startproject nom_projet
```

Le fichier settings est utile pour configurer la base de données, les applications, les templates etc.
Intéressant variable DEBUG
Renommer le dossier du code par src.

Plus pratique pour démarrer le serveur est de se positionner dans src et faire:

```python
python manage.py runserver
```

On crée un fichier views.py avec les fichiers settings.py etc pour les vues.
Pour faire le lien entre urls.py et views.py dans urls.py par urlpatterns:

```python
from src.nom_projet.views import nom_url
```

Dans views.py

```python
from django.http import httpResponse

def nom_url(request):
	return HttpResponse("mon_html")
```

On se rend compte que mettre notre code html dans le fichier views c'est pas ouf.
On va utiliser les templates.
D'abord on définit le path dans la clé DIRS de la variable TEMPLATE du settings:

```python
os.path.join(BASE_DIR, "nom_projet/templates")
```

templates est le dossier dans le dossier settings urls
BASE_DIR fait référence à src

```python
from django.shortcuts import render

def index(request):
	return render(request, "index.html")
```

Il suffirat de mettre dans le path des views le nom du fichier.

Pour faire des pages dynamiques, on utilise le context. On passe en argument à render, undictionnaitre qui s'appelle context. Il fait le lien entre le template et les données que l'on veut afficher. A l'intérieur de la page html, on met une double accolade et une clé du dictionnaire.

Pour créer une application:

```python
python3 manage.py startapp nom_app
```

Dans le ficheir settings, il faut ajouter dans la liste INSTALLED_APPS, "nom_projet" 

Une bonne pratique est de mettre les urls dans le dossier de l'app. Pour cela on fait dans le fichier root urls:

```python
path("nom_app/", include("nom_app.urls"))
```

Bien sur il faut importer ce qu'il faut dans les deux fichiers urls. Les urls de l'app doivent être dans une liste urlpatterns et seront relatifs au dossier de l'app.

Dans le dossier de l'app il faut ajouter un dossier templates précisement mais comme il regarde tous les dossiers templates il faut créer dedans un dossier avec le nom de l'app. Le path des views sont relatif aux dossier templates de l'app.

Pour faire le lien entre le html et css. On crée un dossier static dans le dossier de l'app. Puis css. On rajoute {% load static %} au début du fichier css. href="{% static 'nom_app/css/style.css' %}" dans le fichier html. Le lien est relatif au dossier static de l'app.

Pour faire le lien entre le html et le css dans le projet gobal, il faut ajouter dans le fichier settings.py:

```python
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "nom_projet/static")
]
```

Mongodb:

Les fichiers de logs et et de données:

/var/lib/mondodb
/var/log/mongodb

Le fichier de configuration:

/etc/mongodb.conf












