from django import forms
from .models import UploadedFile
from django.contrib.auth.models import User

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = [ 'file']
