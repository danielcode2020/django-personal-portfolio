**Cerintele :**

Tema pe parcurs la disciplina TWAAOS va consta în implementarea unei aplicații Django minimale.

Exemplificare:
Implementarea unui C.V. personal folosind Django. Cerințe minimale: 
- utilizarea unui fișier CSS sau framework de stilizare (de exemplu Bootstrap);
- extragerea informațiilor dintr-o baza de date (de exemplu SQLite 3);
- utilizarea a cel puțin unei imagini în cadrul C.V.-ului;
- utilizarea a cel puțin 2 pagini web diferite pentru prezentarea informațiilor;
- exportarea pachetelor cerute de aplicație (pip freeze); fișier de requirements;
- utilizarea unui mediu virtual/container/sandbox pentru rularea aplicației.
Aplicația va fi însoțită de un document PDF care va descrie pe scurt tema, tehnologia de implementare și screenshot-uri relevante din GUI și baza de date (2-3 pagini). 

Comenzile de compilare/rulare/execuție (sau scripturile ce le conțin) vor fi de asemenea listate în document.


**Rularea aplicatiei folosind python local :**

1. Create the virtual environment :
```
py -m venv .venv
```
2. Navigate to personalportfolio and start application
```
cd personalportfolio/
```
```
py manage.py runserver 8001
```

**Rularea aplicatiei folosind docker (1 comanda) :**
```
docker run -p 8000:8000 danielmarandici/django-personal-portfolio:latest
```

**Comenzi utile :**

Creating a virtual env 
```
py -m venv .venv
```

Activating the virtual env :
```
source .venv/Scripts/activate
```

Installing Django :
```
py -m pip install Django
```

Creating a django project :
```
django-admin startproject personalportfolio
```

**Comenzi docker**

Build local docker image.
From Django-portfolio/personalportfolio run :
```
docker build -t danielmarandici/django-personal-portfolio .
```

Push the image :
``` 
docker push danielmarandici/django-personal-portfolio:latest 
```
