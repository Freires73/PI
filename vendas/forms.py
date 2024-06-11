from django import forms

from reciclagem.models import Produto
from pontocoleta.models import Pontocoletas


class VendasForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"
    