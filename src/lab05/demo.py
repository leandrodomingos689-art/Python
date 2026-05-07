import sys
import os

# Configuração de caminhos para evitar o erro de importação anterior
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
sys.path = [p for p in sys.path if 'lab02' not in p]
sys.path.insert(0, CURRENT_DIR)
sys.path.insert(1, os.path.join(BASE_DIR, 'lab01'))
sys.path.insert(2, os.path.join(BASE_DIR, 'lab03'))

from collection import AthleteCollection
from models import ProfessionalAthlete, AmateurAthlete
import strategies as st

def main():
    # SETUP: Criando a coleção com 5 atletas (Requisito Nota 3)
    team = AthleteCollection()
    team.add(ProfessionalAthlete("Cristiano", 39, "Futebol", 85, 187, 50000, "Nike"))
    team.add(ProfessionalAthlete("Rebeca", 25, "Ginástica", 48, 155, 15000, "Adidas"))
    team.add(AmateurAthlete("Carlos", 20, "Corrida", 70, 175, "Lisboa Runners", "Estudante"))
    team.add(AmateurAthlete("Ana", 19, "Volei", 65, 170, "Escola A", "Estudante"))
    team.add(ProfessionalAthlete("Neymar", 32, "Futebol", 68, 175, 40000, "Puma"))

    print("="*65)
    print("      LABORATÓRIO 05 - PROGRAMAÇÃO FUNCIONAL E ESTRATÉGIAS")
    print("="*65)

    # --- CENÁRIO 1: CADEIA DE OPERAÇÕES (Nota 5) ---
    print("\n🔹 CENÁRIO 1: Cadeia (Filter PRO -> Rating > 1000 -> Sort Rating)")
    # Fábrica de funções (Nota 4)
    rating_filter = st.make_rating_filter(1000)
    
    result = (team
              .filter_by(st.is_professional)
              .filter_by(rating_filter)
              .sort_by(st.sort_by_rating))
    
    # SAÍDA: Usando MAP para extrair apenas os nomes (Nota 4)
    nomes_pro = list(map(lambda x: x.name, result.get_all()))
    print(f" -> Resultados Filtrados: {nomes_pro}")

    # --- CENÁRIO 2: TROCA DE ESTRATÉGIAS (Nota 3) ---
    print("\n🔹 CENÁRIO 2: Diferentes Estratégias de Ordenação")
    
    # Estratégia A: Por Nome
    team.sort_by(st.sort_by_name)
    print(f" -> Ordenado por Nome: {[a.name for a in team]}")
    
    # Estratégia B: Por Idade (usando Lambda - Nota 4)
    team.sort_by(lambda x: x.age)
    print(f" -> Ordenado por Idade: {[(a.name, a.age) for a in team]}")

    # --- CENÁRIO 3: CALLABLE OBJECT STRATEGY (Nota 5) ---
    print("\n🔹 CENÁRIO 3: Aplicação de Bónus via Callable Object")
    bonus_10_percent = st.TrainingBonusStrategy(0.10)
    
    # Aplica a estratégia a todos (Método Apply - Nota 5)
    team.apply(bonus_10_percent)
    
    print(" -> Novos Ratings (após bónus de 10%):")
    for a in team:
        print(f"    Atleta: {a.name:<12} | Rating: {a.rating}")

    print("\n" + "="*65)
    print("✅ EXECUÇÃO FINALIZADA COM SUCESSO!")

if __name__ == "__main__":
    main()
S