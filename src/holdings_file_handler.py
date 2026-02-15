from pathlib import Path

import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows

from src.header_detector import HeaderDetector


class HoldingsFileHandler:
    @classmethod
    def read(cls, input_file_path: Path | str) -> pd.DataFrame:
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
    def write(output_path: Path, df: pd.DataFrame) -> None:
        print("Writing output...")
        wb = Workbook()
        ws = wb.active
        ws.title = "Aggregated Holdings"
        for r_idx, row in enumerate(dataframe_to_rows(df, index=False, header=True), 1):
            for c_idx, value in enumerate(row, 1):
                cell = ws.cell(row=r_idx, column=c_idx, value=value)
                if r_idx == 1:
                    cell.font = Font(bold=True)
                    cell.fill = PatternFill(
                        start_color="D3D3D3", end_color="D3D3D3", fill_type="solid"
                    )
                    cell.alignment = Alignment(horizontal="center")
                if c_idx == 5 and r_idx > 1:
                    cell.number_format = "0.00%"
                    cell.value = (
                        value / 100 if isinstance(value, (int, float)) else value
                    )
        for col in ws.columns:
            max_length = 0
            column = col[0].column_letter
            for cell in col:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            ws.column_dimensions[column].width = min(max_length + 2, 50)
        wb.save(output_path)
        print(f"Output saved to: {output_path}")
