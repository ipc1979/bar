from dataclasses import dataclass
from datetime import datetime
from typing import List
from app.domain.round import Round
from app.domain.item_summary import ItemSummary 

@dataclass
class Order:
    created: datetime
    paid: bool
    subtotal: float
    taxes: float
    discounts: float
    items: List[ItemSummary]    
    rounds: List[Round]