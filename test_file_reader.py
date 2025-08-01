import unittest
from unittest.mock import patch

import pandas as pd

from file_reader import read_csv_transactions, read_excel_transactions


class TestFileReader(unittest.TestCase):
    @patch("pandas.read_csv")
    def test_read_csv_transactions(self, mock_read_csv):
        # Setup mock
        mock_data = pd.DataFrame(
            [
                {"date": "2023-01-01", "amount": 100, "description": "Test"},
                {"date": "2023-01-02", "amount": 200, "description": "Test 2"},
            ]
        )
        mock_read_csv.return_value = mock_data

        # Call function
        result = read_csv_transactions("dummy.csv")

        # Assertions
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["amount"], 100)
        mock_read_csv.assert_called_once_with("dummy.csv")

    @patch("pandas.read_excel")
    def test_read_excel_transactions(self, mock_read_excel):
        # Setup mock
        mock_data = pd.DataFrame(
            [
                {"date": "2023-01-01", "amount": 300, "description": "Excel Test"},
                {"date": "2023-01-02", "amount": 400, "description": "Excel Test 2"},
            ]
        )
        mock_read_excel.return_value = mock_data

        # Call function
        result = read_excel_transactions("dummy.xlsx")

        # Assertions
        self.assertEqual(len(result), 2)
        self.assertEqual(result[1]["amount"], 400)
        mock_read_excel.assert_called_once_with("dummy.xlsx")


if __name__ == "__main__":
    unittest.main()
