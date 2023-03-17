from datetime import timezone
from django.shortcuts import render,redirect
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from .models import Cuerpo, Categoria, Rutina
from django.urls import reverse_lazy

def categorias_all(request):
    categoria = Categoria.objects.all()
    
    context ={
        'categoria':categoria
              }
              
    return render(request,'rutinas/rutinas.html',context)

def rutinas_all(request,pk):
    rutinas = Rutina.objects.all().filter(categoria = pk)
    
    context ={
        'rutinas':rutinas
              }
              
    return render(request,'rutinas/rutinasCategoria.html',context)
