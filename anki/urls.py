from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
        path('admin', admin.site.urls),
        path('', views.index, name='index'),
        path('cards', views.cards, name='cards'),
        path('create', views.create, name='create')
]
