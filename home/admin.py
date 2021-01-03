from django.contrib import admin
from . import models

# Register your models here.
class post_admin(admin.ModelAdmin):
    list_display = ['title', 'date']

admin.site.register(models.post, post_admin)