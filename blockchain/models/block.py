from typing import List
import hashlib
import json
from datetime import datetime

from blockchain.models.transaction import Transaction


class Block:
    def __init__(self, nonce: int, timestamp: datetime, transactions: List[Transaction], previous_hash: str):
        self.nonce = nonce
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.compute_hashing()
        
        def compute_hashing(self):
            if self.transactions:
                block_string = json.dumps({
                    "nonce": self.nonce,
                    "timestamp": self.timestamp,
                    "transactions": self.transactions[0].amount,
                    "previous_hash": self.previous_hash
                },sort_keys=True).encode()
                return hashlib.sha256(block_string).hexdigest()

        def mine_block(self, complexity_level: int) -> None:
            while self.hash and self.hash[:complexity_level] != ("0" * complexity_level):
                self.nonce += 1
                self.hash = self.compute_hashing()