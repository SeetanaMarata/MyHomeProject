from typing import Union


def get_mask_card_number(pin_code_numbers: list[str]) -> Union[str]:
    """
    Маскировка номера банковской карты
    :param pin_code_numbers: список цифр карты
    :return: замаскированный номер с группировкой по 4 цифры
    """
    n = len(pin_code_numbers)
    if n > 6:
        # Заменяем 6 символов начиная с 6-й позиции
        end_replace = min(12, n)  # Ограничиваем конец замены длиной номера
        num_stars = end_replace - 6  # Количество символов для замены
        if num_stars > 0:
            pin_code_numbers[6:end_replace] = ["*"] * num_stars

    # Собираем строку из списка
    code_after_masks = "".join(pin_code_numbers)
    # Разбиваем на группы по 4 символа
    code_for_user = [code_after_masks[i: i + 4] for i in range(0, len(code_after_masks), 4)]
    return " ".join(code_for_user)


# Проверка работы функции
print(get_mask_card_number(list("7000792289606361")))  # 7000 79** **** 6361
print(get_mask_card_number(list("1234")))  # 1234
print(get_mask_card_number(list("")))  # (пустая строка)


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """
    маскировки номера банковского счета
    :return: замаскированный счет
    """
    account_can_be_show = "**" + account_number[-4:]
    return account_can_be_show


print(get_mask_account("73654108430135874305"))
