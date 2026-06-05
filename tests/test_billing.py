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