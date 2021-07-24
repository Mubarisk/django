from django.urls import path, include
from . import views

urlpatterns = [
    path('user/register', views.register, name='register'),
    path('user/', include('django.contrib.auth.urls')),
    # path('adduser/', views.adduser, name='adduser'),

]
