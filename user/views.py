from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserProfile, Director, Requests
import os
from django.core.mail import send_mail, send_mass_mail


# Create your views here.
@login_required
def path(request):
    userinstance = User.objects.get(id=request.user.id)
    path_specifier = Director.objects.get_or_create(user=userinstance)
    print(path_specifier[0].position)
    if path_specifier[0].position == 'user':
        return redirect('/')
    elif path_specifier[0].position == 'owner':
        return redirect('/hotel/')
    else:
        return redirect('/admin/')


@login_required
def home(request):
    details = UserProfile.objects.filter(user=request.user.id)

    return render(request, 'home.html', {'data': details})


@login_required
def add_user_data(request):
    if request.method == 'POST':
        print(request.POST['phone'])
        userinstance = User.objects.get(id=request.user.id)
        add = UserProfile(user=userinstance, image=request.FILES['image'], phone=request.POST['phone'])
        add.save()
        return redirect("/")
    else:

        return render(request, 'add_data.html')


@login_required
def delete_user(request):
    user = User.objects.get(id=request.user.id)
    user.delete()
    return redirect('/')


@login_required
def edit_data(request):
    if request.method == 'POST':

        change = UserProfile.objects.get(user=request.user.id)
        change.phone = request.POST['phone']
        change.image = request.FILES['image']
        change.save()
        return redirect("/")
    else:
        data = UserProfile.objects.filter(user=request.user)
        # print(data[0].phone)
        return render(request, 'edit_details.html', {'phone': data[0].phone})


@login_required
def delete_data(request):
    data = UserProfile.objects.filter(user=request.user)

    data.delete()

    return redirect("/")


@login_required
def view_users(request):
    user_profiles = UserProfile.objects.exclude(user=request.user)
    print(user_profiles.values())
    return render(request, 'all_users.html', {'profiles': user_profiles})


@login_required
def detailed_view(request, userid):
    user = User.objects.get(id=userid)
    profile = UserProfile.objects.get(user_id=userid)
    print(user)
    print(profile.phone)
    return render(request, 'view_detail.html', {'user': user, 'profile': profile})


def addlike(request, userid):
    profile = UserProfile.objects.get(user_id=userid)
    if profile.like:
        profile.like = profile.like + 1
        profile.save()
    else:
        profile.like = 1
        profile.save()

    userid = str(userid)
    return redirect('/users/detailed_view/' + userid + '/')


def view_owners(request):
    owners = Director.objects.filter(position='owner')

    return render(request, 'view_owners.html', {'owners': owners})


def detailed_owner_view(request, id):
    data = User.objects.get(id=id)
    return render(request, 'detailed_owner_view.html', {'data': data})


def add_request(request, id):
    user = User.objects.get(id=id)
    rw = Requests.objects.create(owner=user, userid=request.user.id, status='pending')
    rw.save()
    return redirect('/')


def view_requests(request):
    req = Requests.objects.filter(userid=request.user.id)
    return render(request, 'request.html', {'requests': req})


def delete_request(request, id):
    Requests.objects.filter(id=id).delete()

    return redirect('/view_requests/')



