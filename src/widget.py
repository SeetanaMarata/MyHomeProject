from masks import get_mask_card_number
from masks import get_mask_account
from typing import Union

def mask_account_card(unique_number: Union[str]) -> Union[str]:
    """
    Маскирует номер банковской карты или счета.
    :return: Строка с маскированным номером и исходным префиксом.
    """

    #account_or_card_number = unique_number.split()  # разделяем строку пробелами
    number_card_for_masks = ""
    number_account_for_mask = unique_number[5:] # переменная для получения номера счета по индексу
    disguised_number = ""
    disguised_account = ""
    only_card_name = unique_number[:-16]
    for word in unique_number: # перебираем строку по словам
        for symbol in word:
            if symbol.isdigit():   # проверяем является ли символ цифрой
                number_card_for_masks += symbol # Собираем цифры в отдельную переменную
                if len(number_card_for_masks) == 16: # проверяем по количеству карта это или счет
                    disguised_number = get_mask_card_number(number_card_for_masks) # вызываем функцию из другого модуля в отдельную переменную
                else:
                    disguised_account = get_mask_account(number_account_for_mask)
                    return f"'Счет' {disguised_account}"
    return f"{only_card_name} {disguised_number}"


# Примеры использования
print(mask_account_card("Maestro 7000792289606361"))  # Maestro 7000 79** **** 6361
print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305


