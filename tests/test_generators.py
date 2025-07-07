import pytest
from src .generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "operationAmount": {
                "currency": {"code": "USD"}
            },
            "description": "Перевод организации"
        },
        {
            "id": 142264268,
            "operationAmount": {
                "currency": {"code": "EUR"}
            },
            "description": "Перевод со счета на счет"
        },
        {
            "id": 873106923,
            "operationAmount": {
                "currency": {"code": "USD"}
            },
            "description": "Перевод с карты на карту"
        },
    ]

def test_filter_by_currency(sample_transactions):
    # Фильтрация USD
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 2
    assert usd_transactions[0]["id"] == 939719570
    assert usd_transactions[1]["id"] == 873106923

    # Фильтрация RUB (нет данных)
    rub_transactions = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(rub_transactions) == 0

    # Пустой список
    assert list(filter_by_currency([], "USD")) == []

def test_transaction_descriptions(sample_transactions):
    # Извлечение описаний
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту"
    ]

    # Пустой список
    assert list(transaction_descriptions([])) == []

@pytest.mark.parametrize("start, end, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]),
    (9999999999999998, 9999999999999999, [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999"
    ]),
])
def test_card_number_generator(start, end, expected):
    # Проверка генерации номеров
    result = list(card_number_generator(start, end))
    assert result == expected