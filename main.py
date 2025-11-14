from src.structures.Program import Program
from src.utils import calculate_execution_time

print("============================")
print("===== LAS VEGAS CASINO =====")
print("============================")

app = Program()
app.init()
app.loop()
time,_ = calculate_execution_time(app.close)

print(f"\nTempo de geração de arquivos output {time:.2f} ms\n")
