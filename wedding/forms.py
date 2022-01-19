from django import forms
from django.conf import settings
from django.forms import ModelForm
from wedding.models import Guest, Invitation
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm


class AccessForm(forms.Form):
    password = forms.CharField(label='', widget=forms.PasswordInput())

    """Defines a form to enter a password for accessing locked down content."""
    # pylint: disable=keyword-arg-before-vararg
    def __init__(self, passwords=None, *args, **kwargs):
        """Initialize the form by setting the valid passwords."""
        super().__init__(*args, **kwargs)
        if passwords is None:
            passwords = getattr(settings, 'LOCKDOWN_PASSWORDS', ())
            if not isinstance(passwords, (tuple, list)):
                passwords = (passwords,) if passwords else ()

        self.valid_passwords = passwords

    def clean_password(self):
        """Check that the password is valid."""
        value = self.cleaned_data.get('password')
        if value not in self.valid_passwords:
            raise forms.ValidationError('Incorrect password.')
        return value

    def generate_token(self):
        """Save the password as the authentication token.
        It's acceptable to store the password raw, as it is stored server-side
        in the user's session.
        """
        return self.cleaned_data['password']

    def authenticate(self, token_value):
        """Check that the password is valid.
        This allows for revoking of a user's preview rights by changing the
        valid passwords.
        """
        return token_value in self.valid_passwords

    def show_form(self):
        """Show the form if there are any valid passwords."""
        return bool(self.valid_passwords)


class InterestForm(forms.Form):
    Name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Name'}))
    Email= forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    Phone= forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Phone'}))
    Street_Address = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Street Address'}))
    Street_Address_Line_2 = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Street Address Line 2'}))
    City = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'City'}))
    State = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'State'}))
    Country = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Country'}))
    Zipcode = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Zipcode'}))

class SearchForm(forms.Form):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Search'}))

class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = ('food_allergies',)

class InviteForm(ModelForm):
    class Meta:
        model = Invitation
        yes_no = forms.RadioSelect(choices=[(True,'I will attend'),(False,'I will not attend')])
        fields = ('attending',)
        widgets = {'attending':yes_no}


