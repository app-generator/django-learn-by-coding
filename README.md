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

--- 
Learn Django by Coding - Provided and actively supported by AppSeed [App Generator](https://appseed.us)
