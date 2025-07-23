import pytest
from unittest.mock import mock_open, patch
from src.utils import load_transactions

def test_load_transactions_file_not_found():
    assert load_transactions("non_existent.json") == []

@patch("builtins.open", mock_open(read_data="invalid json"))
def test_load_transactions_invalid_json():
    assert load_transactions("invalid.json") == []

@patch("builtins.open", mock_open(read_data='{"key": "value"}'))
def test_load_transactions_not_list():
    assert load_transactions("not_list.json") == []

@patch("builtins.open", mock_open(read_data='[{"id": 1}]'))
def test_load_transactions_success():
    assert load_transactions("valid.json") == [{"id": 1}]