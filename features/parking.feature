Feature: Facturación de ParkingUV
  As a gerente de ParkingUV
  I want the system to calculate the correct charge
  So that clients are billed fairly

  Scenario: Cliente que sale antes de 30 minutos no paga
    Given un cliente estuvo 20 minutos en el parqueadero
    When se calcula la tarifa
    Then el cobro es 0 pesos

  Scenario: Cliente que pasa exactamente 30 minutos no paga
    Given un cliente estuvo 30 minutos en el parqueadero
    When se calcula la tarifa
    Then el cobro es 0 pesos

  Scenario: Cliente que pasa 91 minutos paga por 2 horas
    Given un cliente estuvo 91 minutos en el parqueadero
    When se calcula la tarifa
    Then el cobro es 1000 pesos

  Scenario: El cobro no supera el tope diario de 12000
    Given un cliente estuvo 1440 minutos en el parqueadero
    When se calcula la tarifa
    Then el cobro es 12000 pesos

  Scenario: Cliente VIP recibe 20% de descuento
    Given un cliente VIP estuvo 150 minutos en el parqueadero
    When se calcula la tarifa
    Then el cobro es 800 pesos