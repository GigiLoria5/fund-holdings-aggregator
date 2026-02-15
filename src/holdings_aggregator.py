import pandas as pd

from src.market_classifier import MarketClassifier


class HoldingsAggregator:
    @staticmethod
    def run() -> None:
        print("Hello")

    @classmethod
    def aggregate(cls, holdings: pd.DataFrame) -> pd.DataFrame:
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
        return aggregated[["Country", "Market Type", "Currency", "Sector", "Weight"]]
