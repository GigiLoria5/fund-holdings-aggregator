from pathlib import Path

from src.holdings_aggregator import HoldingsAggregator
from src.holdings_file_handler import HoldingsFileHandler


class HoldingsPipeline:
    @classmethod
    def run(cls, input_file_path: Path | str, output_file_path: Path | str) -> None:
        holdings_df = HoldingsFileHandler.read(input_file_path)
        aggregated_df = HoldingsAggregator.aggregate(holdings_df)
        HoldingsFileHandler.write(Path(output_file_path), aggregated_df)
