import json

class Game:
    def __init__(self, id, name, house_edge, min_bet, max_bet, category, active, rules):
        self.id = int(id)
        self.name = name
        self.house_edge = float(house_edge)
        self.min_bet = float(min_bet)
        self.max_bet = float(max_bet)
        self.category = category
        self.active = bool(active)
        self.rules = json.loads(rules)

    def update(self, id=None, name=None, house_edge=None, min_bet=None, max_bet=None, category=None, active=None, rules=None):
        self.id = int(id) if id is not None else self.id
        self.name = name if name is not None else self.name
        self.house_edge = float(house_edge) if house_edge is not None else self.house_edge
        self.min_bet = float(min_bet) if min_bet is not None else self.min_bet
        self.max_bet = float(max_bet) if max_bet is not None else self.max_bet
        self.category = category if category is not None else self.category
        self.active = bool(active) if active is not None else self.active
        self.rules = json.loads(rules) if rules is not None else self.rules
    
    def write_content(self):
        return (f"GAME ID: {self.id}\n"
                f"NAME: {self.name}\n"
                f"HOUSE EDGE: {self.house_edge}\n"
                f"BET RANGE: {self.min_bet} - {self.max_bet}\n"
                f"CATEGORY: {self.category}\n"
                f"ACTIVE: {self.active}\n"
                f"RULES: {self.rules}\n")

    def get_id(self):
        return self.id
