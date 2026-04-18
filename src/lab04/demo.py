import sys
import os

# 1. Configuração de Caminhos Absolutos
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(BASE_DIR, 'lab01'))
sys.path.insert(0, os.path.join(BASE_DIR, 'lab02'))
# Garante que o models do lab04 é o primeiro a ser lido
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))) 

# 2. Importações
from collection import AthleteCollection
from interfaces import ITrainable, IReportable
from models import ProfessionalAthlete, AmateurAthlete

def process_gym_session(items: list[ITrainable]):
    """Função Universal (Requisito Nota 4)"""
    print("\n--- 🔹 CENÁRIO 1: Sessão de Treino (Interface ITrainable) ---")
    for item in items:
        # Polimorfismo puro via interface (Nota 5)
        item.execute_workout()

def main():
    print("="*65)
    print("      LABORATÓRIO 04 - EXECUÇÃO DOS 3 CENÁRIOS (NÍVEL 5)")
    print("="*65)

    # Inicialização da Coleção (Lab 02)
    team = AthleteCollection()
    
    # Criando instâncias com múltiplas interfaces (Nota 4)
    p1 = ProfessionalAthlete("Cristiano", 39, "Futebol", 85, 187, 50000, "Nike")
    a1 = AmateurAthlete("Carlos", 20, "Corrida", 70, 175, "Lisboa Runners", "Estudante")
    
    team.add(p1)
    team.add(a1)

    # --- CENÁRIO 1: Polimorfismo via Função Universal ---
    # Usa o contrato ITrainable para todos
    process_gym_session(team.get_all())

    # --- CENÁRIO 2: Filtragem por Interface (Requisito Nota 5) ---
    print("\n--- 🔹 CENÁRIO 2: Sistema de Relatórios (Filtro IReportable) ---")
    # Usando o novo método que adicionamos na AthleteCollection
    reportables = team.get_by_interface(IReportable)
    for obj in reportables:
        print(f" > {obj.get_summary()}")

    # --- CENÁRIO 3: Validação de Contratos (Requisito Nota 4) ---
    print("\n--- 🔹 CENÁRIO 3: Validação de Contratos (isinstance) ---")
    for ath in team:
        train_ok = "SIM" if isinstance(ath, ITrainable) else "NÃO"
        report_ok = "SIM" if isinstance(ath, IReportable) else "NÃO"
        print(f"Objeto: {ath.name:<10} | Trainable: {train_ok} | Reportable: {report_ok}")

    print("\n" + "="*65)
    print("✅ EXECUÇÃO FINALIZADA COM SUCESSO!")

# 3. CHAMADA DA FUNÇÃO (Vital para o código correr)
if __name__ == "__main__":
    main()
