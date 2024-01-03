from django.contrib import admin
from .models import ExcelFile
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

class ExcelAdmin(admin.ModelAdmin):
    list_display = ('file', 'date')

admin.site.register(ExcelFile, ExcelAdmin)
admin.site.register(User, UserAdmin)