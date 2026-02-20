import pandas as pd
from pandas import DataFrame

from src.constants import ColumnPatterns


class HeaderDetector:
    @classmethod
    def find_header_row(cls, df: DataFrame, max_search_rows: int = 20) -> int:
        required_patterns = ColumnPatterns.get_all()
        search_limit = min(max_search_rows, len(df))
        for i in range(search_limit):
            row_values = [
                str(val).lower() if pd.notna(val) else "" for val in df.iloc[i]
            ]
            if cls._row_contains_all_patterns(row_values, required_patterns):
                return i
        raise RequiredColumnsNotFound(required_patterns, search_limit)

    @staticmethod
    def _row_contains_all_patterns(row_values: list[str], patterns: list[str]) -> bool:
        matches = sum(
            1
            for pattern in patterns
            if any(pattern.lower() in val for val in row_values)
        )
        return matches == len(patterns)

    @classmethod
    def map_columns(cls, columns: pd.Index) -> dict[str, str]:
        column_map = {}
        for pattern in ColumnPatterns.get_all():
            matches = [col for col in columns if pattern in str(col).lower()]
            if len(matches) != 1:
                raise HeaderMismatchError(pattern, matches)
            column_map[pattern] = matches[0]
        return column_map


class RequiredColumnsNotFound(Exception):
    def __init__(self, required_patterns: list[str], search_limit: int) -> None:
        super().__init__(
            f"Required columns '{required_patterns}' not found "
            f"in the first {search_limit} rows"
        )


class HeaderMismatchError(Exception):
    def __init__(self, pattern: str, matches: list[str]) -> None:
        super().__init__(
            f"Expected exactly one column matching pattern "
            f"'{pattern}', but found {len(matches)} match(es): {matches}."
        )
