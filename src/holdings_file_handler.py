import pandas as pd

from src.header_detector import HeaderDetector


class HoldingsFileHandler:
    @classmethod
    def read(cls, input_file_path: str) -> pd.DataFrame:
        print(f"Reading: {input_file_path}")
        raw_df = pd.read_excel(input_file_path, header=None)
        header_row = HeaderDetector.find_header_row(raw_df)
        holdings_df = pd.read_excel(input_file_path, header=header_row)
        column_map = HeaderDetector.map_columns(holdings_df.columns)
        holdings_df = holdings_df[
            [
                column_map["currency"],
                column_map["percent"],
                column_map["country"],
                column_map["sector"],
            ]
        ].copy()
        holdings_df.columns = ["Currency", "Percent", "Country", "Sector"]
        holdings_df = cls._clean_data(holdings_df)
        print(f"Found {len(holdings_df)} holdings")
        return holdings_df

    @staticmethod
    def _clean_data(df: pd.DataFrame) -> pd.DataFrame:
        df = df.dropna(subset=["Country"])
        df = df[df["Country"].astype(str).str.strip() != ""]
        df["Percent"] = pd.to_numeric(df["Percent"], errors="coerce")
        df = df.dropna(subset=["Percent"])
        for col in ["Currency", "Country", "Sector"]:
            df[col] = df[col].fillna("Unknown").astype(str).str.strip()
        return df

    @staticmethod
    def write(output_file_path: str, aggregated_df: pd.DataFrame) -> None:
        print("Writing output...")
        # ...
