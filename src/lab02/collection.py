from model import Athlete

class AthleteCollection:
    def __init__(self):
        self._items = []

    def add(self, athlete):
        if not isinstance(athlete, Athlete):
            raise TypeError(f"Erro: Esperado Athlete, recebido {type(athlete)}")
        if athlete in self._items:
            raise ValueError("Atleta já existe.")
        self._items.append(athlete)

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)
