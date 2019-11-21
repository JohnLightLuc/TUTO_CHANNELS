from django.contrib import admin
from .models import *


@admin.register(Chat)
class CategorieAdminCategorieAdmin(admin.ModelAdmin):
    list_display = ('message','user','status','date_add','date_update')
    list_filter = ('status','date_add','date_update')
    search_fields = ('message',)