class Movimentation:
    def __init__(self, transaction_id, sender, recipient, amount, datetime, transaction_type, tags):
        self.transaction_id = int(transaction_id)
        self.sender = sender
        self.recipient = recipient
        self.amount = float(amount)
        self.datetime = datetime
        self.transaction_type = transaction_type
        self.tags = tags

    def show_details(self):
        print("TRANSACTION ID:", self.transaction_id)
        print("TYPE:", self.transaction_type)
        print("DATETIME:", self.datetime)
        print("SENDER:", self.sender)
        print("RECIPIENT:", self.recipient)
        print("AMOUNT:", self.amount)
        print("TAGS:", self.tags, end="\n\n")

    def get_id(self):
        return self.transaction_id
