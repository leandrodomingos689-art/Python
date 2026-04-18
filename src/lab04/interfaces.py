from abc import ABC, abstractmethod

class ITrainable(ABC):
    """Interface para objetos que podem ser treinados."""
    @abstractmethod
    def execute_workout(self):
        pass

class IReportable(ABC):
    """Interface para objetos que podem gerar um relatório visual."""
    @abstractmethod
    def get_summary(self) -> str:
        pass
