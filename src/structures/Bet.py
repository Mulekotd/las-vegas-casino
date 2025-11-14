import json

class Bet:
    def __init__(self, id, client_id, game_id, amount, outcome, payout, datetime, odds_breakdown):
        self.id = int(id)
        self.client_id = client_id
        self.game_id = int(game_id)
        self.amount = float(amount)
        self.outcome = outcome
        self.payout = float(payout)
        self.datetime = datetime
        self.odds_breakdown = json.loads(odds_breakdown)

    def update(self, id=None, client_id=None, game_id=None, amount=None, outcome=None, payout=None, datetime=None, odds_breakdown=None):
        self.id = int(id) if id is not None else self.id
        self.client_id = client_id if client_id is not None else self.client_id
        self.game_id = int(game_id) if game_id is not None else self.game_id
        self.amount = float(amount) if amount is not None else self.amount
        self.outcome = outcome if outcome is not None else self.outcome
        self.payout = float(payout) if payout is not None else self.payout
        self.datetime = datetime if datetime is not None else self.datetime
        self.odds_breakdown = json.loads(odds_breakdown) if odds_breakdown is not None else self.odds_breakdown

    def show_details(self):
        print("BET ID:", self.id)
        print("CLIENT:", self.client_id)
        print("GAME:", self.game_id)
        print("AMOUNT:", self.amount)
        print("OUTCOME:", self.outcome)
        print("PAYOUT:", self.payout)
        print("DATETIME:", self.datetime, end="\n\n")

    def get_id(self):
        return self.id
