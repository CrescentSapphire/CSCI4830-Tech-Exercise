from django_tables2 import data
from .tables import BoardgameTable
from .models import Boardgame
from .forms import BoardgameForm
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def index(request):
    games = Boardgame.objects.all()
    gametable = BoardgameTable(games)
    data_dict = {
        'table': gametable,
    }
    return render(request, 'games/index.html', data_dict)

def add(request):
    if request.method == 'POST':
        form = BoardgameForm(request.POST)
        if form.is_valid():
            return redirect(index)
    else:
        form = BoardgameForm()
    data_dict = {
        'form': form
    }
    return render(request, 'games/add.html', data_dict)

