from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm
from .models import Usuario


class Registro(CreateView):
#FORMULARIO DJANGO
    form_class = RegistroForm
    success_url = reverse_lazy('home')
    template_name = 'usuarios/registro.html'    


def usuario(request):
    usuario = Usuario.objects.all()
    
    context = {'usuario':usuario}
    
    return render(request,'usuarios/usuarios.html',context)