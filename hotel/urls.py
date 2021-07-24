from django.urls import path
from . import views
urlpatterns=[
    path('',views.dash,name='dash'),
    path('requests/',views.request,name='requets'),
    path('requests/accept_request/<int:id>/',views.accept_request,name='accept_request'),
]