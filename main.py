"""
======================================================
Binance Futures High-Frequency Trading Bot (HFT Demo)
======================================================

✔ Python 3.x
✔ Binance USDT-M Futures (estructura lista)
✔ Indicadores: EMA, RSI, Bollinger Bands
✔ Módulo de ML (placeholder)
✔ Gestión dinámica de TP y SL
✔ Arquitectura modular para producción

⚠ IMPORTANTE:
Este archivo es una DEMO para portafolio.
No ejecuta órdenes reales ni usa claves reales.
======================================================
"""

import time
import random
from typing import List, Tuple

import numpy as np

from indicators import ema, rsi, bollinger_bands
from model import ml_predict_direction
from risk import calc_take_profit, calc_stop_loss, calc_position_size


def generate_signal(prices: List[float]) -> Tuple[str, float]:
    """
    Lógica principal de la estrategia:
    - Cruce de EMAs
    - RSI
    - Bollinger Bands
    - Probabilidad de ML
    Devuelve: ("BUY" | "SELL" | "NO_SIGNAL", probabilidad)
    """
    if len(prices) < 60:
        return "NO_SIGNAL", 0.0

    ema_fast = ema(prices, 10)[-1]
    ema_slow = ema(prices, 30)[-1]
    rsi_val = rsi(prices)[-1]
    upper, mid, lower = bollinger_bands(prices)

    ml_prob = ml_predict_direction(prices)

    # Señal de compra
    if ema_fast > ema_slow and rsi_val > 55 and prices[-1] > mid and ml_prob > 0.6:
        return "BUY", ml_prob

    # Señal de venta
    if ema_fast < ema_slow and rsi_val < 45 and prices[-1] < mid and ml_prob < 0.4:
        return "SELL", ml_prob

    return "NO_SIGNAL", ml_prob


def fake_price_stream(n: int = 300) -> List[float]:
    """
    Genera una serie de precios simulada (solo para DEMO).
    En producción, aquí se conectaría al websocket de Binance.
    """
    base = 43000
    prices = []
    for i in range(n):
        noise = random.gauss(0, 15)
        wave = 120 * np.sin(i / 18)
        prices.append(base + wave + noise)
    return prices


def main_demo():
    print("🚀 Binance HFT Trading Bot — DEMO MODE (no live orders)")
    balance_usdt = 1000.0  # solo ejemplo para mostrar position sizing

    prices: List[float] = []
    for price in fake_price_stream(350):
        prices.append(price)

        signal, prob = generate_signal(prices)

        if signal != "NO_SIGNAL":
            # Cálculo de tamaño de posición según modo de riesgo
            qty = calc_position_size(balance_usdt, price, risk_mode="moderate")
            tp1, tp2, tp3 = calc_take_profit(price)
            sl = calc_stop_loss(price)

            print("\n🔔 SIGNAL DETECTED")
            print(f"Tipo      : {signal}")
            print(f"Precio    : {price:.2f} USDT")
            print(f"Confianza : {prob:.2f}")
            print(f"Cantidad  : {qty:.4f} contratos (modo moderate)")
            print(f"TP1: {tp1:.2f} | TP2: {tp2:.2f} | TP3: {tp3:.2f}")
            print(f"SL : {sl:.2f}")

        time.sleep(0.03)

    print("\n✅ DEMO completada. Arquitectura lista para conectar a Binance.")


if __name__ == "__main__":
    main_demo()

