# Django Web Programming
Django is a web framework that takes away the complexiteis of setting up a web application and allows the programmer to focus on the logic
...


## HTTP: the internet protocol that enables the client, server communication.

_think of the web as a series of request and responses_

request
GET / HTTP / 1.1
Host: www.localhost.com
...

response
HTTP/1.1 200 OK
Content-Type: text/html
...

HTTP Status Codes
200-OK, 301-Moved permanently, 404-Not Found etc
...

## Starting a Django Project with django-admin

_django-admin startproject PROJECT-NAME_
...

_py manage.py runserver_ start application
...

port number 8000 - _indicates what type of sevice is being run, multiple internet services can be run in our case is our djano app_
...

_localhost - 127.0.0.1 - indicates our local machine_
...

## Creating our Django App with startapp

add app to Installed Apps list in settings.py _settings.py_
...

you can think of each view as something the user wants to see. 
the (request) argument in the view function represents the request the user wants to make

you can specify additional parameters for your view function, this argument can be used in the path('<str:name>') in urls.py to return anything value passed to the name variable_views.py_
...


we need to tell our app when to run display a particular (or run a particular) and we do this by configuring the url for that particular response, 
...
in path(route, view, name) giving a name to a url pattern allows us to easily reference the url in another application 
...

In our top project(my_app) urls.py we want to add a path with a route and  include(), we use include to link the urls in our app with the one in our project urls _urls.py_
...


we use the render function to render html from the templates directory, the context contains things like variable and other expresions 
_render(request, 'template.html', {context})_
...




layout defines the template of our html, it sets the default look that the other templates will inherit from _layout.html_






when we click on a link the impicit method used is get, while _post_ is used when submitting info on the web 

security defect inherent in forms that are not designed in a secure way,it means someone on a different website could forge a request _cross site request forgery_ the CSRF token is used to validate requests, it creates a unique token for each section

django middleware is the ability for django to intervene in the request/response process. django ensures that we have CSRF token whenever we are submitting a request via 'method=post'.
_submitting data_
...



we can also import forms from django to help us in setting up/interacting with forms, if you dont provide a label for the 'task = charfield(label='')' django will use the variable name as the label  _django forms_