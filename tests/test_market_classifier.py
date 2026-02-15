import pytest

from src.market_classifier import MarketClassifier


@pytest.mark.parametrize(
    ("country", "expected"),
    [
        ("United States", "Developed"),
        ("Japan", "Developed"),
        ("Germany", "Developed"),
        ("japan", "Developed"),
        (" United kingdom ", "Developed"),
        ("China", "Emerging"),
        ("India", "Emerging"),
        ("Brazil", "Emerging"),
        ("Vietnam", "Frontier"),
        ("Kenya", "Frontier"),
        ("Ukraine", ""),
        ("Panama", ""),
        ("USA", ""),
        ("UK", ""),
        (None, ""),
        ("", ""),
    ],
)
def test_classify(country: str | None, expected: str) -> None:
    actual = MarketClassifier.classify(country)

    assert actual == expected
