from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_joined'
    list_display = ('username', 'email', 'date_joined')

admin.site.register(User, UserAdmin)
