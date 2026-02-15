import pytest

from src.holdings_file_handler import HoldingsFileHandler
from tests.utils import build_file_path_as_str


def test_file_not_found() -> None:
    with pytest.raises(FileNotFoundError):
        HoldingsFileHandler.read("nonexistent_file.xlsx")


@pytest.mark.parametrize(
    "file_name", ["missing_header.xlsx", "invalid_file_format.txt"]
)
def test_invalid_file(file_name: str) -> None:
    test_file = build_file_path_as_str(file_name)
    with pytest.raises(ValueError):
        HoldingsFileHandler.read(test_file)
