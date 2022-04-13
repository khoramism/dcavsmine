from django import forms
from .models import BNB, BTC, ETH, ADA, SOL

class BNBForm(forms.ModelForm):
    class Meta:
        model = BNB
        exclude = ('datetime',)


class ADAForm(forms.ModelForm):
    class Meta:
        model = ADA
        exclude = ('datetime',)

class BTCForm(forms.ModelForm):
    class Meta:
        model = BTC
        exclude = ('datetime',)

class ETHForm(forms.ModelForm):
    class Meta:
        model = ETH
        exclude = ('datetime',)

class SOLForm(forms.ModelForm):
    class Meta:
        model = SOL
        exclude = ('datetime',)
