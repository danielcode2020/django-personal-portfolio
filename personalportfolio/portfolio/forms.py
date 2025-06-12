from django import forms
from .models import CVSection

class CVSectionForm(forms.ModelForm):
    class Meta:
        model = CVSection
        fields = ['header', 'content', 'order']
        widgets = {
            'header': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }