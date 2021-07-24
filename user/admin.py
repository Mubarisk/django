from django.contrib import admin

# Register your models here.
from user.models import UserProfile,Director,Requests

admin.site.register(UserProfile)
admin.site.register(Director)
admin.site.register(Requests)