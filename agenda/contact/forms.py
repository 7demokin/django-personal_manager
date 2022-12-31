from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        exclude = ('date',)
        
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    company = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
