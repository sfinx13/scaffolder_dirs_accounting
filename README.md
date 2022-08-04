# Scaffold directory for accounting
Generate the skeleton of the directories which makes it possible to store the documents for the accounting

## Installation

> Create virtual environments
```
 python -m venv env
```

> [Linux] Activate virtual environment
```
source .env/bin/activate 
```


> [Windows] Activate virtual environment
```
.env/Scripts/activate
```

> Install packages with pip
```
pip install -r requirements.txt
```

> Init file configuration
```
mv config/settings.ini.dist config/settings.ini
```

> Lint with flake
```
$ flake8 .
```


##  Demonstration


```
$ python main.py 
```

```
Merci de saisir une année : 2023
Merci de saisir le numéro du mois entre 1 et 12 : 5
```

```
[OK] /home/jdoe/accounting/2023/05-mai/1-frais-transport crée
[OK] /home/jdoe/accounting/2023/05-mai/2-frais-repas crée
[OK] /home/jdoe/accounting/2023/05-mai/3-charges-communes crée
[OK] /home/jdoe/accounting/2023/05-mai/4-frais-achats crée
[OK] /home/jdoe/accounting/2023/05-mai/5-dons crée
```
