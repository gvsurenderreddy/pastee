from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Paste
from .forms import PasteForm

import random
import string


def index(request):
    return render(request, 'index.html')


def add_paste(request):
    if request.method == 'POST':
        form = PasteForm(request.POST)

        if form.is_valid():
            rand_name = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))

            paste = Paste()

            paste.paste_name = rand_name
            paste.created_at = timezone.now()
            paste.paste_text = form.cleaned_data['paste_text']

            paste.save()

            return added_paste(request, paste.paste_name)
        else:
            print(form.errors)
    else:
        form = PasteForm()

    return render(request, 'add.html', {'form': form})


def view_paste(request, paste_name):
    requested_paste = get_object_or_404(Paste, paste_name=paste_name)
    return render(request, 'detail.html', {'paste': requested_paste})


def added_paste(request, name):
    return render(request, 'index.html', {'paste_name': name})