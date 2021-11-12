from django import forms
from . models import Page



class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }

class PageEditForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }