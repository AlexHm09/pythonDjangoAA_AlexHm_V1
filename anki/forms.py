from .models import AnkiCards
from django.forms import ModelForm, TextInput, Textarea


class AnkiCardsForm(ModelForm):
    class Meta:
        model = AnkiCards
        fields = ["name_cards", "description"]
        widgets = {
            "name_cards": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите название карточки"
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите описание карточки"
            }),
        }
