from dataclasses import dataclass
from datetime import datetime
from typing import List
from app.domain.item import Item

@dataclass
class Round:
    created: datetime
    items: List[Item]