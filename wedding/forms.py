from django import forms

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
