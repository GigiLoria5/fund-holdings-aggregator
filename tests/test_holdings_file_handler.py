from typing import Any

import pytest

from src.header_detector import RequiredColumnsNotFound
from src.holdings_file_handler import HoldingsFileHandler
from tests.utils import build_file_path_as_str


def test_file_not_found() -> None:
    with pytest.raises(FileNotFoundError):
        HoldingsFileHandler.read("nonexistent_file.xlsx")


@pytest.mark.parametrize(
    ("file_name", "exception"),
    [
        ("missing_header.xlsx", RequiredColumnsNotFound),
        ("invalid_file_format.txt", ValueError),
    ],
)
def test_invalid_file(file_name: str, exception: Any) -> None:
    test_file = build_file_path_as_str(file_name)
    with pytest.raises(exception):
        HoldingsFileHandler.read(test_file)
