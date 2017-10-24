from django import forms
from . import models
class CapmForm(forms.ModelForm):
    class Meta:
        model = models.Capm
        fields = [
            'beta',
            'risk_free_rate',
             'market_return',
        ]