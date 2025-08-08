import logging
import os


def setup_logger(name: str, log_file: str) -> logging.Logger:
    """
    Настройка логгера для модуля

    :param name: Имя логгера (совпадает с именем модуля)
    :param log_file: Путь к файлу логов
    :return: Объект логгера
    """
    # Создаем папку для логов если её нет
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # FileHandler с перезаписью файла при каждом запуске
    file_handler = logging.FileHandler(log_file, mode="w")
    file_handler.setLevel(logging.DEBUG)

    # Форматирование логов
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger
