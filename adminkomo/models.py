from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class ExcelFile(models.Model):
    file = models.FileField(upload_to='data_excel/')
    date = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return f"{self.file}"