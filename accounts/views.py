from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User



# Create your views here.


def register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:

            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'])
            user.save()

            return redirect('/')
        else:
            return render(request, 'registration/register.html')
    else:
        return render(request, 'registration/register.html')


def logout(request):
    logout(request)
