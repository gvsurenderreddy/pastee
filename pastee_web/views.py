from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Paste
from .forms import PasteForm
from .helpers import *

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

            write_file(form.cleaned_data['paste_text'], rand_name)

            paste.save()

            return render(request, 'index.html', {'paste_name': paste.paste_name})
        else:
            print(form.errors)
    else:
        form = PasteForm()

    return render(request, 'add.html', {'form': form})


def view_paste(request, paste_name):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/pastee_web/pastes/'

    with open(path + paste_name) as f:
        paste = f.read()

    return render(request, 'detail.html', {'paste': paste})

