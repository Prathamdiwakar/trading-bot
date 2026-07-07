import os
from binance.client import Client
from bot.logging_config import logger

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

TESTNET_URL = "https://testnet.binancefuture.com"


def get_client():
    client = Client(API_KEY, API_SECRET, testnet=True)
    client.FUTURES_URL = TESTNET_URL + "/fapi"
    logger.info("Binance Futures Testnet client initialized")
    return client