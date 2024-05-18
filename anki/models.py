from django.db import models

# Create your models here.


class AnkiCards(models.Model):
    name_cards = models.CharField("Название карточки", max_length=50)
    description = models.TextField("Описание карточки")

    def __str__(self):
        return self.name_cards

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"
