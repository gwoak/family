from django import forms
from . models import Post, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# from django_summernote.widgets import SummernoteWidget

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    
    choice_list.append(item)
choice_list.sort()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'snippet', 'date_created')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'style': 'text-transform: capitalize;'}),            
            'body': CKEditorUploadingWidget(),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'date_created': forms.DateTimeInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'title_tag': 'Tag label that appears on the browser tab - change if desired',
            'snippet': 'Extract for summary page: max 255 characters',
            'date_created': 'Date created - change if desired',
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'header_image', 'body', 'snippet', 'date_created')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'style': 'text-transform: capitalize;'}),
            'body': CKEditorUploadingWidget(),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'date_created': forms.DateTimeInput(attrs={'class': 'form-control'}),

        }