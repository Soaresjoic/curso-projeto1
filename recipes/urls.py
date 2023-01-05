from django.urls import path

from recipes.views import contatos, home, sobre

urlpatterns = [
    path('', home),  # home
    path('sobre/', sobre),  # /sobre/
    path('contatos/', contatos),  # /contatos/
]
