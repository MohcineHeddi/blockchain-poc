class Transaction:
    def __init__(self, amount: int, sender_address: str, recipient_address: str):
        self.amount = amount
        self.sender_address = sender_address
        self.recipient_address = recipient_address
