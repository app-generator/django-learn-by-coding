from django.shortcuts import render

from django.http      import HttpResponse 

from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

from datetime         import datetime

def index(request):                                  
    html  = 'PDF creation in Django'
    html += '<br /> <a href="/pdf_dw/">Download PDF</a>'
    html += '&nbsp;&bullet;&nbsp; <a href="/pdf_dw/?name=Bill Gates">PDF with GET Argument</a>'    
    html += '&nbsp;&bullet;&nbsp; <a href="/pdf_img/">PDF with IMAGE</a>'    
    return HttpResponse( html )   

def pdf_dw(request):                                  

    # Create the HttpResponse object with the appropriate PDF headers. 
    response = HttpResponse(content_type='application/pdf') 

    # This line force a download
    response['Content-Disposition'] = 'attachment; filename="1.pdf"' 
 
    # READ Optional GET param
    get_param = request.GET.get('name', 'World')
    
    # Generate unique timestamp
    ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

    p = canvas.Canvas(response)
    
    # Write content on the PDF 
    p.drawString(100, 500, "Hello " + get_param + " (Dynamic PDF) - " + ts ) 
 
    # Close the PDF object. 
    p.showPage() 
    p.save() 

    # Show the result to the user    
    return response

def pdf_img(request):                                  

    # Create the HttpResponse object with the appropriate PDF headers. 
    response = HttpResponse(content_type='application/pdf') 
 
    # Create the PDF object, using the response object as its "file." 
    p = canvas.Canvas(response)     

    logo = ImageReader('https://www.google.com/images/srpr/logo11w.png')
    
    p.drawImage(logo, 10, 500, mask='auto')

    # Close the PDF object. 
    p.showPage() 
    p.save() 

    # Show the result to the user    
    return response

