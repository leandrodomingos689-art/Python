import sys
import os

# Adiciona o caminho para importar da pasta lib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
Classe Athlete com validações separadas no módulo validation.
"""

from lib.Validation import *


class Athlete:
    """Representa um atleta com encapsulamento e validações."""
    
    # Atributo de classe
    total_athletes = 0
    
    def __init__(self, name, age, sport, weight, height):
        """
        Construtor com validações usando funções externas.
        """
        # VALIDAÇÕES USANDO FUNÇÕES SEPARADAS
        validate_name(name)
        validate_age(age)
        validate_sport(sport)
        validate_weight(weight)
        validate_height(height)
        
        # Atributos privados
        self._name = name.strip()
        self._age = age
        self._sport = sport.strip()
        self._weight = float(weight)
        self._height = float(height)
        self._rating = 1000
        self._active = True
        
        # Incrementa contador
        Athlete.total_athletes += 1
    
    # Propriedades (getters)
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def sport(self):
        return self._sport
    
    @property
    def weight(self):
        return self._weight
    
    @property
    def height(self):
        return self._height
    
    @property
    def rating(self):
        return self._rating
    
    @property
    def imc(self):
        """Índice de Massa Corporal (calculado)."""
        altura_m = self._height / 100
        return round(self._weight / (altura_m ** 2), 2)
    
    # Setter com validação
    @weight.setter
    def weight(self, new_weight):
        """Setter com validação usando função externa."""
        validate_weight(new_weight)
        
        old_weight = self._weight
        self._weight = float(new_weight)
        print(f"Peso atualizado: {old_weight}kg -> {self._weight}kg")
    
    # Métodos de negócio
    def treinar(self, minutos):
        """Registra um treino."""
        if not self._active:
            raise Exception(" Atleta inativo não pode treinar")
        pontos = minutos // 10
        self._rating += pontos
        print (f"Treino de {minutos}min! Rating +{pontos}")
        return
    
    def competir(self, venceu):
        """Registra uma competição."""
        if venceu:
            self._rating += 50
            print (" Vitória! Rating +50")
        else:
            self._rating -= 20
            if self._rating < 0:
                self._rating = 0
            print (" Derrota... Rating -20")
        return
    
    # Métodos de estado
    def ativar(self):
        """Ativa o atleta."""
        self._active = True
        print(" Atleta ativado")
    
    def desativar(self):
        """Desativa o atleta."""
        self._active = False
        print("Atleta desativado")
    
    # Métodos mágicos
    def __str__(self):
        """Representação amigável."""
        status = "Ativo" if self._active else "Inativo"
        return (f"Athlete: {self._name} | {self._sport} | "
                f"{self._age} anos | {self._weight}kg | "
                f"IMC: {self.imc} | Rating: {self._rating} | {status}")
    
    def __repr__(self):
        """Representação técnica."""
        return (f"Athlete('{self._name}', {self._age}, "
                f"'{self._sport}', {self._weight}, {self._height})")
    
    def __eq__(self, other):
        """Comparação por nome e esporte."""
        if not isinstance(other, Athlete):
            return False
        return self._name == other._name and self._sport == other._sport
    