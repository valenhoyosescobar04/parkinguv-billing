# tests/test_billing.py
import pytest
from src.billing import calcular_tarifa


class TestPrimerMedia:
    """Regla: primeros 30 minutos gratis"""

    def test_0_minutos_es_gratis(self):
        assert calcular_tarifa(0) == 0

    def test_15_minutos_es_gratis(self):
        assert calcular_tarifa(15) == 0

    def test_30_minutos_es_gratis(self):
        assert calcular_tarifa(30) == 0


class TestCobrosBasicos:
    """Regla: desde minuto 31, $500 por hora o fracción"""

    def test_31_minutos_cobra_una_fraccion(self):
        assert calcular_tarifa(31) == 500

    def test_90_minutos_cobra_una_hora(self):
        # 90 - 30 gratis = 60 cobrables → ceil(60/60) = 1 hora → $500
        assert calcular_tarifa(90) == 500

    def test_91_minutos_cobra_dos_horas(self):
        # 91 - 30 gratis = 61 cobrables → ceil(61/60) = 2 horas → $1000
        assert calcular_tarifa(91) == 1000

    def test_150_minutos_cobra_dos_horas_exactas(self):
        # 150 - 30 gratis = 120 cobrables → ceil(120/60) = 2 horas → $1000
        assert calcular_tarifa(150) == 1000


class TestTopeDiario:
    """Regla: máximo $12.000 por 24 horas"""

    def test_24_horas_cobra_tope_maximo(self):
        assert calcular_tarifa(1440) == 12_000

    def test_mas_de_24_horas_no_supera_tope(self):
        assert calcular_tarifa(2000) == 12_000

    def test_justo_antes_del_tope(self):
        # 1410 - 30 = 1380 cobrables → ceil(1380/60) = 23 horas → 23*500 = 11.500
        assert calcular_tarifa(1410) == 11_500


class TestClienteVIP:
    """Regla: VIP tiene 20% de descuento antes del tope"""

    def test_vip_paga_80_por_ciento(self):
        # 150 min → 120 cobrables → 2 horas → $1000 × 0.8 = $800
        assert calcular_tarifa(150, vip=True) == 800

    def test_vip_respeta_tope_diario(self):
        # Sin descuento sería $12.000, con 20% = $9.600
        assert calcular_tarifa(1440, vip=True) == 9_600

    def test_no_vip_paga_precio_normal(self):
        assert calcular_tarifa(91) == 1_000


class TestValoresLimite:
    """
    Tabla de partición de equivalencia y valores límite

    Partición 1 — Gratis:       [0, 30]
    Partición 2 — Cobro normal: [31, 1440]
    Partición 3 — Tope diario:  [1441, ∞]

    Valores límite clave: 0, 30, 31, 90, 91, 1440, 1441
    """

    @pytest.mark.parametrize("minutos,vip,esperado", [
        (0,    False, 0),        # mínimo absoluto
        (29,   False, 0),        # un minuto antes del límite gratis
        (30,   False, 0),        # exactamente el límite gratis
        (31,   False, 500),      # primer minuto cobrable → 1 fracción
        (90,   False, 500),      # 60 min cobrables → exactamente 1 hora
        (91,   False, 1_000),    # 61 min cobrables → entra en 2da hora
        (1440, False, 12_000),   # exactamente 24h = tope
        (1441, False, 12_000),   # supera el tope → sigue en tope
        (90,   True,  400),      # VIP: $500 × 0.8 = $400
        (1440, True,  9_600),    # VIP con tope: $12.000 × 0.8 = $9.600
    ])
    def test_tabla_equivalencia(self, minutos, vip, esperado):
        assert calcular_tarifa(minutos, vip) == esperado