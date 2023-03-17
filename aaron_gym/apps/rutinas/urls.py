from django.urls import path
from . import views

app_name = 'rutinas'


urlpatterns = [
      path('', views.categorias_all, name = 'rutinas'),
      path('Rutinas/<int:pk>', views.rutinas_all, name = 'rutinasCategoria'),
]