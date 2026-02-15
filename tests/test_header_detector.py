import pandas as pd
import pytest

from src.constants import ColumnPatterns
from src.header_detector import HeaderDetector


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (
            [
                ["Metadata", "Value"],
                ["Fund Name", "Test Fund"],
                [
                    "ISIN",
                    "Security Name",
                    "Currency",
                    "Percent of Fund",
                    "Trade country Name",
                    "Sector Classification",
                ],
                ["US001", "Apple", "USD", 5.0, "United States"],
            ],
            2,
        ),
        (
            [
                ["", "", ""],
                ["Fund:", "Test"],
                ["", "", ""],
                [
                    "ISIN",
                    "Security Name",
                    "Currency",
                    "percent of Fund",
                    "Security Sector",
                    "country Name",
                ],
                ["US001", "Microsoft", "USD", 3.0],
            ],
            3,
        ),
        (
            [
                ["Currency", "Currency", "Currency", "Country"],
                ["Currency", "Percent", "Currency", "Country"],
            ],
            None,
        ),
        (
            [
                ["A", "B", "C"],
                ["1", "2", "3"],
            ],
            None,
        ),
    ],
)
def test_find_header_row(data: list[list[str | float]], expected: int | None) -> None:
    df = pd.DataFrame(data)

    try:
        header_row = HeaderDetector.find_header_row(df)
        assert header_row == expected
    except ValueError:
        if expected is not None:
            pytest.fail("Expected header row not found")


@pytest.mark.parametrize(
    ("max_search_rows", "expected"),
    [(1, None), (2, 1)],
)
def test_find_header_row_max_search_rows(
    max_search_rows: int, expected: int | None
) -> None:
    df = pd.DataFrame(
        [
            ["Fund Name", "Test Fund"],
            [
                "Currency",
                "Percent of Fund",
                "Trade country Name",
                "Sector Classification",
            ],
        ],
    )

    try:
        header_row = HeaderDetector.find_header_row(df, max_search_rows=max_search_rows)
        assert header_row == expected
    except ValueError:
        if expected is not None:
            pytest.fail("Expected header row not found")


@pytest.mark.parametrize(
    "columns",
    [
        ["Currency", "Percent", "Country", "Sector"],
        ["currency", "percent", "country", "sector"],
        ["CURRENCY", "PERCENT", "COUNTRY", "SECTOR"],
        ["Trade Currency", "Percent of Fund", "Trade Country", "Sector Class"],
    ],
)
def test_column_mapping_case_insensitive(columns: list[str]) -> None:
    column_map = HeaderDetector.map_columns(pd.Index(columns))

    assert len(column_map) == 4
    for pattern in ColumnPatterns.get_all():
        assert pattern in column_map


def test_column_mapping_missing_column() -> None:
    columns = pd.Index(["Currency", "Percent", "Country"])
    with pytest.raises(ValueError) as exc_info:
        HeaderDetector.map_columns(columns)
    assert "sector" in str(exc_info.value)


def test_column_mapping_duplicate_match() -> None:
    columns = pd.Index(["Currency", "Trade Currency", "Percent", "Country", "Sector"])
    with pytest.raises(ValueError) as exc_info:
        HeaderDetector.map_columns(columns)
    assert "currency" in str(exc_info.value)
