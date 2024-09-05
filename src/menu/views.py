from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MenuForm
from .models import Menu

# Create your views here.

def index(request):
    search_field = request.GET.get('search')
    if search_field:
        menus = Menu.objects.filter(plat__icontains=search_field)
        context = {'menus': menus, 'search_field': search_field}
    else:
        menus = Menu.objects.all()
        numbers_menus = menus.count()
        context = {
            'menus': menus,
            'numbers_menus': numbers_menus,
        }
    return render(request, 'menu/menus.html', context)
    
    

def add_menu(request):
    if request.method == 'POST':
        menu_form = MenuForm(request.POST)
        if menu_form.is_valid():
            menu_form.save()
            messages.success(request, 'Menu ajouter avec succès')
            return redirect('menu:index')
        else:
            messages.error(request, 'Erreur lors de l\'ajout du menu')
            return render (request, 'menu/forms.html')
            
    menu_form = MenuForm()
    context = {'form' : menu_form, 'title': 'Ajouter un menu',}
    return render(request, 'menu/forms.html', context)
    
    

def update_menu(request, id):
    menu = Menu.objects.get(id=id)
    
    if request.method == 'POST':
        menu_form = MenuForm(request.POST, instance=menu)
        if menu_form.is_valid():
            menu_form.save()
            messages.success(request, 'menu a bien été modifié')
            return redirect('menu:index')
        else:
            messages.error(request, 'Erreur lors de la modification du menu')
            return render(request, 'menu/forms.html', {'form': menu_form})
            
        menu_form = MenuForm(instance=menu)
        context = {'form': menu_form,
            'title': 'Modification du menu',
        
        }
        return render(request, 'menu/forms.html', context)
        
        

def delete_menu(request, id):
    menu = Menu.objects.get(id=id)
    menu.delete()
    messages.success(request, 'Menu supprimé avec succès')
    return redirect('menu:index')