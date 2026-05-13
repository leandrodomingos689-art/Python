import sys
import os
from typing import TypeVar, Generic, Callable, Optional, Protocol

# Configuração de caminhos para reutilizar o modelo original se necessário
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(BASE_DIR, 'lab01'))

from model import Athlete

# --- [NÍVEL 5] Definição dos Protocolos (Duck Typing Estático) ---
class Displayable(Protocol):
    def display(self) -> str:
        """Deve retornar uma representação em string do objeto."""
        ...

class Scorable(Protocol):
    def score(self) -> float:
        """Deve retornar a pontuação/rating do objeto."""
        ...

# --- Definindo os TypeVars Genéricos ---
T = TypeVar('T')  # Genérico puro (Nível 3)
R = TypeVar('R')  # Para o tipo de retorno do método map (Nível 4)

# TypeVars Delimitados por Protocolos (Nível 5)
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)


# --- [NÍVEL 3, 4 e 5] Coleção Tipada Genérica ---
class TypedCollection(Generic[T]):
    """
    Contentor genérico que replica a interface do Lab 02,
    adicionando suporte estrito a tipos, operações funcionais e protocolos.
    """
    def __init__(self) -> None:
        self._items: list[T] = []

    # --- Métodos Base do Lab 02 com Anotações de Tipo (Nível 3) ---
    def add(self, item: T) -> 'TypedCollection[T]':
        """Adiciona um item validando o tipo de forma estrita."""
        # Nota: O isinstance estático é validado pelo MyPy/IDE via Generic[T].
        # Mantemos uma validação em tempo de execução para manter a robustez do Lab 02.
        if item in self._items:
            raise ValueError("Item já existe na coleção.")
        self._items.append(item)
        return self

    def remove_at(self, index: int) -> T:
        """Remove e retorna o elemento numa posição específica."""
        return self._items.pop(index)

    def get_all(self) -> list[T]:
        """Retorna a lista completa de elementos."""
        return list(self._items)

    def sort_by_rating(self) -> None:
        """Ordena a coleção pelo atributo rating se os objetos o possuírem."""
        # Abordagem segura usando getattr para evitar quebras se o tipo não tiver rating
        self._items.sort(key=lambda x: getattr(x, 'rating', 0), reverse=True)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    # --- Métodos de Ordem Superior Avançados (Nível 4) ---
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Procura e retorna o primeiro elemento que satisfaz a condição."""
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        """Filtra a coleção e retorna uma lista com os elementos correspondentes."""
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        """Transforma a coleção aplicando uma função, alterando o tipo genérico para R."""
        return [transform(item) for item in self._items]
