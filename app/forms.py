from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField()
    #columns = forms.CharField(label='Column',widget=forms.Select(choices=Column_Choices))

#class HeaderChoiceForm(forms.Form):
