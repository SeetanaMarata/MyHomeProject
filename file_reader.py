from typing import Any, Dict, List

import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Read financial transactions from a CSV file.

    Args:
        file_path: Path to the CSV file.

    Returns:
        List of dictionaries with transaction data.
    """
    df = pd.read_csv(file_path, delimiter=";")
    return [{str(k): v for k, v in item.items()} for item in df.to_dict("records")]


def read_excel_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Read financial transactions from an Excel file.

    Args:
        file_path: Path to the Excel file.

    Returns:
        List of dictionaries with transaction data.
    """
    df = pd.read_excel(file_path)
    return [{str(k): v for k, v in item.items()} for item in df.to_dict("records")]
