from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.models import User, UserProfile, Requests


# Create your views here.
def dash(request):
    users = UserProfile.objects.all()

    return render(request, 'hoteldash.html', {'users': users})


def request(request):
    r = Requests.objects.filter(owner=request.user.id)
    print(r)
    return render(request, 'request_page.html', {'datas': r})


def accept_request(request, id):
    Requests.objects.filter(id=id).update(status='accept')

    return redirect('/hotel/requests/')

def sendmail(request):
    subject = 'welcome '
    message = 'Hi  this is admin.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mubarikunnath@gmail.com']
    send_mail(subject, message, email_from, recipient_list)

    return HttpResponse('ok')