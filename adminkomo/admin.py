from django.contrib import admin
from .models import Excel
# Register your models here.

class ExcelAdmin(admin.ModelAdmin):
    list_display = ('file', 'date')

admin.site.register(Excel, ExcelAdmin)