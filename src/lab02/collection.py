import sys
import os

# Garante que a coleção consegue encontrar o model original
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(BASE_DIR, 'lab01'))

from model import Athlete

class AthleteCollection:
    """
    Contentor evoluído do Lab 02.
    Gerencia objetos Athlete e suporta filtragem por Interface (Lab 04).
    """
    def __init__(self):
        self._items = []

    # --- Requisitos Lab 02 ---
    def add(self, athlete):
        """Adiciona e valida o tipo (Nota 3 do Lab 02)."""
        if not isinstance(athlete, Athlete):
            raise TypeError(f"Erro: Esperado objeto Athlete, recebido {type(athlete)}")
        
        # Bloqueio de duplicados (Nota 4 do Lab 02)
        if athlete in self._items:
            raise ValueError(f"Atleta {athlete.name} já existe na coleção.")
            
        self._items.append(athlete)

    def get_all(self):
        """Retorna todos os itens (Requisito essencial para integração)."""
        return self._items

    def __len__(self):
        """Permite usar len(colecao) (Nota 4 do Lab 02)."""
        return len(self._items)

    def __iter__(self):
        """Permite usar for item in colecao (Nota 4 do Lab 02)."""
        return iter(self._items)

    def __getitem__(self, index):
        """Permite acesso por índice [0] (Nota 5 do Lab 02)."""
        return self._items[index]

    # --- Ajuste Especial para o Lab 04 (Nível 5) ---
    def get_by_interface(self, interface_class):
        """
        Filtra a coleção por uma Interface específica (ABC).
        Exemplo: colecao.get_by_interface(ITrainable)
        """
        return [item for item in self._items if isinstance(item, interface_class)]
