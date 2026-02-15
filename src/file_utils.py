import pandas as pd
from pandas import DataFrame


def find_header_row(df: DataFrame, max_search_rows: int = 20) -> int | None:
    expected_columns = ["Currency", "Percent", "Country", "Sector"]
    search_limit = min(max_search_rows, len(df))
    for i in range(search_limit):
        row_values = [str(val) if pd.notna(val) else "" for val in df.iloc[i]]
        matches = sum(
            1
            for col in expected_columns
            if any(col.lower() in val.lower() for val in row_values)
        )
        if matches == len(expected_columns):
            return i
    return None
