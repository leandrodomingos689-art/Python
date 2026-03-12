class Athlete:
    """Classe que representa um atleta.""" #Класс, представляющий спортсмена
    
    total_athletes = 0  # Atributo de classe # Атрибут класса
    
    def __init__(self, name, age, sport, weight, height):
        """Construtor com validações separadas.""" #Конструктор с отдельными проверками
        self._validate_name(name)
        self._validate_age(age)
        self._validate_sport(sport)
        self._validate_weight(weight)
        self._validate_height(height)
        
        self._name = name.strip()
        self._age = age
        self._sport = sport.strip()
        self._weight = float(weight)
        self._height = float(height)
        self._rating = 1000
        self._active = True
        Athlete.total_athletes += 1
    
    # ===== MÉTODOS DE VALIDAÇÃO SEPARADOS (NÍVEL 5) ===== ОТДЕЛЬНЫЕ МЕТОДЫ ПРОВЕРКИ (УРОВЕНЬ 5)=========
    def _validate_name(self, name):
        if not isinstance(name, str) or len(name.strip()) < 2:
            raise ValueError("Nome inválido") #(Неверное имя)
    
    def _validate_age(self, age):
        if not isinstance(age, int) or age < 12 or age > 100:
            raise ValueError("Idade inválida") #(Недействительный возраст)
    
    def _validate_sport(self, sport):
        if not isinstance(sport, str) or len(sport.strip()) == 0:
            raise ValueError("Esporte inválido") #(Инвалидный спорт)
    
    def _validate_weight(self, weight):
        if not isinstance(weight, (int, float)) or weight < 20 or weight > 300:
            raise ValueError("Peso inválido") #(Неверный вес)
    
    def _validate_height(self, height):
        if not isinstance(height, (int, float)) or height < 100 or height > 250:
            raise ValueError("Altura inválida") #(Недопустимая высота)
    
    # ===== PROPRIEDADES ===== СВОЙСТВО =======
    @property
    def name(self): return self._name
    
    @property
    def age(self): return self._age
    
    @property
    def sport(self): return self._sport
    
    @property
    def weight(self): return self._weight
    
    @property
    def height(self): return self._height
    
    @property
    def rating(self): return self._rating
    
    @property
    def active(self): return self._active
    
    @property
    def imc(self):
        h = self._height / 100
        return round(self._weight / (h * h), 2)
    
    # ===== SETTER COM VALIDAÇÃO ==//== СЕТТЕР С ПРОВЕРКОЙ =====
    @weight.setter
    def weight(self, new_weight):
        self._validate_weight(new_weight)  # Reusa método
        self._weight = float(new_weight)
        print(f"Peso atualizado: {self._weight}kg")
    
    # ===== MÉTODOS DE ESTADO ==//== МЕТОДЫ СОСТОЯНИЯ ====
    def ativar(self):
        self._active = True
        print("Atleta ativado") #Активированный спортсмен
    
    def desativar(self):
        self._active = False
        print("Atleta desativado") #Инвалид спортсмен
    
    # ===== MÉTODOS DE NEGÓCIO ==//==МЕТОДЫ БИЗНЕСА =====
    def treinar(self, mins):
        """Comportamento DEPENDE do estado (NÍVEL 5).""" #Поведение зависит от состояния (Уровень 5)
        if not self._active:
            raise Exception("Atleta inativo não pode treinar") #Неактивный спортсмен не может тренироваться
        self._rating += mins // 10
        print(f"Treino de {mins}min! Rating: {self._rating}")
    
    def competir(self, venceu):
        """Comportamento DEPENDE do estado .""" #Поведение зависит от состояния 
        if not self._active:
            raise Exception("Atleta inativo não pode competir") #Неактивный спортсмен не может соревноваться
        self._rating += 50 if venceu else -20
        if self._rating < 0: self._rating = 0
        print(f"{'Vitória' if venceu else 'Derrota'}! Rating: {self._rating}")
    
    # ===== MÉTODOS MÁGICOS ==//==МАГИЧЕСКИЕ МЕТОДЫ ====
    def __str__(self):
        status = "Ativo" if self._active else "Inativo"
        return f"{self._name} | {self._sport} | {self._age}anos | {self._weight}kg | Rating:{self._rating} | {status}"
    
    def __repr__(self):
        return f"Athlete('{self._name}', {self._age}, '{self._sport}', {self._weight}, {self._height})"
    
    def __eq__(self, other):
        return isinstance(other, Athlete) and self._name == other._name and self._sport == other._sport
    
    def __del__(self):
        Athlete.total_athletes -= 1