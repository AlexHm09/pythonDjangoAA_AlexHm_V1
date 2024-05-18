from django.shortcuts import render
from .models import AnkiCards


# Create your views here.
def index(request):
    table_cards = AnkiCards.objects.order_by('-id')
    return render(request, 'anki/index.html', {'title': 'Главная страница сайта', 'cards': table_cards})  # Главная страница


def cards(request):
    return render(request, 'anki/cards.html')   # Карточки
