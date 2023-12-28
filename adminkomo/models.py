from django.db import models

# Create your models here.
class Excel(models.Model):
    file = models.FileField(upload_to='data_excel/')
    date = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return f"{self.file} - Date: {self.date}"