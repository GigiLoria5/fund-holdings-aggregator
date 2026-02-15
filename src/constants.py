from dataclasses import dataclass
from enum import StrEnum


class ColumnNames(StrEnum):
    CURRENCY = "Currency"
    PERCENT = "Percent"
    COUNTRY = "Country"
    SECTOR = "Sector"
    WEIGHT = "Weight"
    MARKET_TYPE = "Market Type"


@dataclass(frozen=True)
class ColumnPatterns:
    CURRENCY = "currency"
    PERCENT = "percent"
    COUNTRY = "country"
    SECTOR = "sector"

    @classmethod
    def get_all(cls) -> list[str]:
        return [cls.CURRENCY, cls.PERCENT, cls.COUNTRY, cls.SECTOR]

    @classmethod
    def to_standard_name(cls, pattern: str) -> str:
        mapping = {
            cls.CURRENCY: ColumnNames.CURRENCY,
            cls.PERCENT: ColumnNames.PERCENT,
            cls.COUNTRY: ColumnNames.COUNTRY,
            cls.SECTOR: ColumnNames.SECTOR,
        }
        return mapping[pattern]
