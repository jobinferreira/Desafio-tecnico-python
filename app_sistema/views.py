from django.shortcuts import render
from django.views.generic import ListView
from app_sistema.models import Equipamento

class EquipamentoListView(ListView):
    model = Equipamento