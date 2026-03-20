"""
Módulo de validações para a classe Athlete.
Contém funções reutilizáveis de validação.
"""

def validate_name(name):
    """
    Valida o nome do atleta.
    
    Args:
        name: Nome a ser validado
        
    Returns:
        bool: True se válido
        
    Raises:
        TypeError: Se não for string
        ValueError: Se for vazio ou muito curto
    """
    if not isinstance(name, str):
        raise TypeError("Nome deve ser uma string")
    
    name_clean = name.strip()
    if not name_clean:
        raise ValueError("Nome não pode ser vazio")
    
    if len(name_clean) < 3:
        raise ValueError("Nome deve ter pelo menos 3 caracteres")
    
    return True


def validate_age(age):
    """
    Valida a idade do atleta.
    
    Args:
        age: Idade a ser validada
        
    Returns:
        bool: True se válido
        
    Raises:
        TypeError: Se não for inteiro
        ValueError: Se estiver fora do intervalo [12, 70]
    """
    if not isinstance(age, int):
        raise TypeError("Idade deve ser um número inteiro")
    
    if age < 12 or age > 70:
        raise ValueError("Idade deve estar entre 12 e 70 anos")
    
    return True


def validate_sport(sport):
    """
    Valida o esporte do atleta.
    
    Args:
        sport: Esporte a ser validado
        
    Returns:
        bool: True se válido
        
    Raises:
        TypeError: Se não for string
        ValueError: Se for vazio
    """
    if not isinstance(sport, str):
        raise TypeError("Esporte deve ser uma string")
    
    if not sport.strip():
        raise ValueError("Esporte não pode ser vazio")
    
    return True


def validate_weight(weight):
    """
    Valida o peso do atleta.
    
    Args:
        weight: Peso em kg a ser validado
        
    Returns:
        bool: True se válido
        
    Raises:
        TypeError: Se não for número
        ValueError: Se estiver fora do intervalo [20, 300]
    """
    if not isinstance(weight, (int, float)):
        raise TypeError("Peso deve ser um número")
    
    if weight < 20 or weight > 300:
        raise ValueError("Peso deve estar entre 20kg e 300kg")
    
    return True


def validate_height(height):
    """
    Valida a altura do atleta.
    
    Args:
        height: Altura em cm a ser validada
        
    Returns:
        bool: True se válido
        
    Raises:
        TypeError: Se não for número
        ValueError: Se estiver fora do intervalo [100, 250]
    """
    if not isinstance(height, (int, float)):
        raise TypeError("Altura deve ser um número")
    
    if height < 100 or height > 250:
        raise ValueError("Altura deve estar entre 100cm e 250cm")
    
    return True


def validate_rating(rating):
    """
    Valida o rating do atleta.
    
    Args:
        rating: Rating a ser validado
        
    Returns:
        bool: True se válido
        
    Raises:
        TypeError: Se não for número
        ValueError: Se for negativo
    """
    if not isinstance(rating, (int, float)):
        raise TypeError("Rating deve ser um número")
    
    if rating < 0:
        raise ValueError("Rating não pode ser negativo")
    
    return True