from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "input_card, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("", ""),  # Пустая строка
        ("1234", "1234"),  # Короткий номер
    ],
)
def test_get_mask_card_number(input_card:list[str], expected:Union[str]):
    masked = get_mask_card_number(list(input_card))
    assert masked == expected


@pytest.mark.parametrize(
    "input_account, expected",
    [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890"),
        ("1", "**1"),  # Короткий номер
        ("", "**"),  # Пустая строка
    ],
)
def test_get_mask_account(input_account:Union[str], expected:Union[str]):
    assert get_mask_account(input_account) == expected
