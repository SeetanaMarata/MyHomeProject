from unittest.mock import MagicMock, patch

import requests

from src.external_api import convert_transaction_to_rub


def test_convert_rub_transaction() -> None:  # Добавлено -> None
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}}
    assert convert_transaction_to_rub(transaction) == 100.0


@patch("requests.get")
def test_convert_usd_transaction(mock_get: MagicMock) -> None:  # Добавлены аннотации
    mock_get.return_value.json.return_value = {"rates": {"RUB": 75.0}}
    mock_get.return_value.raise_for_status.return_value = None

    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "USD"}}}
    assert convert_transaction_to_rub(transaction) == 7500.0


@patch("requests.get")
def test_api_failure(mock_get: MagicMock) -> None:  # Добавлены аннотации
    mock_get.side_effect = requests.RequestException("API error")
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "USD"}}}
    assert convert_transaction_to_rub(transaction) == 0.0
