import pandas as pd

from src.holdings_aggregator import HoldingsAggregator


def test_aggregate() -> None:
    holdings = pd.DataFrame(
        {
            "Currency": ["USD", "JPY", "USD", "USD", "KRW"],
            "Percent": [5.0, 2.0, 3.0, 2.5, 1.5],
            "Country": [
                "United States",
                "Japan",
                "United States",
                "United States",
                "South Korea",
            ],
            "Sector": [
                "Technology",
                "Consumer",
                "Health Care",
                "Technology",
                "Technology",
            ],
        }
    )
    expected = pd.DataFrame(
        {
            "Country": ["United States", "United States", "Japan", "South Korea"],
            "Market Type": ["Developed", "Developed", "Developed", "Emerging"],
            "Currency": ["USD", "USD", "JPY", "KRW"],
            "Sector": ["Technology", "Health Care", "Consumer", "Technology"],
            "Weight": [7.5, 3.0, 2.0, 1.5],
        }
    )

    result = HoldingsAggregator.aggregate(holdings)

    assert result.equals(expected)
