from datetime import datetime

from blockchain.models.block import Block
from blockchain.models.transaction import Transaction


class BlockChainService:

    def __init__(self, mining_complexity=1, mining_cut=0.01):
        self.chain = [Block(1, datetime.now(), Transaction(0), "")]
        self.pending_transactions = []
        self.nodes = set()
        self.mining_complexity = mining_complexity
        self.mining_cut = mining_cut

    def mine_pending_transactions(self):
        new_block = Block(1, datetime.now(), self.pending_transactions, self.chain[-1].hash)
        new_block.mine_block(self.mining_complexity)
        self.chain.append(new_block)
        self.pending_transactions = []

    def add_new_transaction(self, transaction: Transaction):
        this.pending_transactions.append(transaction)

    def get_miner_balance(self, sender_address: str):
        miner_balance = 0
        for block in chain:
            for transaction in block.transactions:
                if transaction.sender_address == sender_address:
                    miner_balance += (transaction.amount * self.mining_cut)
        return miner_balance

    def is_chain_tempered(self):
        for i in range(len(self.chain) - 1):
            current_block = self.chain[i+1]
            previous_block = self.chain[i]
            if current_block.hash != current_block.compute_hashing():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def add_node(self, url_address: str):
        self.nodes.add(url_address)

    def resolve_nodes_conflict(self):
        pass
