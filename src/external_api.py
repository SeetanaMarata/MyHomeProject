import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/latest"
API_KEY = os.getenv("API_KEY_EXCHANGE")


def convert_transaction_to_rub(transaction: Dict[str, Any]) -> float:
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency_code = transaction["operationAmount"]["currency"]["code"]

        if currency_code == "RUB":
            return amount

        if currency_code in ["USD", "EUR"]:
            response = requests.get(
                API_URL,
                params={"base": currency_code, "symbols": "RUB"},
                headers={"apikey": API_KEY},
                timeout=5,
            )
            response.raise_for_status()
            # Явное преобразование курса к float
            rate = float(response.json()["rates"]["RUB"])  # Исправлено здесь
            return amount * rate

        return amount
    except (KeyError, ValueError, requests.RequestException):
        return 0.0
