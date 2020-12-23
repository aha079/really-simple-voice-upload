from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a voice',
        help_text='max. 20 megabytes'
    )