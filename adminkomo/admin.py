from django.contrib import admin
from .models import ExcelFile
from django.contrib.auth.admin import UserAdmin
from .models import User
from .utils.excel import send_data
# Register your models here.

class ExcelFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'date')
    actions = ['download_file']

    def download_file(self, request, queryset):
        for excel_file in queryset:
            send_data(excel_file.file.path)

    download_file.short_description = 'Fichier excel exporté'

admin.site.register(ExcelFile, ExcelFileAdmin)
admin.site.register(User, UserAdmin)