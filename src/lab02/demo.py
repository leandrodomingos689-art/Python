import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.lab01.model import Athlete
from collection import AthleteCollection

def main():
    print("="*50)
    print("LABORATÓRIO 02 - COLEÇÕES DE ATLETAS")
    print("="*50)

    team = AthleteCollection()

    # 1. CRIAÇÃO E ADIÇÃO (Nível 3)
    print("\n[1] Добавление спортсменов:")
    a1 = Athlete("João Silva", 25, "Futebol", 75, 180)
    a2 = Athlete("Maria Souza", 22, "Natação", 60, 165)
    a3 = Athlete("Carlos Ferro", 30, "Boxe", 90, 185)
    
    team.add(a1)
    team.add(a2)
    team.add(a3)
    print(f"   Coleção criada com {len(team)} atletas.")

    # 2. RESTRIÇÕES (Nível 4)
    print("\n[2]Ограничения тестирования (дубликаты и тип):")
    try:
        team.add(a1) # Tentativa de duplicado
    except ValueError as e:
        print(f"   Блокировка дубликатов: {e}")
    
    try:
        team.add("Não sou atleta")
    except TypeError as e:
        print(f"   Bloqueio de tipo: {e}")

    # 3. ITERAÇÃO E ACESSO (Nível 4 e 5)
    print("\n[3] Демонстрация итерации и индексирования:")
    print(f"   Atleta na posição 0: {team[0]}")
    for i, ath in enumerate(team):
        print(f"   Iteração {i}: {ath.name} | Rating: {ath.rating}")

    # 4. PESQUISA E FILTRO (Nível 4 e 5)
    print("\n[4] PИсследования и логика в бизнесе (активы):")
    a2.desativar() # Desativa a Maria
    ativos = team.get_active()
    print(f"   Total Ativos: {len(ativos)}")
    
    busca = team.find_by_name("Silva")
    if busca:
        print(f"   Busca por 'Silva' encontrou: {busca[0].name}")

    # 5. ORDENAÇÃO E REMOÇÃO (Nível 5)
    print("\n[5] Сортировка и удаление по индексу:")
    # Simular treinos para mudar ratings
    a1.treinar(100) # +10 pontos
    team.sort_by_rating()
    print(f"   Top Atleta (Rating): {team[0].name} com {team[0].rating}")
    
    removido = team.remove_at(2)
    print(f"   Removido da posição 2: {removido.name}")
    print(f"   Tamanho final da coleção: {len(team)}")

if __name__ == "__main__":
    main()
