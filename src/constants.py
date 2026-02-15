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
