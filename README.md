# Learn Django by Coding

Open-source project provided by AppSeed to help beginners accommodate and learn Django faster. For newcomers, Django is a popular web framework designed and actively supported by Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel.  

> **For support and more [Django Samples](https://appseed.us/admin-dashboards/django) join [AppSeed](https://appseed.us).**

<br />

## Create a new Django project

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

--- 
Learn Django by Coding - Provided and actively supported by AppSeed [App Generator](https://appseed.us)