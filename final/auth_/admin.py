from django.contrib import admin
from auth_.models import AuthUser, UserProfile
# Register your models here.

admin.site.register(AuthUser)
admin.site.register(UserProfile)
