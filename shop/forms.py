from django import forms
from default.models import Product

class HirdetesForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'feladocim', 'feladoorszag', 'kategoria', 'allapot', 'description', 'image', 'terms_checkbox']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: Samsung Galaxy S21'}),
            'price': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: 15000'}),
            'feladocim': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: 9012 Győr, Kalapos utca 12.'}),
            'feladoorszag': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: Magyarország'}),
            'kategoria': forms.Select(),  # No need to provide choices here
            'allapot': forms.Select(),     # No need to provide choices here
            'description': forms.TextInput(attrs={'class': 'input-field', 'placeholder': ''}),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
        }

    def __init__(self, *args, **kwargs):
        super(HirdetesForm, self).__init__(*args, **kwargs)
        self.fields['terms_checkbox'].label = 'Elfogadom a szerződési feltételeket'

    def __init__(self, *args, **kwargs):
        super(HirdetesForm, self).__init__(*args, **kwargs)
        # Set the choices for kategoria and allapot fields
        self.fields['kategoria'].choices = Product.KATEGORIA_CHOICES
        self.fields['allapot'].choices = Product.ALLAPOT_CHOICES