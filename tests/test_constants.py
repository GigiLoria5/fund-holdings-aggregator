import pytest

from src.constants import ColumnNames


@pytest.mark.parametrize(
    ("attribute", "expected"),
    [
        ("CURRENCY", "Currency"),
        ("PERCENT", "Percent"),
        ("COUNTRY", "Country"),
        ("SECTOR", "Sector"),
        ("WEIGHT", "Weight"),
        ("MARKET_TYPE", "Market Type"),
    ],
)
def test_column_name_values(attribute: str, expected: str) -> None:
    assert getattr(ColumnNames, attribute) == expected
