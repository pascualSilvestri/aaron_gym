from django.urls import path
from . import views

app_name = 'rutinas'


urlpatterns = [
      path('', views.rutinas_all, name = 'rutinas'),
]