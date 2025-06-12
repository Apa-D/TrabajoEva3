from django.urls import path, include
from . import views

urlpatterns = [
    # URLs Públicas
    path('', views.vista_publica, name='home'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registro/', views.registro, name='registro'),


    path('dashboard/', views.dashboard, name='dashboard'),
    path('notas/crear/', views.crear_nota, name='crear_nota'),
    path('notas/<int:nota_id>/eliminar/', views.eliminar_nota, name='eliminar_nota'),

]