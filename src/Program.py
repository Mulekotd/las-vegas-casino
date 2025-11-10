import json
from .utils import get_breakline

from .File import File

from .Bet import Bet
from .Client import Client
from .Game import Game
from .Movimentation import Movimentation

# constants
ENTITY_MAP = {
    "Bets": "bets",
    "Clientes": "clients",
    "Jogos": "games",
    "Movimentações": "movimentations"
}

CRUD_MAP = {
    1: "read",
    2: "create",
    3: "update",
    4: "delete"
}

options = ["Bets", "Clientes", "Jogos", "Movimentações", "Sair"]
options_len = len(options)

sub_options = ["Listar", "Adicionar", "Editar", "Excluir"]
sub_options_len = len(sub_options)

class Program:
    def __init__(self):
        self.bets:    list[Bet] = []
        self.clients: list[Client] = []
        self.games:   list[Game] = []
        self.movimentations: list[Movimentation] = []

        self.output_file = "output.txt"

        # states
        self.is_running = True
        self.selected_type = None # bets | clients | games | movimentations
        self.selected_action = None # create | read | update | delete
    
    def init(self):
        bets_file    = File("database/bets.txt")
        clients_file = File("database/clients.txt")
        games_file   = File("database/games.txt")
        movimentations_file = File("database/movimentations.txt")

        bets_data    = bets_file.extract_data()
        clients_data = clients_file.extract_data()
        games_data   = games_file.extract_data()
        movimentations_data = movimentations_file.extract_data()

        for b in bets_data:
            b_id, b_client_uuid, b_game_id, b_amount, b_outcome, b_payout, b_datetime, b_odds_breakdown = b.split(";")
            new_bet = Bet(b_id,
                          b_client_uuid,
                          b_game_id,
                          b_amount,
                          b_outcome,
                          b_payout,
                          b_datetime,
                          json.loads(b_odds_breakdown))
            
            self.bets.append(new_bet)

        for c in clients_data:
            c_uuid, c_first_name, c_last_name, c_country, c_balance, c_vip_level, c_payment_methods = c.split(";")
            new_client = Client(c_uuid,
                                c_first_name,
                                c_last_name,
                                c_country,
                                c_balance,
                                c_vip_level,
                                json.loads(c_payment_methods))
            
            self.clients.append(new_client)

        for g in games_data:
            g_id, g_name, g_house_edge, g_min_bet, g_max_bet, g_category, g_active, g_rules = g.split(";")
            new_game = Game(g_id,
                            g_name,
                            g_house_edge,
                            g_min_bet,
                            g_max_bet,
                            g_category,
                            g_active,
                            json.loads(g_rules))
            
            self.games.append(new_game)

        for m in movimentations_data:
            m_id, m_sender, m_recipient, m_amount, m_datetime, m_transaction_type, m_tags = m.split(";")
            new_movimentation = Movimentation(m_id,
                                              m_sender,
                                              m_recipient,
                                              m_amount,
                                              m_datetime,
                                              m_transaction_type,
                                              json.loads(m_tags))
            
            self.movimentations.append(new_movimentation)
    
    def actions(self, choose: int):
        if choose == 5:
            print("Programa finalizado com sucesso.")
            self.is_running = False
            return
        
        if choose < 1 or choose > 5:
            print("Opção inválida.")
            return

        self.selected_type = options[choose-1]

        for index, sub in enumerate(sub_options, 1):
            breakline = get_breakline("TWO_LINES") if index == sub_options_len else get_breakline("NEW_LINE")
            print(f"{index} - {sub} {self.selected_type}", end=breakline)
        
        sub = int(input("Escolha a ação pelo número: "))
        if sub not in CRUD_MAP:
            print("Opção inválida de ação.")
            return
        
        self.selected_action = CRUD_MAP[sub]
        self.perform_action()

    def perform_action(self):
        entity_name = ENTITY_MAP[self.selected_type]
        entity_list = getattr(self, entity_name)

        match self.selected_action:
            case "read":
                for entity in entity_list:
                    entity.show_details()
            case "create":
                print("TODO: criar rotina de inserção dessa entidade")
            case "update":
                print("TODO: criar rotina de edição dessa entidade")
            case "delete":
                print("TODO: criar rotina de exclusão dessa entidade")

    def loop(self):
        while self.is_running:
            for index, option in enumerate(options, 1):                
                breakline = get_breakline("TWO_LINES") if index == options_len else get_breakline("NEW_LINE")
                print(f"{index} - {option}", end=breakline)
            
            choose = int(input("Escolha a opção pelo número: "))
            self.actions(choose)
