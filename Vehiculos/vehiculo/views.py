from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Vehiculo
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.


class VehiculoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Vehiculo
    template_name ="vehiculos/create_vehiculo.html"
    fields = ["marca", "modelo", "serial_carroceria", "serial_motor", "categoria", "precio"]
    success_url = reverse_lazy('index')
    permission_required = 'vehiculo.add_vehiculo'

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.info(self.request, "Usted no tiene permisos para ingresar vehículos")
            return redirect("index") 
        else:
            messages.info(self.request, "Debe ingresar sesión para acceder a esta vista")
            return redirect("login")


class VehiculoView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Vehiculo
    template_name ="vehiculos/listar_vehiculos.html"
    context_object_name = "vehiculos"
    permission_required = 'vehiculo.visualizar_catalogo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.info(self.request, "Usted no tiene permisos ver el catalogo de vehículos")
            return redirect("index") 
        else:
            messages.info(self.request, "Debe ingresar sesión para acceder a esta vista")
            return redirect("login")
    
