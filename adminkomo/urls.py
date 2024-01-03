from django.urls import path
from .views import index, connexion, deconnexion, data_excel, demande

urlpatterns = [
 path('', index, name="adminkomo"),
 path('connexion/', connexion, name="connexion"),
 path('data_excel/', data_excel, name="excel"),
 path('reclamations/', demande, name="demande"),
 path("deconnexion/", deconnexion, name="deconnexion"),
]