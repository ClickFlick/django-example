from django import forms
from home.models import Order,Sponsor


class NewOrder(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',

        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    date = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'type': 'date'
        }
    ))

    class Meta:
        model = Order
        fields = ['title', 'first_name', 'email', 'date', 'payment_method']


class SponsorContact(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',

        }
    ))

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',

        }
    ))

    class Meta:
        model = Sponsor
        fields = ['email', 'name']
