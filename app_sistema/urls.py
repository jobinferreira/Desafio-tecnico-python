from django.contrib import admin
from django.urls import path

from app_sistema.views import EquipamentoListView

urlpatterns = [
    path('', EquipamentoListView.as_view()),
    # path('api/', name='api_rest_urls')
]