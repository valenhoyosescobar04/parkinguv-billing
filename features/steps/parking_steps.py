# features/steps/parking_steps.py
import pytest
from pytest_bdd import given, when, then, parsers, scenarios
from src.billing import calcular_tarifa


@given(parsers.parse("un cliente estuvo {minutos:d} minutos en el parqueadero"), target_fixture="contexto")
def cliente_normal(minutos):
    return {"minutos": minutos, "vip": False}


@given(parsers.parse("un cliente VIP estuvo {minutos:d} minutos en el parqueadero"), target_fixture="contexto")
def cliente_vip(minutos):
    return {"minutos": minutos, "vip": True}


@when("se calcula la tarifa", target_fixture="contexto")
def se_calcula(contexto):
    contexto["resultado"] = calcular_tarifa(contexto["minutos"], contexto["vip"])
    return contexto


@then(parsers.parse("el cobro es {esperado:d} pesos"))
def verificar_cobro(contexto, esperado):
    assert contexto["resultado"] == esperado