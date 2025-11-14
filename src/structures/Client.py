import json

class Client:
    def __init__(self, id, first_name, last_name, country, balance, vip_level, payment_methods):
        self.id = int(id)
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.balance = float(balance)
        self.vip_level = int(vip_level)   
        self.payment_methods = json.loads(payment_methods) # ["PIX", "CREDIT_CARD", "BTC"]

    def update(self, id=None, first_name=None, last_name=None, country=None, balance=None, vip_level=None, payment_methods=None):
        self.id = int(id) if id is not None else self.id
        self.first_name = first_name if first_name is not None else self.first_name
        self.last_name = last_name if last_name is not None else self.last_name
        self.country = country if country is not None else self.country
        self.balance = float(balance) if balance is not None else self.balance
        self.vip_level = int(vip_level) if vip_level is not None else self.vip_level
        self.payment_methods = json.loads(payment_methods) if payment_methods is not None else self.payment_methods

    def write_content(self):
        return (f"ID: {self.id}\n"
                f"NAME: {self.first_name} {self.last_name}\n"
                f"COUNTRY: {self.country}\n"
                f"BALANCE: {self.balance}\n"
                f"VIP LEVEL: {self.vip_level}\n"
                f"PAYMENT METHODS: {self.payment_methods}\n")

    def get_id(self):
        return self.id
