from django import forms 
 
class HelloForm(forms.Form): 

    title   = forms.CharField()
    message = forms.CharField() 
    id      = forms.IntegerField()
    email   = forms.EmailField(required=False) 

