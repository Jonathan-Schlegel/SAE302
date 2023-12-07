# SAE302

## Description

Ce mini-projet consiste à créer un site web pour la gestion de colis. Les technologies utilisées sont Django et sqlite3.


## Conditions

L'utilisateur administrateur peut réaliser toutes les opérations. Il crée, modifie et supprime notamment les expéditeurs et les transporteurs.

L'expéditeur crée des colis et des destinataires. C'est lui qui renseigne toute les informations sur le colis qu'il peut ainsi que sur le destinataire.

Le transporteur créer des livraisons avec les colis qu'il doit livrer. Les livraisons sont associés à des véhicule. A chaque étape, il actualise la localisation des colis.

Le destinataire peut consulter les colis qui lui sont destinés et affirmer si il les a reçu ou non. On part du principe que le destinataire reçoit un mail avec ses identifiants pour se connecter au site. Il n'y a donc pas d'inscription.

## Structure

On a décidé de faire une application par acteur. On a donc une application pour l'administrateur, une pour l'expéditeur, une pour le transporteur et une pour le destinataire. Le dossier du projet contient l'authentification des quatres.

## Installation

Pour lancer le serveur web, il faut se placer dans le dossier src et faire:

```
python3 manage.py runserver 3456
```

