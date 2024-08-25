from django.contrib import admin
from django.contrib.auth.models import User

from .models import UserProfile, Category, Puzzle

# Inline profile info to user
class ProfileInline(admin.StackedInline):
    model = UserProfile

# Custom UserAdmin
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]


# Unregister the old way
admin.site.unregister(User)

# Re-register with the new UserAdmin
admin.site.register(User, UserAdmin)


admin.site.register(Category)
admin.site.register(Puzzle)
