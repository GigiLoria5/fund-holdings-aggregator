import pandas as pd

from src.holdings_aggregator import HoldingsAggregator
from tests.utils import build_file_path


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


def test_run() -> None:
    input_file = build_file_path("spyy-gy.xlsx")
    output_file = build_file_path("aggregated_holdings.xlsx")
    assert input_file.exists()
    assert output_file.exists() == False

    HoldingsAggregator.run(input_file, output_file)

    assert output_file.exists()
    result_df = pd.read_excel(output_file)
    assert len(result_df) > 1
    output_file.unlink()
