from django import forms
from django.utils import translation
from django.utils.translation import gettext_lazy as _

from language_app.models import Language


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    from language_app.utils import choices

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))
    profile_image = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control', 'name': 'profile_image'}))
    language = forms.ChoiceField(choices=choices(),
                                 widget=forms.Select(attrs={'class': 'form-control', 'label': 'Language'}))

    def is_valid(self):
        from accounts_app.service import username_exists, email_exists
        data = self.data

        username = data.get('username')

        email = data.get('email')

        password = data.get('password')
        confirm_password = data.get('confirm_password')

        language = Language.objects.get(code=data.get('language'))
        translation.activate(language.code.lower())

        if username_exists(username):
            self.add_error('username', _('This username already taken'))
            return False

        if email_exists(email):
            self.add_error('email', 'This email already registered')
            return False

        if not password.__eq__(confirm_password):
            self.add_error('password', 'Password does not match')
            self.add_error('confirm_password', 'Password does not match')
            return False

        return True
