import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(BASE_DIR, 'lab01'))
from model import Athlete

class AthleteCollection:
    def __init__(self, items=None):
        self._items = items if items is not None else []

    def add(self, athlete):
        if isinstance(athlete, Athlete):
            self._items.append(athlete)
        return self

    # --- Nível 4: Métodos de Ordem Superior ---
    def sort_by(self, key_func):
        """Ordena a coleção usando a estratégia fornecida."""
        self._items.sort(key=key_func)
        return self # Retorna self para encadeamento

    def filter_by(self, predicate):
        """Filtra a coleção e retorna uma nova instância (Nível 4/5)."""
        new_items = list(filter(predicate, self._items))
        return AthleteCollection(new_items)

    # --- Nível 5: Método Apply e Transformação ---
    def apply(self, func):
        """Aplica uma função/estratégia a todos os elementos (Nível 5)."""
        self._items = [func(item) for item in self._items]
        return self

    def get_all(self):
        return self._items

    def __iter__(self):
        return iter(self._items)
