import json
from src.utils import get_breakline

from .File import File
from .Bet import Bet
from .Client import Client
from .Game import Game
from .Movimentation import Movimentation


# === CONSTANTS ===
ENTITY_MAP = {
    "Bets": "bets",
    "Clientes": "clients",
    "Jogos": "games",
    "Movimentações": "movimentations",
}

ACTIONS_MAP = {
    1: "read",
    2: "visualize",
    3: "create",
    4: "update",
    5: "delete",
}

options = list(ENTITY_MAP.keys()) + ["Sair"]
sub_options = ["Listar", "Visualizar", "Adicionar", "Editar", "Excluir", "Voltar"]


class Program:
    def __init__(self):
        # collections
        self.bets: list[Bet] = []
        self.clients: list[Client] = []
        self.games: list[Game] = []
        self.movimentations: list[Movimentation] = []

        # states
        self.is_running = True
        self.selected_type = None
        self.selected_action = None

        # saída
        self.output_file = "output.txt"

        # metadatas
        self.entity_configs = {
            "bets": {
                "file": "database/bets.txt",
                "cls": Bet,
                "parser": lambda b: Bet(*b[:-1], json.loads(b[-1]))
            },
            "clients": {
                "file": "database/clients.txt",
                "cls": Client,
                "parser": lambda c: Client(*c[:-1], json.loads(c[-1]))
            },
            "games": {
                "file": "database/games.txt",
                "cls": Game,
                "parser": lambda g: Game(*g[:-1], json.loads(g[-1]))
            },
            "movimentations": {
                "file": "database/movimentations.txt",
                "cls": Movimentation,
                "parser": lambda m: Movimentation(*m[:-1], json.loads(m[-1]))
            },
        }

    def init(self):
        for key, config in self.entity_configs.items():
            setattr(self, key, self.load_entities(config["file"], config["parser"]))

    def load_entities(self, filepath: str, parser):
        file = File(filepath)
        data = file.extract_data()
        entities = []

        for line in data:
            parts = line.split(";")
            entities.append(parser(parts))
        
        return entities

    def loop(self):
        while self.is_running:
            self.display_menu(options)
            choose = self.choose_option(len(options))
            self.actions(choose)

    def display_menu(self, items: list[str]):
        for i, item in enumerate(items, 1):
            breakline = get_breakline("TWO_LINES") if i == len(items) else get_breakline("NEW_LINE")
            print(f"{i} - {item}", end=breakline)

    def choose_option(self, max_option: int) -> int:
        try:
            choose = int(input("Escolha uma opção pelo número: "))

            if 1 <= choose <= max_option:
                return choose
        except ValueError:
            pass

        print("Opção inválida.\n")
        return -1

    def actions(self, choose: int):
        if choose == len(options):
            print("Programa finalizado com sucesso.")
            self.is_running = False
            return

        if choose <= 0:
            return

        self.selected_type = options[choose - 1]
        print(f"\n--- {self.selected_type} ---\n")
        self.submenu_loop()

    def submenu_loop(self):
        while True:
            self.display_menu(sub_options)
            sub = self.choose_option(len(sub_options))

            if sub == len(sub_options):
                print("\nRetornando ao menu principal...\n")
                break

            if sub not in ACTIONS_MAP:
                print("Opção inválida de ação.\n")
                continue

            self.selected_action = ACTIONS_MAP[sub]
            self.perform_action()

    def perform_action(self):
        entity_name = ENTITY_MAP[self.selected_type]
        entity_list = getattr(self, entity_name)

        match self.selected_action:
            case "read":
                if not entity_list:
                    print("Nenhum registro encontrado.\n")
                    return

                print("\nPressione ENTER para avançar, ou 'q' para sair.\n")

                for i, entity in enumerate(entity_list, 1):
                    entity.show_details()
                    print(f"[{i}/{len(entity_list)}]")
                    
                    user_input = input().lower().strip()
                    if user_input == "q":
                        break

            case "visualize":
                pk = int(input("Digite a chave primária: ").strip())
                found = next((entity for entity in entity_list if entity.get_id() == pk), None)
                print()
                
                if found: found.show_details()
                else: print("Nenhum registro encontrado. \n")

            case "create":
                print("TODO: criar rotina de inserção dessa entidade")
            case "update":
                print("TODO: criar rotina de edição dessa entidade")
            case "delete":
                print("TODO: criar rotina de exclusão dessa entidade")
