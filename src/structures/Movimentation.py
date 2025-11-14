import json

class Movimentation:
    def __init__(self, transaction_id, sender, recipient, amount, datetime, transaction_type, tags):
        self.transaction_id = int(transaction_id)
        self.sender = sender
        self.recipient = recipient
        self.amount = float(amount)
        self.datetime = datetime
        self.transaction_type = transaction_type
        self.tags = json.loads(tags)
    
    def update(self, transaction_id=None, sender=None, recipient=None, amount=None, datetime=None, transaction_type=None, tags=None):
        self.transaction_id = int(transaction_id) if transaction_id is not None else self.transaction_id
        self.sender = sender if sender is not None else self.sender
        self.recipient = recipient if recipient is not None else self.recipient
        self.amount = float(amount) if amount is not None else self.amount
        self.datetime = datetime if datetime is not None else self.datetime
        self.transaction_type = transaction_type if transaction_type is not None else self.transaction_type
        self.tags = json.loads(tags) if tags is not None else self.tags        

    def write_content(self):
        return (f"TRANSACTION ID: {self.transaction_id}\n"
                f"TYPE: {self.transaction_type}\n"
                f"DATETIME: {self.datetime}\n"
                f"SENDER: {self.sender}\n"
                f"RECIPIENT: {self.recipient}\n"
                f"AMOUNT: {self.amount}\n"
                f"TAGS: {self.tags}\n")

    def get_id(self):
        return self.transaction_id
