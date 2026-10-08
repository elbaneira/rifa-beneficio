from django.db import models

METODO_PAGO_CHOICES = [
    ('efectivo', 'Efectivo'),
    ('transferencia', 'Transferencia'),
]


class ListaRifa(models.Model):
    numero_lista = models.IntegerField(unique=True, verbose_name="N° de Lista")
    
    def __str__(self):
        return f"Lista N° {self.numero_lista}"

class NumeroRifa(models.Model):
    lista = models.ForeignKey(ListaRifa, on_delete=models.CASCADE, related_name="numeros", verbose_name="Lista")
    numero = models.IntegerField(verbose_name="Número (1 al 10)")
    nombre_comprador = models.CharField(max_length=150, blank=True, null=True, verbose_name="Nombre")
    celular_comprador = models.CharField(max_length=20, blank=True, null=True, verbose_name="Celular")
    fecha_pago = models.DateTimeField(blank=True, null=True, verbose_name="Fecha y Hora de Pago")
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO_CHOICES, blank=True, null=True)
    pagado = models.BooleanField(default=False, verbose_name="¿Pagado?")

    def __str__(self):
        estado = "Pagado 🟢" if self.pagado else "Pendiente ⚪"
        return f"Lista {self.lista.numero_lista} - N° {self.numero} | {self.nombre_comprador or 'Disponible'} ({estado})"   

    

#