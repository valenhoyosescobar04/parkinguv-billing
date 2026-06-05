# src/billing.py
import math

MINUTOS_GRATIS = 30
TARIFA_POR_HORA = 500
TOPE_DIARIO = 12_000


def calcular_tarifa(minutos: int, vip: bool = False) -> int:
 
    if minutos <= MINUTOS_GRATIS:
        return 0

    minutos_cobrables = minutos - MINUTOS_GRATIS
    horas = math.ceil(minutos_cobrables / 60)
    total = horas * TARIFA_POR_HORA

    if vip:
        total = total * 0.80  # 20% de descuento

    total = min(total, TOPE_DIARIO)

    return int(total)