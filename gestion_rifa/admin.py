from django.contrib import admin
from .models import ListaRifa, NumeroRifa

class NumeroRifaInline(admin.TabularInline):
    model = NumeroRifa
    extra = 0  # No agrega filas vacías extra, muestra exactos los 10 números
    fields = ('numero', 'nombre_comprador', 'celular_comprador', 'pagado', 'fecha_pago')

@admin.register(ListaRifa)
class ListaRifaAdmin(admin.ModelAdmin):
    list_display = ('numero_lista',)
    inlines = [NumeroRifaInline]

@admin.register(NumeroRifa)
class NumeroRifaAdmin(admin.ModelAdmin):
    list_display = ('lista', 'numero', 'nombre_comprador', 'celular_comprador', 'pagado')
    list_filter = ('pagado', 'lista')
    search_fields = ('nombre_comprador', 'celular_comprador', 'numero')