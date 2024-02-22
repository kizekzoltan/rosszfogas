from django import forms
from default.models import *

class RegistrationForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Email'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Felhasználónév'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Jelszó'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Jelszó újra'}))
    terms_checkbox = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['terms_checkbox'].label = 'Elfogadom a szerződési feltételeket'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Felhasználónév'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Jelszó'}))


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Email', 'Vezetéknév', 'Keresztnév', 'Lakcím', 'Telefonszám',]
        widgets = {
            'Email': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: bimbo@gmail.com'}),
            'Vezetéknév': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: Varga'}),
            'Keresztnév': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: Bimbó'}),
            'Lakcím': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: 9012 Győr, Kiss utca 1.'}),
            'Telefonszám': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: +36201111111'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'leiras']

    def clean_leiras(self):
        leiras = self.cleaned_data.get('leiras')
        if not leiras:
            return "*Ehhez a témához nem tartozik leírás*"
        return leiras
