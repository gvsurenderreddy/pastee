from django import forms


class PasteForm(forms.Form):

    paste_text = forms.CharField(label='Content', widget=forms.Textarea)
