from django import forms
from .helpers import prettyoutput


class PasteForm(forms.Form):

    paste_text = forms.CharField(label='Content', widget=forms.Textarea)
    paste_language = forms.ChoiceField(label='Language', widget=forms.Select, choices=prettyoutput())

