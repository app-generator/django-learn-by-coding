# Learn Django by Coding

Open-source project provided by AppSeed to help beginners accommodate and learn Django faster. For newcomers, Django is a popular web framework designed and actively supported by Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel.  

> **For support and more [Django Samples](https://appseed.us/admin-dashboards/django) join [AppSeed](https://appseed.us).**

<br />

## Create Django project

> Create a virtual environment

```bash 
$ # Linux-based systems
    $ virtualenv env
    $ source env/bin/activate  
```

For Windows systems, the syntax is different

```bash
$ virtualenv env
$ .\env\Scripts\activate
```

<br />

> Install Django using PIP, the official package manager for Python

```bash
$ pip install django
```

<br />

> Create project directory

```bash
$ mkdir learn-django
$ cd learn-django
```

<br />

> Create project core

```bash
$ django-admin startproject config .
```

<br />

> Set up the database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the project

```bash
$ python manage.py runserver 
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

<br />

## Generate PDF Files 

> Install dependencies

```bash
$ pip install reportlab
```

<br />

> Generate PDF file using Django Shell

```python
$ python ./manage.py shell
>>>
>>> import reportlab
>>> from reportlab.pdfgen import canvas 
>>> p = canvas.Canvas('1.pdf')
>>> p.drawString(200, 200, "Hello world.") 
>>> p.showPage() 
>>> p.save()
```

The above code should create in the root of the project a new PDF file. To open the file, from the Django console, please type:

```python
>>> import os,sys
>>> os.startfile('1.pdf', 'open')
```

The `startfile` helper should open the `PDF` file using the default handler registered in the operating system.

<br />

> PDF creation with dynamic content - `app_pdf/pdf_dw` 

```python
# File Content: app_pdf/pdf_dw (partial content)
def pdf_dw(request):                                  

    # Create the HttpResponse object with the appropriate PDF headers. 
    response = HttpResponse(content_type='application/pdf') 

    # Comment the line to see the PDF in the browser 
    response['Content-Disposition'] = 'attachment; filename="1.pdf"' 
 
    # Create the PDF object, using the response object as its "file." 
    p = canvas.Canvas(response)     

    # READ Optional GET param
    get_param = request.GET.get('name', 'World')
    
    # Generate unique timestamp
    ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

    # Write content on the PDF 
    p.drawString(100, 500, "Hello " + get_param + " (Dynamic PDF) - " + ts ) 
 
    # Close the PDF object. 
    p.showPage() 
    p.save() 

    # Show the result to the user    
    return response
```

<br />

> PDF creation with image - `app_pdf/pdf_img`

```python
def pdf_img(request):                                  

    # Create the HttpResponse object with the appropriate PDF headers. 
    response = HttpResponse(content_type='application/pdf') 
 
    # Create the PDF object, using the response object as its "file." 
    p = canvas.Canvas(response)     

    my_image = ImageReader('https://www.google.com/images/srpr/logo11w.png')
    
    p.drawImage(my_image, 10, 500, mask='auto')

    # Close the PDF object. 
    p.showPage() 
    p.save() 

    # Show the result to the user    
    return response
```

<br />

## Create Custom Commands

> Create the new app

```bash
python manage.py startapp app_customcmd
```

**Inside the new app directory** create a structure as shown below:

```bash
< PROJECT ROOT >                          <-- project directory
 |
 |-- app_customcmd/                                <-- app directory
 |    |-- management/
 |    |	   +-- __init__.py
 |    |    +-- commands/
 |    |         +-- __init__.py
 |    |         +-- cmd_....py  <-- module where all commands are saved
```

<br />

> Update configuration to enable the new app

```python
# File content: config/settings.py (partial content)
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_forms',
    'app_pdf',
    'app_customcmd',                     # <-- NEW
    'app',
]
...
```

<br />

> Code a new dummy command - new file `app_customcmd/management/commands/cmd_time.py`

```python
# File content: cmd_time.py

from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's %s" % time)
```

<br />

> Registered Commands:

- `cmd_time.py` - show current timestamp
- `cmd_apps`    - list all registered apps
- `cmd_models`  - list all apps and associated models
- `cmd_showcfg` - list all CFG keys and values

**Command Usage sample**

```bash
$ python manage.py cmd_models 
```

**Sample output**

```bash
APP -> Administration
         |- (model) -> <class 'django.contrib.admin.models.LogEntry'>
 APP -> Authentication and Authorization
         |- (model) -> <class 'django.contrib.auth.models.Permission'>
         |- (model) -> <class 'django.contrib.auth.models.Group'>
         |- (model) -> <class 'django.contrib.auth.models.User'>
 APP -> Content Types
         |- (model) -> <class 'django.contrib.contenttypes.models.ContentType'>
 APP -> Sessions
         |- (model) -> <class 'django.contrib.sessions.models.Session'>
 APP -> Messages
 APP -> Static Files
 APP -> App_Forms
 APP -> App_Pdf
 APP -> App_Customcmd
 APP -> App
         |- (model) -> <class 'app.models.Book'>
```

<br />

--- 
Learn Django by Coding - Provided and actively supported by AppSeed [App Generator](https://appseed.us)
