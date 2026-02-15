import pandas as pd

from src.holdings_file_handler import HoldingsFileHandler
from src.market_classifier import MarketClassifier


class HoldingsAggregator:
    @classmethod
    def run(cls, input_file_path: str, output_file_path: str) -> None:
        holdings_df = HoldingsFileHandler.read(input_file_path)
        aggregated_df = cls.aggregate(holdings_df)
        HoldingsFileHandler.write(output_file_path, aggregated_df)

    @classmethod
    def aggregate(cls, holdings: pd.DataFrame) -> pd.DataFrame:
        print("Aggregating data...")
        df = holdings.copy()
        aggregated = (
            df.groupby(["Country", "Currency", "Sector"], as_index=False)["Percent"]
            .sum()
            .rename(columns={"Percent": "Weight"})
        )
        aggregated["Market Type"] = aggregated["Country"].apply(
            MarketClassifier.classify
        )
        aggregated = aggregated.sort_values(
            by=["Weight", "Country"],
            ascending=[False, True],
            ignore_index=True,
        )
        print(f"Created {len(aggregated)} aggregated groups")
        return aggregated[["Country", "Market Type", "Currency", "Sector", "Weight"]]
