from django import forms
from .models import Equipamento

class PostEquip(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = '__all__'