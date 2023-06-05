from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'brewery', 'city', 'state',
                  'description', 'abv', 'ibu', 'image', 'quantity')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'brewery': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'city': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'state': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'abv': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'ibu': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'quantity': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'brewery', 'city', 'state',
                  'description', 'abv', 'ibu', 'image', 'quantity')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'brewery': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'city': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'state': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'abv': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'ibu': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'quantity': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        }
