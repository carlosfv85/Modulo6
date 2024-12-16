from django.urls import path

from . import views


urlpatterns = [
    path('add', views.VehiculoCreateView.as_view(), name= 'create_vehiculo'),
    path('detail', views.VehiculoView.as_view(), name= 'listar_vehiculos'),
]