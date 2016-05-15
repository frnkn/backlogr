from django.contrib import admin

# Register your models here.
from models import Backlog

class BacklogAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'short_id', 'user', 'name', 'created_on', 'updated_on']


admin.site.register(Backlog, BacklogAdmin)
