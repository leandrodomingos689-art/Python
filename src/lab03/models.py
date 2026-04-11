from base import BaseAthlete

class ProfessionalAthlete(BaseAthlete):
    """Subclasse para Nota 3, 4 e 5"""
    def __init__(self, name, age, sport, weight, height, salary, sponsor):
        super().__init__(name, age, sport, weight, height)
        self._salary = salary
        self._sponsor = sponsor

    def __str__(self): # Sobrescrita (Nota 4)
        return f"[PRO] {super().__str__()} | Patrocínio: {self._sponsor}"

    def calculate_performance(self): # Polimorfismo Puro (Nota 5)
        return round(self.rating * 1.5, 2)

    def treinar(self, minutos): # Sobrescrita de método de negócio
        super().treinar(minutos)
        self._rating += 5 # Bónus pro
        print(f"  [Bónus Pro] +5 pontos de rating por treino intenso.")

    def promote_sponsor(self): # Novo método (Nota 3)
        return f"Atleta {self.name} está em campanha para a {self._sponsor}."

class AmateurAthlete(BaseAthlete):
    def __init__(self, name, age, sport, weight, height, club, occupation):
        super().__init__(name, age, sport, weight, height)
        self._club = club
        self._occupation = occupation

    def __str__(self):
        return f"[AMADOR] {super().__str__()} | Clube: {self._club}"

    def calculate_performance(self):
        return round(self.rating * 1.1, 2)

    def get_club_info(self): # Novo método (Nota 3)
        return f"Representa orgulhosamente o clube: {self._club}."
