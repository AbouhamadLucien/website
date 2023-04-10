

from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'gender', 'skill_level')

admin.site.register(User, UserAdmin)

