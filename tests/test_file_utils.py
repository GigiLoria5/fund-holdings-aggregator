import pandas as pd
import pytest

from src.file_utils import find_header_row


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

    header_row = find_header_row(df)

    assert header_row == expected


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

    header_row = find_header_row(df, max_search_rows=max_search_rows)

    assert header_row == expected
