from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html')
# a pasta 'recipes' foi criada para evitar confusão de diretório de pastas
