from typing import Union

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(unique_number: Union[str]) -> Union[str]:
    """
    Маскирует номер банковской карты или счета.
    :return: Строка с маскированным номером и исходным префиксом.
    """
    parts_unique_number = unique_number.split()  # делим на слова
    disguised_number = parts_unique_number[-1]  # берём последнее слово-номер

    if disguised_number.isdigit():
        if len(disguised_number) == 16:
            number_for_masks = get_mask_card_number(list(disguised_number))
            prefix = " ".join(parts_unique_number[:-1])
            return f"{prefix} {number_for_masks}"
        elif len(disguised_number) == 20:
            number_for_masks = get_mask_account(disguised_number)
            prefix = " ".join(parts_unique_number[:-1])
            return f"{prefix} {number_for_masks}"
    return unique_number


def get_date(date_str: str) -> str:
    """Функция извлекает дату в формате ДД.ММ.ГГГГ"""
    return f"{date_str[8:10]}.{date_str[5:7]}.{date_str[:4]}"


if __name__ == "__main__":

    # примеры использования
    print(mask_account_card("Счет 73654108430135874305"))
    # Счет **4305
    print(mask_account_card("Visa Platinum 8990922113665229"))
    # Visa Platinum 8990 92** **** 5229
    print(get_date("2024-03-11T02:26:18.671407"))
    # 11.03.2024
