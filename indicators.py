"""
indicators.py
-------------

Módulo de indicadores técnicos usados por la estrategia.
Incluye:
- EMA
- RSI
- Bollinger Bands
"""

from typing import List, Tuple
import numpy as np


def ema(values: List[float], period: int) -> np.ndarray:
    """Exponential Moving Average."""
    if len(values) < period:
        return np.array([])

    weights = np.exp(np.linspace(-1.0, 0.0, period))
    weights /= weights.sum()
    return np.convolve(values, weights, mode="valid")


def rsi(values: List[float], period: int = 14) -> np.ndarray:
    """Relative Strength Index (RSI)."""
    values = np.array(values, dtype=float)
    if len(values) <= period:
        return np.zeros_like(values)

    deltas = np.diff(values)
    seed = deltas[:period]
    up = seed[seed >= 0].sum() / period
    down = -seed[seed < 0].sum() / period if (seed < 0).any() else 1e-9
    rs = up / down
    rsi_vals = np.zeros_like(values)
    rsi_vals[:period] = 100.0 - 100.0 / (1.0 + rs)

    up_avg, down_avg = up, down
    for i in range(period, len(values)):
        delta = deltas[i - 1]
        up_val = max(delta, 0)
        down_val = max(-delta, 0)
        up_avg = (up_avg * (period - 1) + up_val) / period
        down_avg = (down_avg * (period - 1) + down_val) / period
        rs = up_avg / (down_avg if down_avg != 0 else 1e-9)
        rsi_vals[i] = 100.0 - 100.0 / (1.0 + rs)

    return rsi_vals


def bollinger_bands(values: List[float], period: int = 20, num_std: float = 2.0) -> Tuple[float, float, float]:
    """Devuelve (upper, middle, lower) Bollinger Bands."""
    if len(values) < period:
        v = values[-1]
        return v, v, v

    arr = np.array(values, dtype=float)
    sma = arr[-period:].mean()
    std = arr[-period:].std()
    upper = sma + num_std * std
    lower = sma - num_std * std
    return upper, sma, lower
