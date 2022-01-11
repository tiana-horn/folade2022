from django import forms

class InterestForm(forms.Form):
    Name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Name'}))
    Email= forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder':'Email'}))
