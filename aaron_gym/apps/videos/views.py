from datetime import timezone
from django.shortcuts import render,redirect
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from .models import Cuerpo, Categoria, Video
from django.urls import reverse_lazy

def videos_all(request):
    videos = Video.objects.all()
    
    context ={'videos':videos}
              
    return render(request,'videos/videos.html',context)
