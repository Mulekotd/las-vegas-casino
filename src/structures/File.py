import os
from src.utils import calculate_execution_time

class File:
    def __init__(self, path: str):
        self.path = path

    def extract_data(self) -> list[str]:
        time, lines = calculate_execution_time(self.read)

        print(f"Arquivo: {self.path}")
        print(f"Tempo de leitura: {time:.2f}ms", end="\n\n")

        if not lines:
            return []

        return [line.strip() for line in lines if line.strip()]
    
    def write(self, content: str) -> None:
        directory = os.path.dirname(self.path)
        
        if directory:
            os.makedirs(directory, exist_ok=True)
        
        with open(self.path, "w", encoding="utf-8") as f:
            f.write(content)

    def read(self) -> list[str]:
        with open(self.path, encoding="utf-8") as f:
            return f.readlines()

    def append(self, new_line: str) -> None:
        directory = os.path.dirname(self.path)

        if directory:
            os.makedirs(directory, exist_ok=True)
        
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(new_line + "\n")
