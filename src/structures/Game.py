class Game:
    def __init__(self, id, name, house_edge, min_bet, max_bet, category, active, rules):
        self.id = int(id)
        self.name = name
        self.house_edge = float(house_edge)
        self.min_bet = float(min_bet)
        self.max_bet = float(max_bet)
        self.category = category
        self.active = bool(active)
        self.rules = rules

    def show_details(self):
        print("GAME ID:", self.id)
        print("NAME:", self.name)
        print("HOUSE EDGE:", self.house_edge)
        print("BET RANGE:", self.min_bet, "-", self.max_bet)
        print("CATEGORY:", self.category)
        print("ACTIVE:", self.active)
        print("RULES:", self.rules, end="\n\n")

    def get_id(self):
        return self.id
