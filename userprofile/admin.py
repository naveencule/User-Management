from django.contrib import admin
from .models import Profile, Skill

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_email', 'contact_phone', 'bio')  

admin.site.register(Skill)
