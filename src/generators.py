from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, None, None]:
    """Фильтрует транзакции по заданной валюте"""
    for transaction in transactions:
        operation_currency = transaction["operationAmount"]["currency"]["code"]
        if operation_currency == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]:
    """Извлекает описания транзакций"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генерирует номера карт в заданном диапазоне"""
    for num in range(start, end + 1):
        formatted_num = f"{num:016d}"
        yield " ".join([formatted_num[i:i+4] for i in range(0, 16, 4)])
