from django import forms
from default.models import Product

class HirdetesForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'feladocim', 'feladoorszag', 'kategoria', 'description', 'image', 'terms_checkbox']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: Samsung Galaxy S21'}),
            'price': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'pl: 15000'}),
            'feladocim': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: 9012 Győr, Kalapos utca 12.'}),
            'feladoorszag': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: Magyarország'}),
            'kategoria': forms.Select(),
            'description': forms.TextInput(attrs={'class': 'input-field', 'placeholder': ''}),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['terms_checkbox'].label = 'Elfogadom a szerződési feltételeket'
        self.fields['kategoria'].choices = Product.KATEGORIA_CHOICES