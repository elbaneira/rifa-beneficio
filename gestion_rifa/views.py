from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import ListaRifa, NumeroRifa


def index_rifa(request):
  # Filtramos por si usan el buscador de listas
  query_lista = request.GET.get('lista')
  filtro_estado = request.GET.get('filtro')  # Recibimos el parámetro de filtro
  
  listas = ListaRifa.objects.all().order_by('numero_lista')

  if query_lista:
    listas = listas.filter(numero_lista=query_lista)

    # Si el usuario quiere ver solo las que tienen números disponibles
  # (Una lista tiene disponibles si al menos uno de sus 10 números tiene pagado = False)
  if filtro_estado == 'disponibles':
    # Filtramos las listas que contengan al menos un número no pagado
    listas = [
        lista for lista in listas if lista.numeros.filter(pagado=False).exists()
    ]

  context = {
      'listas': listas,
      'query_lista': query_lista,
      'filtro_estado': filtro_estado,
  }
  return render(request, 'gestion_rifa/index.html', context)


def actualizar_numero(request, numero_id):
  numero_rifa = get_object_or_404(NumeroRifa, id=numero_id)

  if request.method == 'POST':
    nombre = request.POST.get('nombre_comprador', '').strip()
    celular = request.POST.get('celular_comprador', '').strip()
    pagado = request.POST.get('pagado') == 'on'

    numero_rifa.nombre_comprador = nombre if nombre else None
    numero_rifa.celular_comprador = celular if celular else None

    # Si pasa de no pagado a pagado, guardamos la fecha y hora actual
    if pagado and not numero_rifa.pagado:
      numero_rifa.fecha_pago = timezone.now()
    elif not pagado:
      numero_rifa.fecha_pago = None  # Si lo desmarcan, se borra la fecha

    numero_rifa.pagado = pagado
    numero_rifa.save()

  # Redirigimos de vuelta a la página principal
  return redirect('index_rifa')

def pagar_lista_completa(request, lista_id):
  lista_rifa = get_object_or_404(ListaRifa, id=lista_id)

  if request.method == 'POST':
    nombre = request.POST.get('nombre_comprador_global', '').strip()
    celular = request.POST.get('celular_comprador_global', '').strip()

    if nombre:  # Si ingresaron un nombre
      ahora = timezone.now()
      # Actualiza de un solo golpe los 10 números de esta lista
      lista_rifa.numeros.all().update(
          nombre_comprador=nombre,
          celular_comprador=celular if celular else None,
          pagado=True,
          fecha_pago=ahora,
      )

  return redirect('index_rifa')


def registrar_pago(request, numero_id):
    numero = get_object_or_404(NumeroRifa, id=numero_id)
    if request.method == 'POST':
        metodo = request.POST.get('metodo_pago')
        numero.metodo_pago = metodo
        numero.pagado = True
        numero.save()
    return redirect('registrar_pago')

