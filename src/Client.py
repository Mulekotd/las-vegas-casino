class Client:
    def __init__(self, uuid, first_name, last_name, country, balance, vip_level, payment_methods):
        self.uuid = uuid
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.balance = float(balance)
        self.vip_level = int(vip_level)   
        self.payment_methods = payment_methods # ["PIX", "CREDIT_CARD", "BTC"]

    def show_details(self):
        print("UUID:", self.uuid)
        print("NAME:", self.first_name, self.last_name)
        print("COUNTRY:", self.country)
        print("BALANCE:", self.balance)
        print("VIP LEVEL:", self.vip_level)
        print("PAYMENT METHODS:", self.payment_methods, end="\n\n")
