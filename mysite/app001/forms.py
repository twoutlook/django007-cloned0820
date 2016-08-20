from django import forms

from .models import Item001

class Item001Form(forms.ModelForm):

    class Meta:
        model = Item001
        fields = ('field1', 'field1a',)