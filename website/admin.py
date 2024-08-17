from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile  

# Inline profile info to user
class ProfileInline(admin.StackedInline):
    model = UserProfile

# Custom UserAdmin
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

# Unregister the old way
admin.site.unregister(User)

# Re-register with the new UserAdmin
admin.site.register(User, UserAdmin)

