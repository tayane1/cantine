from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PlatForm
from .models import Plat

def index(request):
    search_field = request.GET.get('search')
    if search_field:
        plats = Plat.objects.filter(name__icontains=search_field)
        context = {'plats': plats, 'search_field': search_field}
    else:
        plats = Plat.objects.all()
        numbers_plats = plats.count()
        context = {
            'plats': plats,
            'numbers_plats': numbers_plats,
        }
    return render(request, 'plat/plats.html', context)

def add_plat(request):
    if request.method == 'POST':
        plat_form = PlatForm(request.POST)
        if plat_form.is_valid():
            plat_form.save()
            messages.success(request, 'Le plat est ajouté avec succès')
            return redirect('plat:index')
        else:
            messages.error(request, 'Erreur lors de l\'ajout du plat')
            return render(request, 'plat/add_plat.html', {'form': plat_form})
        
    plat_form = PlatForm()
    context = {'form': plat_form, 'title': 'Ajouter un plat'}
    return render(request, 'plat/add_plat.html', context)

def update_plat(request, id):
    plat = get_object_or_404(Plat, id=id)
    
    if request.method == 'POST':
        plat_form = PlatForm(request.POST, instance=plat)
        if plat_form.is_valid():
            plat_form.save()
            messages.success(request, 'Le plat a bien été modifié')
            return redirect('plat:index')
        else:
            messages.error(request, 'Erreur lors de la modification du plat')
            return render(request, 'plat/add_plat.html', {'form': plat_form})
        
    plat_form = PlatForm(instance=plat)
    context = {'form': plat_form, 'title': 'Modification du plat'}
    return render(request, 'plat/add_plat.html', context)

def delete_plat(request, id):
    plat = get_object_or_404(Plat, id=id)
    plat.delete()
    messages.success(request, 'Le plat a été supprimé avec succès')
    return redirect('plat:index')
