"""
risk.py
-------

Gestión de riesgo y cálculo de:
- Take Profit (TP1, TP2, TP3)
- Stop Loss (SL)
- Tamaño de posición según modo de riesgo
"""

from typing import Tuple


def calc_take_profit(entry_price: float) -> Tuple[float, float, float]:
    """
    Tres niveles de take profit:
    - TP1:  +1.0%
    - TP2:  +1.5%
    - TP3:  +2.0%
    """
    tp1 = entry_price * 1.010
    tp2 = entry_price * 1.015
    tp3 = entry_price * 1.020
    return tp1, tp2, tp3


def calc_stop_loss(entry_price: float) -> float:
    """
    Stop loss fijo al -1.0%.
    """
    return entry_price * 0.990


def calc_position_size(balance_usdt: float, price: float, risk_mode: str = "safe") -> float:
    """
    Calcula tamaño de posición aproximado según modo de riesgo.

    - safe:      0.5% del balance
    - moderate:  1.0% del balance
    - aggressive:2.0% del balance

    Devuelve cantidad de contratos (aprox, sin apalancamiento).
    """
    risk_mode = risk_mode.lower()
    if risk_mode == "aggressive":
        risk_pct = 0.02
    elif risk_mode == "moderate":
        risk_pct = 0.01
    else:
        risk_pct = 0.005

    capital_to_use = balance_usdt * risk_pct
    if price <= 0:
        return 0.0

    qty = capital_to_use / price
    return round(qty, 4)
