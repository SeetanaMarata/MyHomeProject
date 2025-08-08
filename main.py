import json
from typing import Any, Dict, List

from src.bank_transactions import (filter_transactions_by_currency, filter_transactions_by_description,
                                   filter_transactions_by_status, sort_transactions_by_date)
from src.masks import get_mask_account, get_mask_card_number
from src.utils import create_test_transactions, load_transactions


def main() -> None:
    # Путь к тестовым данным
    test_file = "test_data/transactions.json"

    # Создаем тестовые данные, если файл не существует
    try:
        transactions = load_transactions(test_file)
        if not transactions:
            print("Тестовый файл не найден. Создаем...")
            create_test_transactions(test_file)
            transactions = load_transactions(test_file)
    except Exception as e:
        print(f"Ошибка: {e}")
        return

    print(f"Загружено транзакций: {len(transactions)}")

    # Демонстрация работы масок
    if transactions:
        first_card = transactions[0].get("from", "")
        if first_card:
            # Извлекаем номер карты (последнее слово в строке)
            card_number = first_card.split()[-1]
            print(f"Маскировка карты: {get_mask_card_number(list(card_number))}")
        else:
            print("Нет данных карты в первой транзакции")

        first_account = transactions[0].get("to", "")
        if first_account:
            account_number = first_account.split()[-1]
            print(f"Маскировка счета: {get_mask_account(account_number)}")
        else:
            print("Нет данных счета в первой транзакции")

    # Тестирование функций масок
    print("\nТестирование масок:")
    print("7000792289606361 ->", get_mask_card_number(list("7000792289606361")))
    print("73654108430135874305 ->", get_mask_account("73654108430135874305"))


if __name__ == "__main__":
    main()


def load_transactions_(filepath: str) -> list[Dict[str, Any]]:
    """Загружает транзакции из JSON файла"""
    with open(filepath, "r", encoding="utf-8") as f:
        data: List[Dict[str, Any]] = json.load(f)
        return data


def main_() -> None:
    """Основная логика программы"""
    # Загрузка данных
    transactions = load_transactions_("transactions.json")

    # 1. Фильтрация по статусу
    status = input("Введите статус транзакций (EXECUTED/CANCELED/PENDING): ").strip()
    filtered = filter_transactions_by_status(transactions, status)

    # 2. Дополнительные фильтры
    if input("Фильтровать по описанию? (y/n): ").lower() == "y":
        search = input("Введите текст для поиска: ")
        filtered = filter_transactions_by_description(filtered, search)

    if input("Только RUB транзакции? (y/n): ").lower() == "y":
        filtered = filter_transactions_by_currency(filtered, "RUB")

    # 3. Сортировка
    if input("Сортировать по дате? (y/n): ").lower() == "y":
        order = input("По возрастанию или убыванию? (asc/desc): ")
        filtered = sort_transactions_by_date(filtered, order == "desc")

    # 4. Вывод результатов
    print(f"\nНайдено {len(filtered)} транзакций:")
    for t in filtered:
        print(f"{t['date']} - {t['description']} - {t.get('amount', 'N/A')} {t.get('currency', '')}")


if __name__ == "__main__":
    main_()
