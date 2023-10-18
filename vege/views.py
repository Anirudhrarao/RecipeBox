from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login_page')
def recipe(request):
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        recipe_img = request.FILES.get('recipe_img')

        try:
            if not recipe_name or not recipe_desc or not recipe_img:
                messages.error(request, 'Please fill in all fields and upload an image.')
            else:
                Recipe.objects.create(
                    name=recipe_name,
                    description=recipe_desc,
                    image=recipe_img
                )
                messages.success(request, 'Recipe created successfully.')
                return redirect('recipe') 
        
        except Exception as e:
            messages.error(request,f'An error ocurred: {str(e)}')
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains = request.GET.get('search'))
    return render(request, "recipe.html",context={'recipes':queryset,'page':'recipe'})

def delete_recipe(request,id):
    try:
        recipe = Recipe.objects.get(id=id)
        recipe.delete()
        messages.success(request, 'Recipe deleted successfully.')
        return redirect('recipe')
    except Recipe.DoesNotExist:
        messages.error(request, 'Recipe not found.')
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
    return redirect('recipe')
    
def update_recipe(request,id):
    try:
        recipe = Recipe.objects.get(id=id)
        if request.method == 'POST':
            data = request.POST
            recipe_name = data.get('recipe_name')
            recipe_desc = data.get('recipe_desc')
            recipe_img = request.FILES.get('recipe_img')
            recipe.name = recipe_name
            recipe.description = recipe_desc
            recipe.image = recipe_img
            if recipe_img:
                recipe.image = recipe_img
            recipe.save()
            messages.success(request, 'Recipe updated successfully.')
            return redirect('recipe')
        context = {'recipes': recipe}
        return render(request,'update_recipe.html',context)
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username')
            return redirect('login_page')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('recipe')
            else:
                messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def register_page(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.filter(username=username)
            if user.exists():
                messages.success(request,'Username already taken!')
                return redirect('register')
            user = User.objects.create(
                email = email,
                username = username
            )
            user.set_password(password)
            user.save()
            messages.success(request, f'Welcome {username} your registration done successful.')
            return redirect('recipe')
        return render(request,'register.html') 
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')


def logout_page(request):
    try:
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
        return redirect('recipe')
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')