from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):

    send_mail( 'Hello from Shared Shelf',
    'Hello there. This is an automated message!',
    'sharedshelf454@gmail.com',
    ['jbatif786@gmail.com'],
    fail_silently = False )

    return render(request, 'send/index.html')
