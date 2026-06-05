# locustfile.py
from locust import HttpUser, task, between


class ParkingUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task(3)
    def tarifa_normal(self):
        self.client.get("/tarifa?minutos=90&vip=false")

    @task(1)
    def tarifa_vip(self):
        self.client.get("/tarifa?minutos=120&vip=true")

    @task(1)
    def tarifa_larga(self):
        self.client.get("/tarifa?minutos=1440&vip=false")