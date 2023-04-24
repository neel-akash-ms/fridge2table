from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Ingredient

@login_required(login_url="/login")
def home(request):
    ingredients = Ingredient.objects.all()
    fake_recipes = []

    if request.method == 'POST':
        print(dict(request.POST).get("ingredients", []))
        fake_recipes.append({"id": 1, "name": "fake recipe", "description": "fake stuff", "procedure": "more fake shit to add"})

    return render(request, 'main/home.html', {"ingredients": ingredients, "recipes": fake_recipes})

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