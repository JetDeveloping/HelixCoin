from hashlib import sha256
import json
import time
from dataclasses import dataclass

"""
The Block Class
"""
@dataclass
class Block:
    index: int
    transactions: list
    timestamp: float
    previous_hash: str
    nonce: int

