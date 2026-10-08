from django.contrib import admin
from .models import ListaRifa, NumeroRifa

class NumeroRifaInline(admin.TabularInline):
    model = NumeroRifa
    extra = 0  # No agrega filas vacías extra
    # Agregamos 'metodo_pago' aquí para que se vea y edite dentro de la lista
    fields = ('numero', 'nombre_comprador', 'celular_comprador', 'pagado', 'metodo_pago', 'fecha_pago')

@admin.register(NumeroRifa)
class NumeroRifaAdmin(admin.ModelAdmin):
    # Agregamos 'metodo_pago' para verlo en la tabla principal de números
    list_display = ('lista', 'numero', 'nombre_comprador', 'celular_comprador', 'pagado', 'metodo_pago', 'fecha_pago')
    # Opcional: puedes agregarlo a los filtros laterales para buscar por método de pago
    list_filter = ('pagado', 'metodo_pago', 'lista')
    search_fields = ('nombre_comprador', 'celular_comprador', 'numero')

@admin.register(ListaRifa)
class ListaRifaAdmin(admin.ModelAdmin):
    list_display = ('numero_lista',)
    inlines = [NumeroRifaInline]

