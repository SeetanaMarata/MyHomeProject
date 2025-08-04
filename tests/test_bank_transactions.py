from src.bank_transactions import (count_transactions_by_categories, filter_transactions_by_currency,
                                   filter_transactions_by_description, filter_transactions_by_status,
                                   sort_transactions_by_date)

# Тестовые данные
SAMPLE_TRANSACTIONS = [
    {"description": "Payment for services", "status": "EXECUTED", "date": "2023-01-01", "currency": "RUB"},
    {"description": "Grocery shopping", "status": "EXECUTED", "date": "2023-01-02", "currency": "USD"},
    {"description": "Service fee", "status": "PENDING", "date": "2023-01-03", "currency": "RUB"},
]


class TestDescriptionFilter:
    def test_basic_search(self) -> None:
        result = filter_transactions_by_description(SAMPLE_TRANSACTIONS, "service")
        assert len(result) == 2
        assert all("service" in t["description"].lower() for t in result)

    def test_case_insensitive(self) -> None:
        result = filter_transactions_by_description(SAMPLE_TRANSACTIONS, "SERVICE")
        assert len(result) == 2


class TestCategoryCounter:
    def test_basic_counting(self) -> None:
        categories = ["Payment for services", "Grocery shopping", "Non-existent"]
        result = count_transactions_by_categories(SAMPLE_TRANSACTIONS, categories)
        assert result == {"Payment for services": 1, "Grocery shopping": 1, "Non-existent": 0}


class TestStatusFilter:
    def test_status_filtering(self) -> None:
        result = filter_transactions_by_status(SAMPLE_TRANSACTIONS, "executed")
        assert len(result) == 2
        assert all(t["status"] == "EXECUTED" for t in result)


class TestDateSorting:
    def test_ascending_sort(self) -> None:
        result = sort_transactions_by_date(SAMPLE_TRANSACTIONS)
        assert result[0]["date"] == "2023-01-01"
        assert result[-1]["date"] == "2023-01-03"

    def test_descending_sort(self) -> None:
        result = sort_transactions_by_date(SAMPLE_TRANSACTIONS, reverse=True)
        assert result[0]["date"] == "2023-01-03"
        assert result[-1]["date"] == "2023-01-01"


class TestCurrencyFilter:
    def test_currency_filter(self) -> None:
        result = filter_transactions_by_currency(SAMPLE_TRANSACTIONS, "rub")
        assert len(result) == 2
        assert all(t["currency"] == "RUB" for t in result)
