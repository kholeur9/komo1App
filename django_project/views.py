from django.shortcuts import render, redirect
from client.views import client

#
def home(request):
    return redirect('client/connexion')