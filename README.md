Installing Packages:
New Terminal
pip3 install Django~=4.2.1
pip3 freeze --local > requirements.txt
check requirements asgiref==3.7.2, django==4.2.7, sqlparse==0.4.4
return to terminal
django-admin startproject my_project .
python3 manage.py runserver

open browser
expect yellow screen in browser
Select and copy the hostname after "Invalid HTTP_HOST header:' eg. '8000-nielmc-django-project-0kylrta3cs.us2.codeanyapp.com'

in my_project/settings.py paste
ALLOWED_HOSTS = ['8000-nielmc-django-project-0kylrta3cs.us2.codeanyapp.com']
refresh browser

creating views
python3 manage.py startapp hello_world
hello_world/views.py
from django.http import HttpResponse

create urls
my_project/urls.py
django.urls import include
from hello_world import views as index_views
above url patterns:
path('', index_views.index, name='index'),

settings.py
scroll through my_project/settings.py 
find INSTALLED_APPS
Append 'hello_world',
