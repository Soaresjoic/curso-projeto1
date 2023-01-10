from django.shortcuts import render
from utils.recipes.factory import make_recipe


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })

# a função importada make_recipes vai criar dados aleatórios para nosso
# formulário.Nesse caso, irá gerar 10 receitas aleatórias para a home


# a pasta 'recipes' foi criada para evitar confusão de diretório de pastas


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
