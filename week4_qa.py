"""
Week 4: Data Quality Assurance

Write functions to validate data and practice testing.
"""

import pandas as pd


def validate_dataframe(df: pd.DataFrame) -> bool:
    """
    Return True if the DataFrame is valid, meaning:
    - It is not empty
    - It has no NaN values
    - It has at least one column
    """
    # TODO: implement
    if df.empty:
        return False
    if df.isnull().values.any():
        return False
    if df.shape[1] < 1:
        return False
    return True


def validate_no_negative_values(df: pd.DataFrame, column: str) -> bool:
    """Return True if all values in the given column are non-negative."""
    # TODO: implement
    if (df[column] < 0).any():
        return False
    return True
    


def mock_external_api_call(url: str) -> dict:
    """
    This function will be mocked in tests.
    In reality it would call an API. Here, if you call it without mocking,
    it should raise an exception (so you learn to mock it).
    """
    raise NotImplementedError("This should be mocked in tests") 




def process_payment(amount: float, currency: str = "USD") -> float:
    """
    Convert amount to EUR if currency is USD (1 USD = 0.85 EUR).
    Return the converted amount.
    If currency is not USD, just return the amount.
    """
    # TODO: implement
    if currency == "USD":
        return amount * 0.85
    return amount
