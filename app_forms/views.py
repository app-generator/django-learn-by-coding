from django.shortcuts import render

from django.http import HttpResponse 
from .forms      import HelloForm

def index(request):                                  
       

    if request.method == 'POST': 
        form = HelloForm(request.POST) 
        if form.is_valid(): 
            return HttpResponse("Form is valid")
    else: 
        form = HelloForm() 
    return render(request, 'hello.html', {'form': form}) 
