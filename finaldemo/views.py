from django.shortcuts import render
from django.http import HttpResponse
from  .models import Contact
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def show(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        #mail send code
        subject = 'Brainscube'
        message = f'Hi {name}, thank you for visiting braincibes.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )

        thank = True
        return render(request, 'home.html', {'thank':thank})
    return render(request,'home.html')


def sapuishow(request):
    return render(request,'sapui.html')

def fiorishow(request):
    return render(request,'fiori.html')

def hanashow(request):
    return render(request,'hana.html')

def cloudshow(request):
    return render(request,'cloud.html')

def cpishow(request):
    return render(request,'cpi.html')

def successfactshow(request):
    return render(request,'success.html')

def saleshow(request):
    return render(request,'sale.html')

def c4cshow(request):
    return render(request,'c4c.html')

def javashow(request):
    return render(request,'javacdc.html')

def cloudcomputingshow(request):
    return render(request,'cloudcomputing.html')

def aboutshow(request):
    return render(request,'about.html')

def serviceshow(request):
    return render(request,'service.html')

def portfolioshow(request):
    return render(request,'portfolio.html')

def contactshow(request):
    return render(request,'contact.html')
