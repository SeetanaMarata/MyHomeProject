import pytest

from typing import List, Tuple
from src.widget import get_date, mask_account_card


# Фикстуры для mask_account_card
@pytest.fixture
def card_account_samples() -> List[Tuple[str, str]]:
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),
        ("Maestro 98765432109876543210", "Maestro **3210"),
        ("Invalid", "Invalid"),  # Некорректные данные
    ]


# Фикстуры для get_date
@pytest.fixture
def date_samples() -> List[Tuple[str, str]]:
    return [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
        ("1995-12-31T23:59:59.999999", "31.12.1995"),
    ]


# Параметризованные тесты для mask_account_card
def test_mask_account_card(card_account_samples: List[Tuple[str, str]]) -> None:
    for input_str, expected in card_account_samples:
        result = mask_account_card(input_str)
        assert result == expected


# Тесты для get_date
def test_get_date(date_samples: List[Tuple[str, str]]) -> None:
    for input_date, expected in date_samples:
        result = get_date(input_date)
        assert result == expected


def test_get_date_invalid():
    assert get_date("2024-13-32T25:70:99") == "32.13.2024"  # Обработка некорректной даты
