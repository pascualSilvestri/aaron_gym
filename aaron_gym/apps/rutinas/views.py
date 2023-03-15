from datetime import timezone
from django.shortcuts import render,redirect
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from .models import Cuerpo, Categoria, Rutina
from django.urls import reverse_lazy

def rutinas_all(request):
    rutinas = Rutina.objects.all()
    
    context ={'rutinas':rutinas}
              
    return render(request,'rutinas/rutinas.html',context)
