from django.urls import path
from . import views

app_name = 'videos'


urlpatterns = [
      path('', views.videos_all, name = 'videos'),
]