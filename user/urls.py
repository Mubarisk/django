from django.urls import path
from . import views

urlpatterns = [
    path('path/',views.path,name='pathSpecifier'),
    path('', views.home, name="home"),
    path('add_user_data/', views.add_user_data, name='add_user_data'),
    path('delete_user/', views.delete_user, name="delete_user"),
    path('edit_data/', views.edit_data, name='edit_data'),
    path('delete_data/', views.delete_data, name='delete_data'),
    path('users/', views.view_users, name='view_users'),
    path('users/detailed_view/<int:userid>/', views.detailed_view, name='detailed_view'),
    path('users/addlike/<int:userid>/', views.addlike, name='addlike'),
    path('view_owners/',views.view_owners,name='view-owner'),
    path('detailed_owner_view/<int:id>/',views.detailed_owner_view,name="detailed_owner_view"),
    path('add_request/<int:id>/',views.add_request,name='add_request'),
    path('view_requests/',views.view_requests,name='view-requests'),
    path('delete_request/<int:id>/',views.delete_request,name='delete_request'),


]
