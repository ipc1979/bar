from dataclasses import dataclass

@dataclass
class ItemSummary:
    name: str
    price_per_unit: float
    total: int