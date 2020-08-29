# Learning_Log  
   *a web app called Learning Log that allows users to log the topics they’re interested in and to make journal entries as they learn about each topic.
   The Learning Log home page will describe the site and invite users to either register or log in.
   Once logged in, a user can create new topics, add new entries, and read and edit existing entries.*

## Installation Process/instructions 
 
 ##### Creating a Virtual Environment/activate/deactivate
```
python -m venv ll_env
source ll_env/bin/activate
deactivate
```
      
##### Installing Django / Creating a Project in Django /Creating the Database
 ```
 pip install django
 django-admin startproject learning_log .
 python manage.py migrate
```      
##### view projects
      python manage.py runserver
##### create app inside the project
      python manage.py startapp learning_logs
      

