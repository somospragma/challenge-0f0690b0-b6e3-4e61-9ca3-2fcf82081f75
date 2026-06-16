from dataclasses import dataclass
from typing import Dict

@dataclass
class Transaction:
    id: str
    amount: float
    timestamp: str
    type: str