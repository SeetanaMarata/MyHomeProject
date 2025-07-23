import pytest
from unittest.mock import patch
from src.external_api import convert_transaction_to_rub


def test_convert_rub_transaction():
    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "RUB"}
        }
    }
    assert convert_transaction_to_rub(transaction) == 100.0


@patch("requests.get")
def test_convert_usd_transaction(mock_get):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 75.0}}
    mock_get.return_value.raise_for_status.return_value = None

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"}
        }
    }
    assert convert_transaction_to_rub(transaction) == 7500.0


@patch("requests.get")
def test_api_failure(mock_get):
    mock_get.side_effect = Exception("API error")
    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"}
        }
    }
    assert convert_transaction_to_rub(transaction) == 0.0