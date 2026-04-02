import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.lab01.model import Athlete

class AthleteCollection:
    """Contentor para gerir objetos Athlete (Lab 02)."""
    
    def __init__(self):
        self._items = []

    # --- Requisitos Nível 3 ---
    def add(self, athlete):
        """Adiciona um atleta com verificação de tipo."""
        if not isinstance(athlete, Athlete):
            raise TypeError("Erro: Apenas objetos da classe Athlete podem ser adicionados.")
        
        # Nível 4: Bloqueio de duplicados (usa o __eq__ do Lab 01)
        if athlete in self._items:
            raise ValueError(f"Erro: O atleta '{athlete.name}' já existe na coleção.")
            
        self._items.append(athlete)

    def remove(self, athlete):
        """Remove um objeto atleta específico."""
        if athlete in self._items:
            self._items.remove(athlete)

    def get_all(self):
        """Retorna a lista completa."""
        return self._items

    # --- Requisitos Nível 4 ---
    def find_by_name(self, name):
        """Pesquisa atletas pelo nome (parcial)."""
        return [a for a in self._items if name.lower() in a.name.lower()]

    def __len__(self):
        """Permite usar len(colecao)."""
        return len(self._items)

    def __iter__(self):
        """Permite usar 'for athlete in colecao'."""
        return iter(self._items)

    # --- Requisitos Nível 5 ---
    def __getitem__(self, index):
        """Permite acesso por índice: colecao[0]."""
        return self._items[index]

    def remove_at(self, index):
        """Remove um atleta numa posição específica."""
        if 0 <= index < len(self._items):
            return self._items.pop(index)
        raise IndexError("Índice fora do intervalo da coleção.")

    def sort_by_rating(self, reverse=True):
        """Ordena a coleção por Rating."""
        self._items.sort(key=lambda a: a.rating, reverse=reverse)

    def get_active(self):
        """Retorna apenas os atletas com estado ativo."""
        return [a for a in self._items if a._active]
