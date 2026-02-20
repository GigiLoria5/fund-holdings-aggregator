import pandas as pd

from src.constants import ColumnNames
from src.market_classifier import MarketClassifier


class HoldingsAggregator:
    @classmethod
    def aggregate(cls, holdings: pd.DataFrame) -> pd.DataFrame:
        print("Aggregating data...")
        holdings = holdings.copy()
        aggregated = cls._group_and_sum(holdings)
        aggregated = cls._add_market_classification(aggregated)
        aggregated = cls._sort_results(aggregated)
        print(f"Created {len(aggregated)} aggregated groups")
        return cls._select_output_columns(aggregated)

    @staticmethod
    def _group_and_sum(df: pd.DataFrame) -> pd.DataFrame:
        return (  # type: ignore
            df.groupby(
                [ColumnNames.COUNTRY, ColumnNames.CURRENCY, ColumnNames.SECTOR],
                as_index=False,
            )[ColumnNames.PERCENT]
            .sum()
            .rename(columns={ColumnNames.PERCENT: ColumnNames.WEIGHT})  # type: ignore
        )

    @staticmethod
    def _add_market_classification(df: pd.DataFrame) -> pd.DataFrame:
        df[ColumnNames.MARKET_TYPE] = df[ColumnNames.COUNTRY].apply(
            MarketClassifier.classify
        )
        return df

    @staticmethod
    def _sort_results(df: pd.DataFrame) -> pd.DataFrame:
        return df.sort_values(
            by=[ColumnNames.WEIGHT, ColumnNames.COUNTRY],
            ascending=[False, True],
            ignore_index=True,
        )

    @staticmethod
    def _select_output_columns(df: pd.DataFrame) -> pd.DataFrame:
        return df[
            [
                ColumnNames.COUNTRY,
                ColumnNames.MARKET_TYPE,
                ColumnNames.CURRENCY,
                ColumnNames.SECTOR,
                ColumnNames.WEIGHT,
            ]
        ]
