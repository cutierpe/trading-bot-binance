"""
model.py
--------

Placeholder de modelo de Machine Learning.

En producción aquí podrías cargar un modelo real
(RandomForest, XGBoost, LSTM, etc). Para esta DEMO,
calculamos una probabilidad basada en el momentum.
"""

from typing import List
import numpy as np


def ml_predict_direction(prices: List[float]) -> float:
    """
    Devuelve una probabilidad entre 0 y 1 de movimiento alcista.

    - > 0.6  → sesgo alcista fuerte
    - < 0.4  → sesgo bajista fuerte
    """
    if len(prices) < 30:
        return 0.5

    arr = np.array(prices, dtype=float)
    short = arr[-10:].mean()
    long = arr[-30:].mean()

    momentum = short - long
    prob = 0.5 + np.tanh(momentum / max(long, 1e-9)) * 0.25  # rango aprox 0.25–0.75
    prob = float(max(0.0, min(1.0, prob)))
    return prob
