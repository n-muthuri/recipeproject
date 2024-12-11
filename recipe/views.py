from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Recipe
from django.contrib.auth.decorators import login_required

from .models import Blog

# Index View - Display all recipes
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

# About View
def about(request):
    return render(request, 'about.html')

# Contact Us View
def contact(request):
    return render(request, 'contact.html')

# Blog View
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

# Login View
def login_view(request):
    return render(request, 'login.html')

def add_recipe(request):
    return render(request, 'add_recipe.html')

def blog_detail(request):
    return render(request, 'blog_detail.html')

# Register View - For user registration
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Recipe CRUD Operations

# RecipeCreateView - For creating a new recipe
class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title', 'description']
    template_name = 'add_recipe.html'
    success_url = reverse_lazy('index')

# RecipeUpdateView - For updating an existing recipe
class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'description']
    template_name = 'add_recipe.html'
    success_url = reverse_lazy('index')

# RecipeDeleteView - For deleting a recipe
class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipe_confirm_delete.html'
    success_url = reverse_lazy('index')

