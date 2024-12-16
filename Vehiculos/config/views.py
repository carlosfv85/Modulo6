from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from vehiculo.models import Vehiculo

# Create your views here.

class Vehiculosview(ListView):
    model = Vehiculo
    template_name ="index.html"
    context_object_name = "vehiculos"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Catalogo de Vehículos"
        return context