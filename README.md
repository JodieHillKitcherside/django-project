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
python3 manage.py startapp hello_world - starting an ppp
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

Explanation:
Creating a project:

The django-admin startproject command expects to see a project name followed by a directory name. For example:
django-admin startproject project_name directory_name
In our case, the directory name is shown as a dot. The dot tells us that the project should be created in the current directory.
django-admin startproject my_project .
Note: If you leave the dot off and just type django-admin startproject my_project then it will create the project, my_project, inside a directory called my_project. If that happens, simply delete the directory and run the correct startproject command again.
When the project is created, you should see the directory structure similar to the following:
manage.py
my_project/
  init__.py
  settings.py
  urls.py
  asgi.py
  wsgi.py
You'll learn more about these files in future lessons, but for now key files to note are: manage.py, settings.py, and urls.py.
You can see that the settings.py file is in the my_project directory. There are six apps listed in INSTALLED_APPS; this is the default for any new project.
Creating an app:

The command we used to start the Hello World app was:
python3 manage.py startapp hello_world
The command created an app Inside the hello_world directory. In there, you will see files such as models.py and views.py. These will be the main files you will use to build a project.
Creating a project
The top level in Django is a project. A project is like a container for everything we want to do. By default, the project contains a settings file and some other administrative files.

Important files in our project folder:

settings.py: this file contains the project-wide settings, such as installed apps and database connection information, among other things.
manage.py: this file is in the root directory, above the project folder. It is used to create apps, run our project and perform some database operations.
Creating an app
Inside the project, we create apps. We’ll go into this a bit deeper later on, but an app’s structure is like a Python package with multiple Python modules within a directory.

Simply put, apps are the building blocks of Django. They’re the things that actually do something, such as a blog, a to-do list, or a poll. A project can contain many, many apps. You could do everything you want with just one app, but for maintainability and good design practices, it is better to separate different functionality into different apps.

Important files in our apps folder:

models.py: our database models are stored here, which define the structure of the database used by our app.
views.py: this file contains the view code for our app. You’ve already created some view code to display a text response to the user.

Urls:
When you add a path like this to the urls.py file, we are telling Django that when the user inputs this specific URL, it should run the index function within the views.py linked to this path, e.g.
path('hello/',  index_views.index, name='index'),

Example of views function:
def index(request):

   if request.method == "GET":
       return HttpResponse("This was a GET request")
   elif request.method == "POST":
       return HttpResponse("This was a POST request")

Deploy project:
Click on the Settings tab and reveal the config vars. Add a key of DISABLE_COLLECTSTATIC and a value of 1 and click Add.
In the terminal:
pip3 install gunicorn~=20.1 
Add gunicorn==20.1.0 to the requirements.txt file with:
pip3 freeze --local > requirements.txt
Create a file named Procfile at the root directory of the project (same directory as requirements.txt).
. In the Procfile, declare this is a web process followed by the command to execute your Django project.
web: gunicorn my_project.wsgi
Open the my_project/settings.py file and replace DEBUG=True with DEBUG=False.
 Also, in settings.py we need to append the Heroku hostname to the ALLOWED_HOSTS list, in addition to the local host we added in the last lesson.

,'.herokuapp.com'

You can now git add the files you have modified, git commit them and push them to GitHub.