from django.contrib import admin
from . import models

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created', 'last_modified', 'user')

admin.site.register(models.Notes, NotesAdmin)