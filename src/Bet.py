class Bet:
    def __init__(self, bet_id, client_uuid, game_id, amount, outcome, payout, datetime, odds_breakdown):
        self.bet_id = int(bet_id)            # primary key
        self.client_uuid = client_uuid
        self.game_id = int(game_id)
        self.amount = float(amount)
        self.outcome = outcome               # win | lose | push
        self.payout = float(payout)
        self.datetime = datetime             # ISO datetime string
        self.odds_breakdown = odds_breakdown # [1.92, 1.5, 1.3]

    def show_details(self):
        print("BET ID:", self.bet_id)
        print("CLIENT:", self.client_uuid)
        print("GAME:", self.game_id)
        print("AMOUNT:", self.amount)
        print("OUTCOME:", self.outcome)
        print("PAYOUT:", self.payout)
        print("DATETIME:", self.datetime, end="\n\n")
