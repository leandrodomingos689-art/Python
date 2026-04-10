import sys
import os

# 1. Configuração de Caminho Único
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(BASE_DIR, 'lab01'))
sys.path.insert(0, os.path.join(BASE_DIR, 'lab02'))

# 2. Importações
from model import Athlete
from collection import AthleteCollection
from models import ProfessionalAthlete, AmateurAthlete

def main():
    print("="*50)
    print("DEMO LAB 03 - FINAL")
    print("="*50)

    team = AthleteCollection()
    
    # Criar atletas
    p1 = ProfessionalAthlete("Cristiano", 39, "Futebol", 85, 187, 50000, "Nike")
    a1 = AmateurAthlete("Carlos", 20, "Corrida", 70, 175, "Clube Local", "Estudante")
    
    try:
        team.add(p1)
        team.add(a1)
        print("✅ Atletas adicionados com sucesso!")
        
        print("\n--- PERFORMANCE POLIMÓRFICA ---")
        for ath in team:
            print(f"Atleta: {ath.name:<12} | Perf: {ath.calculate_performance()}")
            
    except TypeError as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main()
