# tests/test_billing.py
import pytest
from src.billing import calcular_tarifa


class TestPrimerMedia:
    def test_0_minutos_es_gratis(self):
        assert calcular_tarifa(0) == 0

    def test_15_minutos_es_gratis(self):
        assert calcular_tarifa(15) == 0

    def test_30_minutos_es_gratis(self):
        assert calcular_tarifa(30) == 0


class TestCobrosBasicos:
    def test_31_minutos_cobra_una_fraccion(self):
        assert calcular_tarifa(31) == 500

    def test_60_minutos_cobra_una_hora(self):
        assert calcular_tarifa(60) == 500

    def test_61_minutos_cobra_dos_fracciones(self):
        assert calcular_tarifa(61) == 1000

    def test_90_minutos_cobra_dos_horas(self):
        assert calcular_tarifa(90) == 1000

class TestTopeDiario:
    """Regla: máximo $12.000 por 24 horas"""

    def test_24_horas_cobra_tope_maximo(self):
        assert calcular_tarifa(1440) == 12_000

    def test_mas_de_24_horas_no_supera_tope(self):
        assert calcular_tarifa(2000) == 12_000

    def test_justo_antes_del_tope(self):
        # 23 horas y 30 min cobrables = 23 horas → 23*500 = 11.500
        assert calcular_tarifa(23 * 60 + 30) == 11_500


class TestClienteVIP:

    def test_vip_paga_80_por_ciento(self):
        # 2 horas = $1000, con 20% descuento = $800
        assert calcular_tarifa(150, vip=True) == 800

    def test_vip_respeta_tope_diario(self):
        # Sin VIP ya estaría en tope. Con descuento no lo supera pero el tope aplica
        assert calcular_tarifa(1440, vip=True) == 9_600

    def test_no_vip_paga_precio_normal(self):
        assert calcular_tarifa(90) == 1_000

