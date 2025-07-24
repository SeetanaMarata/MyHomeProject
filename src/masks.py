from typing import List

from .logger_config import setup_logger

# Настройка логгера для модуля masks
logger = setup_logger("masks", "logs/masks.log")


def get_mask_card_number(pin_code_numbers: List[str]) -> str:
    """
    Маскирует номер карты с логированием
    """
    try:
        n = len(pin_code_numbers)
        if n > 6:
            end_replace = min(12, n)
            num_stars = end_replace - 6
            if num_stars > 0:
                pin_code_numbers[6:end_replace] = ["*"] * num_stars

        code_after_masks = "".join(pin_code_numbers)
        code_for_user = [code_after_masks[i: i + 4] for i in range(0, len(code_after_masks), 4)]
        result = " ".join(code_for_user)

        logger.info(f"Карта успешно замаскирована: {result}")
        return result
    except Exception as e:
        logger.error(f"Ошибка маскировки карты: {str(e)}", exc_info=True)
        return ""


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета с логированием
    """
    try:
        result = "**" + account_number[-4:]
        logger.info(f"Счет успешно замаскирован: {result}")
        return result
    except Exception as e:
        logger.error(f"Ошибка маскировки счета: {str(e)}", exc_info=True)
        return ""
