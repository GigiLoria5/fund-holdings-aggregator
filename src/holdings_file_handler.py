import pandas as pd


class HoldingsFileHandler:
    @staticmethod
    def read(input_file_path: str) -> pd.DataFrame:
        holdings_df = pd.read_excel(input_file_path)
        print(f"Reading: {input_file_path}")
        # ...
        print(f"Found {len(holdings_df)} holdings")
        return holdings_df

    @staticmethod
    def write(output_file_path: str, aggregated_df: pd.DataFrame) -> None:
        print("Writing output...")
        # ...
