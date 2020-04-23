from django.shortcuts import render
from django.http import HttpResponse
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
        print(message)
        return render(request, 'pages/contact.html')

    else:
        return render(request, 'pages/contact.html')





