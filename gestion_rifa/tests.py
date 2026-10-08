from django.test import TestCase
from django.urls import reverse

from .models import ListaRifa, NumeroRifa


class RifaPagosTest(TestCase):
    def setUp(self):
        self.lista = ListaRifa.objects.create(numero_lista=999)
        self.numero = NumeroRifa.objects.create(lista=self.lista, numero=1)

    def test_index_carga_sin_errores(self):
        response = self.client.get(reverse('index_rifa'))
        self.assertEqual(response.status_code, 200)

    def test_registrar_pago_efectivo_redirige_a_index(self):
        response = self.client.post(
            reverse('registrar_pago', args=[self.numero.id]),
            {'metodo_pago': 'efectivo'},
        )
        self.assertRedirects(response, reverse('index_rifa'))
        self.numero.refresh_from_db()
        self.assertTrue(self.numero.pagado)
        self.assertEqual(self.numero.metodo_pago, 'efectivo')
