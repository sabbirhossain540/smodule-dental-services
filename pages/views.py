from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

# def about(request):
#     return render(request, 'pages/about.html')

def contact(request):
    if request.method == "POST":
        sender_name = request.POST['sender_name']
        sender_email = request.POST['sender_email']
        message = request.POST['message']
        
        #Send Email
        send_mail(
            #Subject
            'Messege From SModule Dental Services '+sender_name
            ,
            #Messege
            message
            ,
            #From Email
            sender_email
            ,
            ['job.sabbirhossain308@gmail.com'],   #To Email

            fail_silently=False 

        )

        return render(request, 'pages/contact.html')

    else:
        return render(request, 'pages/contact.html')





