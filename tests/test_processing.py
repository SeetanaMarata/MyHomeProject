from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


# Фикстура с тестовыми данными
@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
        {"id": 2, "state": "PENDING", "date": "2023-01-02"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03"},
        {"id": 4, "state": "CANCELED", "date": "2023-01-04"},
    ]


# Тесты для filter_by_state
@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),
        ("PENDING", [2]),
        ("CANCELED", [4]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state(sample_data: List[Dict[str, Any]], state: str, expected_ids: List[int]) -> None:
    result = filter_by_state(sample_data, state)
    assert [item["id"] for item in result] == expected_ids


# Тесты для sort_by_date
def test_sort_by_date_desc(sample_data: List[Dict[str, Any]]) -> None:
    result = sort_by_date(sample_data, reverse=True)
    dates = [item["date"] for item in result]
    assert dates == ["2023-01-04", "2023-01-03", "2023-01-02", "2023-01-01"]


def test_sort_by_date_asc(sample_data: List[Dict[str, Any]]) -> None:
    result = sort_by_date(sample_data, reverse=False)
    dates = [item["date"] for item in result]
    assert dates == ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"]


def test_sort_by_date_empty() -> None:
    assert sort_by_date([]) == []  # Пустой список
