from django.urls import path
from .views import index, data_excel, demande

urlpatterns = [
 path('', index, name="adminkomo"),
 path('data_excel/', data_excel, name="excel"),
 path('reclamations/', demande, name="demande"),
]