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
        fields = ['email', 'firstname', 'lastname', 'location', 'phone',]
        widgets = {
            'email': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: bimbo@gmail.com'}),
            'firstname': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: Varga'}),
            'lastname': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: Bimbó'}),
            'location': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: 9012 Győr, Kiss utca 1.'}),
            'phone': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'pl: +36201111111'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']