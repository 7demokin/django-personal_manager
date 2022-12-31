from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        exclude = ('date',)
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.TextInput(attrs={'class':'form-control'}),
            'estimated_end' : forms.DateInput(attrs={'class':'form-control'}),
            'priority' : forms.NumberInput(attrs={'class':'form-control'})
        }
