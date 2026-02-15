import pandas as pd

from src.holdings_pipeline import HoldingsPipeline
from tests.utils import build_file_path


def test_run() -> None:
    input_file = build_file_path("spyy-gy.xlsx")
    output_file = build_file_path("aggregated_holdings.xlsx")
    assert input_file.exists()
    assert output_file.exists() is False

    HoldingsPipeline.run(input_file, output_file)

    assert output_file.exists()
    result_df = pd.read_excel(output_file)
    assert len(result_df) > 1
    output_file.unlink()
