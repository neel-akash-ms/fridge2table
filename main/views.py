from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Ingredient
from .core.non_personal import non_personalized_rec

@login_required(login_url="/login")
def home(request):
    ingredients = []
    hiddenchosen = ""
    if request.method == 'POST':
        q = "%" + request.POST.get("query", "") + "%"
        hiddenchosen = request.POST.get("hiddenchosen", "")
        if q == "%%":
            return render(request, 'main/home.html', {"ingredients": ingredients, "hiddenchosen": hiddenchosen})
        for i in Ingredient.objects.raw("SELECT id,name FROM main_ingredient WHERE name LIKE %s", [q]):
            ingredients.append(i)

    return render(request, 'main/home.html', {"ingredients": ingredients, "hiddenchosen": hiddenchosen})

@login_required(login_url="/login")
def results(request):
    recipes = {
        'exact_recipes': [],
        'low_cal': [],
        'few_steps': [],
        'order_by_time': []
    }
    if request.method == 'POST':
        ingredients = []
        chosen = request.POST.get("chosen", "")
        if len(chosen) > 0:
            ingredients = ingredients + chosen.split(",")
        recipes = non_personalized_rec(ingredients)

    return render(request, 'main/results.html', recipes)

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})