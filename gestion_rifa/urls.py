from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_rifa, name='index_rifa'),
    path(
        'actualizar/<int:numero_id>/',
        views.actualizar_numero,
        name='actualizar_numero',
    ),
    path(
        'pagar-lista/<int:lista_id>/',
        views.pagar_lista_completa,
        name='pagar_lista_completa',
    ),
    path(
        'registrar-pago/<int:numero_id>/',
        views.registrar_pago,
        name='registrar_pago',
    ),
]
    
    