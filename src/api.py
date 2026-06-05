# src/api.py
from flask import Flask, request, jsonify
from src.billing import calcular_tarifa

app = Flask(__name__)


@app.route("/tarifa")
def tarifa():
    minutos = int(request.args.get("minutos", 0))
    vip = request.args.get("vip", "false").lower() == "true"
    resultado = calcular_tarifa(minutos, vip)
    return jsonify({"minutos": minutos, "vip": vip, "tarifa": resultado})


if __name__ == "__main__":
    app.run(port=8000)