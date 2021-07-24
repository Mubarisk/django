from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from user.models import UserProfile, Director


# Create your views here.
@login_required
def adminpanel(request):
    users = Director.objects.filter(position='user')
    owners = Director.objects.filter(position='owner')

    print(owners)
    return render(request, 'adminpanel.html', {'users': users, 'owners': owners})


@login_required
def remove(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('adminpanel'))


def add_owner(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:

            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'])
            user.save()
            userid = User.objects.get(username__exact=request.POST['username'])
            userinstance = User.objects.get(id=userid.id)
            director = Director.objects.create(user=userinstance, position='owner')
            director.save()
            subject = 'welcome '
            message = 'youre registered  your username : ' + request.POST['username'] + '\n your password :' + \
                      request.POST['password1']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email']]
            send_mail(subject, message, email_from, recipient_list)

            return HttpResponseRedirect(reverse('adminpanel'))
        else:

            return render(request, 'registration/register.html')
    return render(request, 'add_owner.html')
