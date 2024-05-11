## Projet : Développez un programme logiciel en Python

[**English**](README.md)
<p>
  <img src="pictures/Chess-Tournament-OOP.png" />
</p>

### Tables des matières :
1. Description générale du projet.
2. Configurations compatibles.
3. Installation du programme.
4. Fonctionnalités.
5. Démarrage du programme.

## 1. Descripton générale du projet :

Ce projet a été réalisé dans le cadre de la formation de
développeur Python proposée par OpenClassrooms. Le thème principal étant
la programmation orientée objet : P.O.O,
l'objectif de ce projet est de coder une "application" de gestion de tournoi d'échecs
tout en utilisant le design pattern M.V.C (Model View Controller).
De plus, le logiciel fonctionne hors ligne et permet de sauvegarder les données relatives aux joueurs
et aux tournois dans une base de données.

## 2. Configurations compatibles :

* Python 3
* Windows 10
* Mac
* Linux

## 3. Installation du programme :
Ce programme utilise les librairies Python suivantes :

```
flake8 6.0.0
flake8-html 0.4.3
Jinja2 3.1.2
MarkupSafe 2.1.1
mccabe 0.7.0
prettytable 3.5.0
pycodestyle 2.10.0
pyflakes 3.0.1
Pygments 2.13.0
tinydb 4.7.0
wcwidth 0.2.5
```

## 4. Fonctionnalités :

### *Fonctionnalité 1* : Afficher les **joueurs**
  * 1.1 : Afficher tous les joueurs présents dans la **base de données**.
  * 1.2 : Afficher les joueurs d'un **tournoi**.
### *Fonctionnalité 2* : **Ajouter** un joueur.
### *Fonctionnalité 3* : **Modifier le classement** d'un ou de plusieurs joueurs.
### *Fonctionnalité 4* : **Afficher tous les tournois** sauvegardés dans la base de données.
  * 4.1 : Ajouter un tournoi.
  * 4.2 : Accéder à un tournoi.
    * 4.2.1 : **Terminer un tour** (afin d'indiquer le **gagnant** de chaque **partie**).
    * 4.2.2 : Accéder au **tour suivant**.
    * 4.2.3 : **Modifier** le classement des joueurs (lorsque le tournoi est terminé).
    * 4.2.4 : Afficher le **score** actuel.
    
## 5. Démarrage du programme :

1. Ouvrir un terminal (ex: Cygwin pour Windows, le terminal pour Mac) ou dans un IDE (ex: PyCharm).
2. Télécharger le dossier contenant le projet puis se placer dans ce dossier sur le terminal.
3. Créer un environnement virtuel avec :
  > $<b> python -m venv <nom de l'environnement></b> 
4. Activer l'environnement virtuel en éxécutant :
  > $ <b>source env/bin/activate</b>  (sur Mac) 

  > $ <b>env/Scripts/activate.bat</b> (sur Windows)
5. Installer les paquets présents dans le fichier requirements.txt (ce fichier se trouve dans le dossier du projet avec main.py) avec :
  > $ <b>pip install -r requirements.txt</b> 
6. Finalement, lancer le script avec
> $ <b>python main.py</b>
7. Pour générer un nouveau rapport flake8 :
> $ <b>flake8 --format=html --htmldir=flake8-rapport</b>


---
