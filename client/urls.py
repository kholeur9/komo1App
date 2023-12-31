from django.urls import path
from .views import client, connexion, deconnexion, retrait, forfait, historique, service_client

urlpatterns = [
    path('<int:client_id>/', client, name="client"),
    path('connexion/', connexion, name="connexion"),
    path('deconnexion/', deconnexion, name="deconnexion"),
    path('retrait/<int:client_id>/', retrait, name="retrait"),
    path('forfaitkomo/<int:client_id>/', forfait, name="forfait"),
    path('historique/<int:client_id>/', historique, name="historique"),
    path('service-client/<int:client_id>/', service_client, name="service_client"),
]