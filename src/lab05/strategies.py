"""
Módulo de estratégias para o Lab 05.
Contém funções de ordenação, filtros e callable-objects.
"""

# --- Estratégias de Ordenação (Nível 3) ---
def sort_by_name(athlete):
    """Retorna o nome para ordenação."""
    return athlete.name

def sort_by_rating(athlete):
    """Retorna o rating para ordenação."""
    return athlete.rating

def sort_by_age_and_weight(athlete):
    """Ordenação composta: idade e depois peso."""
    return (athlete.age, athlete.weight)

# --- Fábrica de Funções (Nível 4) ---
def make_rating_filter(min_rating):
    """Cria um filtro personalizado para rating mínimo."""
    def filter_fn(athlete):
        return athlete.rating >= min_rating
    return filter_fn

# --- Filtros Simples (Nível 3) ---
def is_professional(athlete):
    """Filtra apenas instâncias de ProfessionalAthlete."""
    from models import ProfessionalAthlete
    return isinstance(athlete, ProfessionalAthlete)

# --- Pattern Strategy via Callable-Objects (Nível 5) ---
class TrainingBonusStrategy:
    """Aplica um bónus de rating como um objeto chamável."""
    def __init__(self, bonus_multiplier):
        self.multiplier = bonus_multiplier

    def __call__(self, athlete): #Callable Objects (__call__): Objects that can be invoked like functions
        bonus = int(athlete.rating * self.multiplier)
        athlete._rating += bonus # Acesso direto para fins acadêmicos
        return athlete

a = TrainingBonusStrategy()

