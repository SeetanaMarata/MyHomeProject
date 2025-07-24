import json
import os
from typing import Any, Dict, List

from .logger_config import setup_logger

# Настройка логгера для модуля utils
logger = setup_logger("utils", "logs/utils.log")


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла с логированием
    """
    try:
        logger.info(f"Загрузка транзакций из {file_path}")

        if not os.path.exists(file_path):
            logger.error(f"Файл не найден: {file_path}")
            return []

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if not isinstance(data, list):
                logger.error(f"Некорректный формат данных в файле {file_path}")
                return []

            logger.info(f"Успешно загружено {len(data)} транзакций")
            return data
    except (json.JSONDecodeError, OSError) as e:
        logger.error(f"Ошибка при чтении файла: {str(e)}", exc_info=True)
        return []


def create_test_transactions(file_path: str) -> None:
    """
    Создает тестовые данные транзакций
    """
    test_data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(test_data, file, ensure_ascii=False, indent=2)
    logger.info(f"Создан тестовый файл с {len(test_data)} транзакциями")
