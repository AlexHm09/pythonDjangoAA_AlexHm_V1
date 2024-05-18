from django.shortcuts import render, redirect
from .models import AnkiCards
from .forms import AnkiCardsForm


# Create your views here.
def index(request):

    return render(request, 'anki/index.html')  # Главная страница


def cards(request):
    table_cards = AnkiCards.objects.order_by('-id')
    return render(request, 'anki/cards.html', {'title': 'Главная страница сайта', 'cards': table_cards})   # Карточки


def create(request):
    error = ""
    if request.method == "POST":
        form = AnkiCardsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "Неправильно заполнили форму, повторите попытку"
    form = AnkiCardsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'anki/create.html', context)   # Создание карточек
