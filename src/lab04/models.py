import sys
import os

# Configuração de caminhos para reutilizar Lab 01 e Lab 03
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(BASE_DIR, 'lab01'))
sys.path.insert(0, os.path.join(BASE_DIR, 'lab03'))

from model import Athlete
from interfaces import ITrainable, IReportable

class ProfessionalAthlete(Athlete, ITrainable, IReportable):
    """Atleta Pro: Implementa múltiplas interfaces (Nota 4)."""
    
    def __init__(self, name, age, sport, weight, height, salary, sponsor):
        super().__init__(name, age, sport, weight, height)
        self._salary = salary
        self._sponsor = sponsor

    # Implementação obrigatória de ITrainable (Nota 3)
    def execute_workout(self):
        self.treinar(120) # Usa lógica da base
        print(f"  [CONTRATO PRO] Treino de elite focado em performance para {self.name}.")

    # Implementação obrigatória de IReportable (Nota 3)
    def get_summary(self) -> str:
        return f"RELATÓRIO PRO: {self.name} | Patrocínio: {self._sponsor} | Rating: {self.rating}"

class AmateurAthlete(Athlete, ITrainable, IReportable):
    """Atleta Amador: Implementa as mesmas interfaces com comportamentos diferentes."""
    
    def __init__(self, name, age, sport, weight, height, club, occupation):
        super().__init__(name, age, sport, weight, height)
        self._club = club
        self._occupation = occupation

    def execute_workout(self):
        self.treinar(45)
        print(f"  [CONTRATO AMADOR] Treino recreativo para {self.name} no clube {self._club}.")

    def get_summary(self) -> str:
        return f"RESUMO AMADOR: {self.name} | Ocupação: {self._occupation} | IMC: {self.imc}"
