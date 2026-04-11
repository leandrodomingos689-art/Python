from base import BaseAthlete
from models import ProfessionalAthlete, AmateurAthlete
from collection import AthleteCollection

def main():
    team = AthleteCollection()
    
    # Criando instâncias (Nota 3)
    p1 = ProfessionalAthlete("Cristiano", 39, "Futebol", 85, 187, 50000, "Nike")
    a1 = AmateurAthlete("Carlos", 20, "Corrida", 70, 175, "Lisboa Runners", "Estudante")
    
    team.add(p1)
    team.add(a1)

    print("="*60)
    print("DEMO LAB 03 - POLIMORFISMO E HIERARQUIA")
    print("="*60)

    # CENÁRIO 1: Polimorfismo Puro (Nota 5) - Sem usar 'if'
    print("\n🔹 CENÁRIO 1: Cálculo de Performance (Polimorfismo)")
    for ath in team:
        # Chamada única, resultados diferentes por classe
        print(f"Atleta: {ath.name:<12} | Performance: {ath.calculate_performance()}")

    # CENÁRIO 2: Filtragem por Tipo (Nota 5) e isinstance (Nota 4)
    print("\n🔹 CENÁRIO 2: Filtragem de Objetos (Apenas Profissionais)")
    pros = [ath for ath in team if isinstance(ath, ProfessionalAthlete)]
    for pro in pros:
        print(f"Encontrado: {pro.name} | {pro.promote_sponsor()}")

    # CENÁRIO 3: Métodos de Negócio e Sobrescrita (Nota 3 e 4)
    print("\n🔹 CENÁRIO 3: Métodos de Negócio e Herança")
    print(f"Ação do Amador: {a1.get_club_info()}")
    print(f"Treino do Profissional:")
    p1.treinar(60) # Usa o método sobrescrito que dá bónus
    print(f"Novo Rating {p1.name}: {p1.rating}")

if __name__ == "__main__":
    main()
