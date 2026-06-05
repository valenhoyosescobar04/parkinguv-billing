# language: es
Característica: Facturación de ParkingUV
  Como gerente de ParkingUV
  Quiero que el sistema calcule el cobro correcto
  Para garantizar tarifas justas a los clientes

  Escenario: Cliente que sale antes de 30 minutos no paga
    Dado que un cliente estuvo 20 minutos en el parqueadero
    Cuando se calcula la tarifa
    Entonces el cobro es 0 pesos

  Escenario: Cliente que pasa exactamente 30 minutos no paga
    Dado que un cliente estuvo 30 minutos en el parqueadero
    Cuando se calcula la tarifa
    Entonces el cobro es 0 pesos

  Escenario: Cliente que pasa 90 minutos paga por 2 horas
    Dado que un cliente estuvo 90 minutos en el parqueadero
    Cuando se calcula la tarifa
    Entonces el cobro es 1000 pesos

  Escenario: El cobro no supera el tope diario de 12000
    Dado que un cliente estuvo 1440 minutos en el parqueadero
    Cuando se calcula la tarifa
    Entonces el cobro es 12000 pesos

  Escenario: Cliente VIP recibe 20% de descuento
    Dado que un cliente VIP estuvo 90 minutos en el parqueadero
    Cuando se calcula la tarifa
    Entonces el cobro es 800 pesos