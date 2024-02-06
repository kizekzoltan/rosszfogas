from django import forms

class HirdetesForm(forms.Form):
    ALLAPOT = [
        ('bontatlan', 'Bontatlan'),
        ('újszerű', 'Újszerű'),
        ('használt', 'Használt'),
        ('megviselt', 'Megviselt'),
    ]
    KATEGORIA = [
        ('autó', 'Autó'),
        ('élelmiszer', 'Élelmiszer'),
        ('egyéb', 'Egyéb'),
    ]

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Termék'}))
    price = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Ár'}))
    feladocim = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'pl.: 9012 Győr, Kalapos utca 6.'}))
    kategoria = forms.ChoiceField(choices=KATEGORIA)
    allapot = forms.ChoiceField(choices=ALLAPOT)
    leiras = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Leírás'}))
    kep = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple':False}))
    terms_checkbox = forms.BooleanField(required=True)

    def __init__(self, *args, **kwargs):
        super(HirdetesForm, self).__init__(*args, **kwargs)
        self.fields['terms_checkbox'].label = 'Elfogadom a szerződési feltételeket'