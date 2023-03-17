from datetime import timezone
from django.shortcuts import render,redirect
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from .models import Cuerpo, Categoria, Video
from django.urls import reverse_lazy

def videos_all(request):
    categoria = Categoria.objects.all()
    cuerpo = Cuerpo.objects.all()
    
    context ={'categoria':categoria,
              'cuerpo':cuerpo}
              
    return render(request,'videos/videos.html',context)


def videosCategoria_all(request,pk):
    
    videos = Video.objects.all().filter(categoria = pk)
    
    context = {'videos':videos}
    
    return render(request,'videos/videoCategoria.html',context)