from django.contrib import admin
from .models import *


@admin.register(Chat)
class CategorieAdminCategorieAdmin(admin.ModelAdmin):
    list_display = ('message','user','statut','date_add','date_up')
    list_filter = ('statut','date_add','date_up')
    search_fields = ('message',)