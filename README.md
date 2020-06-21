# key-value-api

requirements:
-----------------
  - python >= 3.6
  - virtualenv
  - Git
------------------

* first clone the repo:
  - git clone https://github.com/motaz-hejaze/key-value-api.git


* cd into cloned folder:
  - cd key-value-api

* create virtual environmet:
  - virtualenv venv -p python3.6
  
* activate your virtual environment:
  - source venv/bin/activate (linux)

* install required python packages:
  - pip install -r requirements.txt

* create database and tables:
  - python manage.py makemigrations api_fetcher
  - python manage.py migrate

* create superuser:
  - python manage.py creasuperuser

* runserver:
  - python manage.py runserver

* within your browser , go to http://127.0.0.1:8000/
