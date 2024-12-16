from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import Permission 


#vista de registro 
class UserRegistroView(CreateView):
    form_class =  UserCreationForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        usuario = form.instance #   Obtenemos la instancia de la clase User
        
        permiso = Permission.objects.get(codename ="visualizar_catalogo" ) #Obtener permiso desde la base de datos
        
        usuario.user_permissions.add(permiso) #Le agregamos el permiso al usuario
        
        usuario.save()
    
        messages.success(self.request, 'Registro realizo con éxito.')
        return response
    

#vista de login   
class UserLoginView(LoginView):
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')
   
    def form_valid(self, form):
        messages.success(self.request, 'Login exitoso.')
        return super().form_valid(form)
   
    # una vez ingresado el usuario, djando redirecciona predeterminadamente a la url ../accounts/profile
    # para evitar esto y redireccionar a otra pagina, en este caso la determinada en success_url, entonces hay 
    # que crear la siguiente funcion:
    
    def get_success_url(self) -> str:
        return self.get_redirect_url() or self.success_url
    
 
#vista de logout    
class UserLogoutView(LogoutView):
    next_page = 'index'
   
    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, 'Ha cerrado la sesión exitosamente.')
        return super().dispatch(request, *args, **kwargs)      