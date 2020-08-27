from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def send_message(request):
    if request.method == 'POST':
        subject = request.POST['txtSubject']
        email = request.POST['txtEmail']
        message = request.POST['txtMsg']
    
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER, #from
            [email] #to
        )
    
    return render(request, 'contact/contact.html', {})
