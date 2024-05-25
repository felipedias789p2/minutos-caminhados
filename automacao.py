import os 
from pathlib import Path

listar_pastas = os.listdir()

numero_pastas = len([x for x in listar_pastas if Path(x).is_dir()])

print(f"Contém {numero_pastas} pastas")
