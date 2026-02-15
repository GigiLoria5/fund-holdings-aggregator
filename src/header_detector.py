import pandas as pd
from pandas import DataFrame


class HeaderDetector:
    REQUIRED_PATTERNS = ["currency", "percent", "country", "sector"]

    @classmethod
    def find_header_row(cls, df: DataFrame, max_search_rows: int = 20) -> int | None:
        search_limit = min(max_search_rows, len(df))
        for i in range(search_limit):
            row_values = [
                str(val).lower() if pd.notna(val) else "" for val in df.iloc[i]
            ]
            matches = sum(
                1
                for pattern in cls.REQUIRED_PATTERNS
                if any(pattern.lower() in val for val in row_values)
            )
            if matches == len(cls.REQUIRED_PATTERNS):
                return i
        return None
