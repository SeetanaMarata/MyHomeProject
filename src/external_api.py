import os
import requests
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/latest"
API_KEY = os.getenv("API_KEY_EXCHANGE")


def convert_transaction_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Параметры:
    transaction (Dict[str, Any]): Словарь с данными транзакции

    Возвращает:
    float: Сумма в рублях
    """
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency_code = transaction["operationAmount"]["currency"]["code"]

        if currency_code == "RUB":
            return amount

        if currency_code in ["USD", "EUR"]:
            response = requests.get(
                API_URL,
                params={"base": currency_code, "symbols": "RUB"},
                headers={"apikey": API_KEY}
            )
            response.raise_for_status()
            rate = response.json()["rates"]["RUB"]
            return amount * rate

        # Для других валют возвращаем как есть (по условию задачи)
        return amount
    except (KeyError, ValueError, requests.RequestException):
        return 0.0