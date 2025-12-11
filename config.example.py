"""
config.example.py
------------------

Ejemplo de archivo de configuración para el bot.

⚠ NO uses este archivo para subir claves reales.
La idea es que el usuario copie este archivo como
`config.py` (el verdadero), lo edite localmente y
LO EXCLUYA del repositorio con `.gitignore`.
"""


class Settings:
    # Claves de Binance (solo ejemplo, poner las reales en config.py)
    BINANCE_API_KEY: str = "YOUR_BINANCE_API_KEY"
    BINANCE_API_SECRET: str = "YOUR_BINANCE_API_SECRET"

    # Parámetros generales
    SYMBOL: str = "BTCUSDT"
    BASE_URL_FUTURES: str = "https://fapi.binance.com"

    # Configuración de estrategia
    RISK_MODE: str = "moderate"  # safe | moderate | aggressive
    MIN_NOTIONAL: float = 5.0


# En producción:
# from config import Settings  # y NO desde config.example
