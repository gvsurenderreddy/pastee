from django import forms
from django.utils import timezone
from .models import Paste
import random
import string


class PasteForm(forms.ModelForm):

    paste_text = forms.Textarea

    class Meta:
        model = Paste

        fields = ('paste_text',)
