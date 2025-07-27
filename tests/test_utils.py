from unittest.mock import MagicMock, mock_open, patch

from src.utils import load_transactions


@patch("os.path.exists", return_value=False)
def test_load_transactions_file_not_found(mock_exists: MagicMock) -> None:  # Аннотации
    assert load_transactions("non_existent.json") == []


@patch("os.path.exists", return_value=True)
@patch("builtins.open", mock_open(read_data="invalid json"))
def test_load_transactions_invalid_json(mock_exists: MagicMock) -> None:  # Аннотации
    assert load_transactions("invalid.json") == []


@patch("os.path.exists", return_value=True)
@patch("builtins.open", mock_open(read_data='{"key": "value"}'))
def test_load_transactions_not_list(mock_exists: MagicMock) -> None:  # Аннотации
    assert load_transactions("not_list.json") == []


@patch("os.path.exists", return_value=True)
@patch("builtins.open", mock_open(read_data='[{"id": 1}]'))
def test_load_transactions_success(mock_exists: MagicMock) -> None:  # Аннотации
    assert load_transactions("valid.json") == [{"id": 1}]
