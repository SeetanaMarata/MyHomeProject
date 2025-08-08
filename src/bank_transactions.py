import re
from typing import Dict, List


def filter_transactions_by_description(data: List[Dict], search: str) -> List[Dict]:
    """
    Фильтрует транзакции по строке в описании (с использованием regex)

    Args:
        data: Список транзакций
        search: Строка для поиска в описании

    Returns:
        Отфильтрованный список транзакций
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [item for item in data if "description" in item and pattern.search(item["description"])]


def count_transactions_by_categories(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Считает количество транзакций по категориям

    Args:
        data: Список транзакций
        categories: Список категорий для подсчета

    Returns:
        Словарь {категория: количество}
    """
    return {category: sum(1 for item in data if item.get("description") == category) for category in categories}


def filter_transactions_by_status(data: List[Dict], status: str) -> List[Dict]:
    """
    Фильтрует транзакции по статусу (case insensitive)
    """
    status = status.upper()
    return [item for item in data if item.get("status", "").upper() == status]


def sort_transactions_by_date(data: List[Dict], reverse: bool = False) -> List[Dict]:
    """
    Сортирует транзакции по дате
    """
    return sorted(data, key=lambda x: x.get("date", ""), reverse=reverse)


def filter_transactions_by_currency(data: List[Dict], currency: str) -> List[Dict]:
    """
    Фильтрует транзакции по валюте (case insensitive)
    """
    currency = currency.upper()
    return [item for item in data if item.get("currency", "").upper() == currency]
