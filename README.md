## Project : Develop a software program in Python

[**Français**](README-fr.md)
<p>
  <img src="Pictures/Chess-Tournament-OOP.png" />
</p>

### Table of contents :
1. Project description.
2. Compatible configurations.
3. Installing the program.
4. Features.
5. Running the program.

## 1. Project description :

This project was carried out as part of the Python Developer training offered by OpenClassrooms.
The main topic being object-oriented programming: O.O.P,
the objective of this project is to code a chess tournament management "application"
while using the M.V.C (Model View Controller) design pattern.
Moreover, the software works offline and saves player and tournament data in a database.

## 2. Compatible configurations :

* Python 3
* Windows 10
* Mac
* Linux

## 3. Installing the program :
This program uses the following Python libraries :

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

## 4. Features :

### *Feature 1* : Show the **players**
  * 1.1 : Show all players present in the **database**.
  * 1.2 : Show players in a **tournament**.
### *Feature 2* : **Add** a player.
### *Feature 3* : **Modify the ranking** of one or more players.
### *Feature 4* : **Show all tournaments** saved in the database.
  * 4.1 : Add a tournament.
  * 4.2 : Access a tournament.
    * 4.2.1 : **End a round** (to indicate the **winner** of each **game**).
    * 4.2.2 : Access the **next round**.
    * 4.2.3 : **Modify** player rankings (when tournament is over).
    * 4.2.4 : Show current **score**.
    
## 5. Running the program :

1. Open a terminal (e.g., Cygwin for Windows, the Terminal for Mac) or in an IDE (e.g., PyCharm).
2. Download the folder containing the project then go in this folder on the terminal.
3. Create a virtual environment with :
  > $<b> python -m venv <nom de l'environnement></b> 
4. Activate the virtual environment via :
  > $ <b>source env/bin/activate</b>  (sur Mac) 

  > $ <b>env/Scripts/activate.bat</b> (sur Windows)
5. Install the packages present in the requirements.txt file (this file is located in the project
folder with main.py) with:
  > $ <b>pip install -r requirements.txt</b> 
6. Finally, run the script with :
> $ <b>python main.py</b>
7. To generate a new flake8 report :
> $ <b>flake8 --format=html --htmldir=flake8-rapport</b>


---
