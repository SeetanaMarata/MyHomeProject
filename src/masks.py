from typing import List


def get_mask_card_number(pin_code_numbers: List[str]) -> str:
    """
    маскировка номера банковской карты
    :return: замаскированный номер
    """
    pin_code_numbers[6:12] = ["*", "*", "*", "*", "*", "*"]
    code_after_masks = ''.join(pin_code_numbers)
    # Разбиваем строку на части по 4 символа
    code_for_user = [code_after_masks[i:i+4]
                     for i in range(0, len(code_after_masks), 4)]
    return ' '.join(code_for_user)


print(get_mask_card_number(list
                           ("7000792289606361")))  # Вывод: 7000 79** **** 6361


def get_mask_account(account_number: str) -> str:
    """
    маскировки номера банковского счета
    :return: замаскированный счет
    """
    account_can_be_show = "**" + account_number[-4:]
    return account_can_be_show


print(get_mask_account("73654108430135874305"))
