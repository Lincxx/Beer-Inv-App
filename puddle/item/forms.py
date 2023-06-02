from django import forms

from .models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'brewery', 'city', 'state',
                  'description', 'abv', 'ibu', 'image', 'quantity')
