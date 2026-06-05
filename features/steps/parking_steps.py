# features/steps/parking_steps.py
from pytest_bdd import given, when, then, parsers
from src.billing import calcular_tarifa


@given(parsers.parse("que un cliente estuvo {minutos:d} minutos en el parqueadero"))
def cliente_normal(minutos):
    return {"minutos": minutos, "vip": False}


@given(parsers.parse("que un cliente VIP estuvo {minutos:d} minutos en el parqueadero"))
def cliente_vip(minutos):
    return {"minutos": minutos, "vip": True}


@when("se calcula la tarifa")
def se_calcula(context):
    context["resultado"] = calcular_tarifa(context["minutos"], context["vip"])


@then(parsers.parse("el cobro es {esperado:d} pesos"))
def verificar_cobro(context, esperado):
    assert context["resultado"] == esperado