from base import BaseAthlete

class ProfessionalAthlete(BaseAthlete):
    def __init__(self, name, age, sport, weight, height, salary, sponsor):
        super().__init__(name, age, sport, weight, height)
        self._salary = salary
        self._sponsor = sponsor

    def calculate_performance(self):
        return round(self.rating * 1.5, 2)

    def promote_sponsor(self):
        return f"Atleta {self.name} promove {self._sponsor}."

class AmateurAthlete(BaseAthlete):
    def __init__(self, name, age, sport, weight, height, club, occupation):
        super().__init__(name, age, sport, weight, height)
        self._club = club
        self._occupation = occupation

    def calculate_performance(self):
        return round(self.rating * 1.1, 2)

    def get_club_info(self):
        return f"Clube: {self._club}."
