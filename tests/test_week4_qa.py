import pandas as pd
import pytest
import week4_qa
from week4_qa import validate_dataframe, validate_no_negative_values, process_payment


def test_validate_dataframe_valid():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    assert validate_dataframe(df) is True


def test_validate_dataframe_empty():
    df = pd.DataFrame()
    assert validate_dataframe(df) is False


def test_validate_dataframe_has_nan():
    df = pd.DataFrame({"a": [1, None]})
    assert validate_dataframe(df) is False


def test_validate_no_negative_values():
    df = pd.DataFrame({"price": [1, 2, 3]})
    assert validate_no_negative_values(df, "price") is True

    df_neg = pd.DataFrame({"price": [1, -2, 3]})
    assert validate_no_negative_values(df_neg, "price") is False


def test_mock_external_api_call(mocker):
    # Mock the function to return a known dict
    mocker.patch("week4_qa.mock_external_api_call", return_value={"status": "ok"})
    result = week4_qa.mock_external_api_call("http://any-url.com")
    assert result == {"status": "ok"}


def test_process_payment():
    assert process_payment(100, "USD") == pytest.approx(85.0, rel=1e-2)
    assert process_payment(100, "EUR") == 100
