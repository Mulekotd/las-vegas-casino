class Bet:
    def __init__(self, id, client_id, game_id, amount, outcome, payout, datetime, odds_breakdown):
        self.id = int(id)                    # primary key
        self.client_id = client_id
        self.game_id = int(game_id)
        self.amount = float(amount)
        self.outcome = outcome               # win | lose | push
        self.payout = float(payout)
        self.datetime = datetime             # ISO datetime string
        self.odds_breakdown = odds_breakdown # [1.92, 1.5, 1.3]

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
