from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminpanel, name='adminpanel'),
    path('removeuer/<int:id>/', views.remove, name='remove'),
    path('addowner/',views.add_owner,name='add_owner'),
]
