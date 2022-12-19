from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipes_omlet(request):
    amount = int(request.GET.get("servings", 1))
    context = {
      'recipe': {
        'яйца, шт': 2 * amount,
        'молоко, л': 0.1 * amount,
        'соль, ч.л.': 0.5 * amount,
      }
    }
    return render(request, 'calculator/index.html', context)

def recipes_pasta(request):
    amount = int(request.GET.get("servings", 1))
    context = {
      'recipe': {
        'макароны, г': 0.3 * amount,
        'сыр, г': 0.05 * amount,
      }
    }
    return render(request, 'calculator/index.html', context)
