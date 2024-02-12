from django import forms

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