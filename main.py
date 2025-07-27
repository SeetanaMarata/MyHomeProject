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
