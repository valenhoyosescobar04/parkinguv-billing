# 🅿️ ParkingUV Billing

Módulo de facturación para ParkingUV S.A.S. construido con TDD y BDD.

## Reglas de negocio
- Primeros 30 minutos: **gratis**
- Del minuto 31 en adelante: **$500 por hora o fracción**
- Tope diario: **$12.000**
- Clientes VIP: **20% de descuento** (antes del tope)

## Cómo correr las pruebas localmente

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Pruebas unitarias (TDD)
```bash
pytest tests/test_billing.py -v
```

### 3. Pruebas BDD (Gherkin)
```bash
pytest tests/test_bdd.py -v
```

### 4. Seguridad (Bandit)
```bash
bandit -r src/ -ll
```

### 5. Rendimiento (Locust)
```bash
# Terminal 1 - levantar el servidor
python src/api.py

# Terminal 2 - correr Locust
locust -f locustfile.py --host http://localhost:8000
# Abre http://localhost:8089 en el navegador
```

## Pipeline CI/CD
- **Todo push**: ejecuta unitarias + BDD + seguridad
- **Solo main**: también ejecuta pruebas de rendimiento