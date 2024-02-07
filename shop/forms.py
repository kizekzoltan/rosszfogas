from django import forms

class HirdetesForm(forms.Form):
    ALLAPOT = [
        ('--válasszon--', '--Válasszon--'),
        ('bontatlan', 'Bontatlan'),
        ('újszerű', 'Újszerű'),
        ('használt', 'Használt'),
        ('megviselt', 'Megviselt'),
    ]
    KATEGORIA = [
        ('--válasszon--', '--Válasszon--'),
        ('autó', 'Autó'),
        ('élelmiszer', 'Élelmiszer'),
        ('egyéb', 'Egyéb'),
    ]

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: Samsung Galaxy S21'}))
    price = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: 15000'}))
    feladocim = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: 9012 Győr, Kalapos utca 12.'}))
    feladoorszag = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: Magyarország'}))
    kategoria = forms.ChoiceField(choices=KATEGORIA)
    allapot = forms.ChoiceField(choices=ALLAPOT)
    leiras = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': ''}))
    kep = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple':False}))
    terms_checkbox = forms.BooleanField(required=True)

    def __init__(self, *args, **kwargs):
        super(HirdetesForm, self).__init__(*args, **kwargs)
        self.fields['terms_checkbox'].label = 'Elfogadom a szerződési feltételeket'